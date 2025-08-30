import streamlit as st
from src.utils.ocr_utils import extract_text, parse_contact_info
from src.models.detection_model import predict_phishing
from src.data.mongodb import save_report

def run_full_pipeline(image_file):
    text = extract_text(image_file)
    emails, phones = parse_contact_info(text)
    label, score = predict_phishing(text)
    return {
        "extracted_text": text,
        "parsed_sender_emails": emails,
        "parsed_sender_phones": phones,
        "prediction_label": label,
        "prediction_score": score,
    }

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
            }
            inserted_id = save_report(report_data)
            st.session_state.report_submitted = True
            st.session_state.inserted_report_id = inserted_id
            st.session_state.page = "thank_you"
            st.rerun()
    else:
        st.success("Report submitted! Redirecting to thank you page...")
        st.session_state.page = "thank_you"
        st.rerun()
