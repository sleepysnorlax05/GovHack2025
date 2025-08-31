import re
import streamlit as st
from src.utils.ocr_utils import extract_text_and_links
from src.models.detection_model import predict_phishing
from src.data.mongodb import save_report
from src.utils.urlhaus import check_domain_urlhaus, check_url_urlhaus

def run_full_pipeline(image_file):
    extraction = extract_text_and_links(image_file)
    text = extraction["extracted_text"]
    label, score = predict_phishing(text)
    extraction.update({
        "prediction_label": label,
        "prediction_score": score,
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

def parse_sender_contacts(text):
    items = [x.strip() for x in text.split(",") if x.strip()]
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_pattern = re.compile(r"\+?\d[\d -]{8,}\d")
    emails = [i for i in items if email_pattern.fullmatch(i)]
    phones = [i for i in items if phone_pattern.fullmatch(i)]
    return emails, phones

def run():
    st.markdown(
        "<h1 style='font-size:2.2rem;margin-bottom:0.1em;'>PhishSlayer &ndash; Analysis Results</h1>",
        unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='color:#999;'>Review your submission and see scam detection insights below.</p>", unsafe_allow_html=True)

    if st.session_state.get("redirect_to_thank_you", False):
        st.session_state["redirect_to_thank_you"] = False
        st.session_state.page = "thank_you"
        st.rerun()

    if "pipeline_result" not in st.session_state:
        with st.spinner("Analyzing submission..."):
            result = run_full_pipeline(st.session_state.uploaded_file)
            st.session_state.pipeline_result = result
    else:
        result = st.session_state.pipeline_result

    label_map = {"LABEL_0": "Not Scam", "LABEL_1": "Scam"}
    label_text = label_map.get(result["prediction_label"], "Unknown")
    st.metric("Prediction", f"{label_text} ({result['prediction_score']:.2f})")

    st.subheader("Extracted Text")
    st.text_area("OCR Text", result["extracted_text"], height=200, disabled=True)

    st.subheader("Sender Contact Information")
    sender_contacts_default = ", ".join(result["sender_emails"] + result["sender_phones"])
    modified_sender_contacts = st.text_area(
        "Sender emails / phone numbers found in image/text (please verify or modify):",
        value=sender_contacts_default,
        height=60,
    )
    st.session_state.modified_sender_contacts = modified_sender_contacts

    st.subheader("Extracted URLs")
    urls_default = ", ".join(result["extracted_urls"])
    modified_urls = st.text_area(
        "URLs found in image/text (please verify or modify):",
        value=urls_default,
        height=60,
    )
    st.session_state.modified_extracted_urls = modified_urls

    emails, phones = parse_sender_contacts(modified_sender_contacts)
    url_list = [u.strip() for u in modified_urls.split(",") if u.strip()]

    malicious_domains = check_sender_domains(emails)
    if malicious_domains:
        st.warning("⚠️ These sender email domains were reported in scam databases:")
        for d in malicious_domains.keys():
            st.write(f"- {d}")
    else:
        st.info("No sender email domains found in URLhaus scam database.")

    malicious_urls = check_extracted_urls(url_list)
    if malicious_urls:
        st.warning("⚠️ These URLs found in the image/text were reported in scam databases:")
        for url in malicious_urls.keys():
            st.write(f"- {url}")
    else:
        st.info("No extracted URLs matched known scam reports.")

    st.markdown("---")
    if not st.session_state.get("report_submitted", False):
        if st.button("Submit Report"):
            report_data = {
                "user_name": st.session_state.user_name,
                "user_contact": st.session_state.user_emails,
                "sender_contacts": modified_sender_contacts,
                "extracted_urls": modified_urls,
                "extracted_text": result["extracted_text"],
                "prediction_label": result["prediction_label"],
                "prediction_score": result["prediction_score"],
                "ip_permission": st.session_state.get("ip_permission_given", None),
                "user_ip": st.session_state.get("user_ip"),
            }
            inserted_id = save_report(report_data)
            st.session_state.report_submitted = True
            st.session_state.inserted_report_id = inserted_id
            st.session_state["redirect_to_thank_you"] = True
            st.rerun()
    else:
        st.success("Report submitted! Redirecting to thank you page...")
