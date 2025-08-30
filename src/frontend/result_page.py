import re
import streamlit as st
from src.utils.ocr_utils import extract_text_and_links
from src.models.detection_model import predict_phishing
from src.data.mongodb import save_report
from src.utils.urlhaus import check_domain_urlhaus, check_url_urlhaus

def run_full_pipeline(image_file):
    """
    Run OCR extraction, contact and URL parsing, and phishing prediction.
    """
    extraction = extract_text_and_links(image_file)
    text = extraction["extracted_text"]
    emails = extraction["parsed_sender_emails"]
    phones = extraction["parsed_sender_phones"]
    urls = extraction["extracted_urls"]

    label, score = predict_phishing(text)
    extraction.update({
        "prediction_label": label,
        "prediction_score": score,
        "extracted_urls": urls,
        "parsed_sender_emails": emails,
        "parsed_sender_phones": phones,
    })
    return extraction

def get_domains_from_emails(emails):
    domains = set()
    for email in emails:
        match = re.search(r"@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$", email.strip())
        if match:
            domains.add(match.group(1).lower())
    return list(domains)

def check_sender_domains(emails):
    domains = get_domains_from_emails(emails)
    malicious_domains = {}
    for domain in domains:
        is_malicious, details = check_domain_urlhaus(domain)
        if is_malicious:
            malicious_domains[domain] = details
    return malicious_domains

def check_extracted_urls(urls):
    malicious_urls = {}
    for url in urls:
        is_malicious, details = check_url_urlhaus(url)
        if is_malicious:
            malicious_urls[url] = details
    return malicious_urls

def run():
    st.title("Analysis Results")

    if "pipeline_result" not in st.session_state:
        with st.spinner("Analyzing submission..."):
            result = run_full_pipeline(st.session_state.uploaded_file)
            st.session_state.pipeline_result = result
    else:
        result = st.session_state.pipeline_result

    label_map = {"LABEL_0": "Not Scam", "LABEL_1": "Scam"}
    label_text = label_map.get(result["prediction_label"], "Unknown")

    st.subheader("Prediction")
    st.write(f"**{label_text}** (Confidence: {result['prediction_score']:.2f})")

    st.subheader("Extracted Text")
    st.text_area("OCR Text", result["extracted_text"], height=300, disabled=True)

    st.subheader("Sender Contact Information")
    initial_sender = ", ".join(result["parsed_sender_emails"] + result["parsed_sender_phones"])
    sender_contact = st.text_area(
        "Sender Emails / Phone Numbers (please verify or modify):",
        value=initial_sender,
        height=80,
    )
    st.session_state.modified_sender_contact = sender_contact

    st.subheader("Your Contact Information")
    st.write(st.session_state.user_name)
    st.write(st.session_state.user_emails)

    # Check sender domains against URLhaus
    malicious_domains = check_sender_domains(result["parsed_sender_emails"])
    if malicious_domains:
        st.warning("⚠️ The following sender domains have been reported in scam databases:")
        for domain in malicious_domains.keys():
            st.write(f"- {domain}")
    else:
        st.info("Sender domains were not found in the scam URLhaus database.")

    # Check extracted URLs against URLhaus
    malicious_urls = check_extracted_urls(result["extracted_urls"])
    if malicious_urls:
        st.warning("⚠️ The following URLs found in the submission have been reported in scam databases:")
        for url in malicious_urls.keys():
            st.write(f"- {url}")
    else:
        st.info("No URLs in the submission matched known scam reports.")

    if "report_submitted" not in st.session_state:
        if st.button("Submit Report"):
            report_data = {
                "user_name": st.session_state.user_name,
                "user_contact": st.session_state.user_emails,
                "sender_contact": st.session_state.modified_sender_contact,
                "extracted_text": result["extracted_text"],
                "prediction_label": result["prediction_label"],
                "prediction_score": result["prediction_score"],
                "ip_permission": st.session_state.get("ip_permission_given", None),
                "user_ip": st.session_state.get("user_ip"),  # stored silently
            }
            inserted_id = save_report(report_data)
            st.session_state.report_submitted = True
            st.session_state.inserted_report_id = inserted_id
            st.session_state.page = "thank_you"
            st.rerun()
    else:
        st.success("Report submitted successfully!")
        st.session_state.page = "thank_you"
        st.rerun()
