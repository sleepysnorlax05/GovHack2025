import streamlit as st
from src.utils.ocr_utils import extract_text, parse_contact_info
from src.models.detection_model import predict_phishing


def run_full_pipeline(image_file):
    """
    Runs complete pipeline:
    - OCR extraction
    - Parsing contacts (for sender info)
    - Phishing prediction
    """
    text = extract_text(image_file)
    emails, phones = parse_contact_info(text)
    label, score = predict_phishing(text)
    return {
        'extracted_text': text,
        'parsed_sender_emails': emails,
        'parsed_sender_phones': phones,
        'prediction_label': label,
        'prediction_score': score
    }


def input_page():
    st.title("XPhish Vision - Report Submission")

    user_name = st.text_input("Your Name")
    user_emails = st.text_area("Your Emails / Phone Numbers (comma separated)")
    uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])

    if st.button("Submit"):
        if not uploaded_file:
            st.error("Please upload a screenshot before submitting.")
            return

        st.session_state.user_name = user_name
        st.session_state.user_emails = user_emails
        st.session_state.uploaded_file = uploaded_file
        st.session_state.page = "result"
        # Clear previous pipeline results on new submission
        st.session_state.pop('pipeline_result', None)
        st.rerun()


def result_page():
    st.title("Analysis Results")

    with st.spinner("Analyzing submission..."):
        if 'pipeline_result' not in st.session_state:
            result = run_full_pipeline(st.session_state.uploaded_file)
            st.session_state.pipeline_result = result
        else:
            result = st.session_state.pipeline_result

    label_map = {'LABEL_0': 'Not Scam', 'LABEL_1': 'Scam'}
    label_text = label_map.get(result['prediction_label'], "Unknown")

    st.subheader("Prediction")
    st.write(f"**{label_text}** (Confidence: {result['prediction_score']:.2f})")

    st.subheader("Extracted Text")
    st.text_area("OCR Text", result['extracted_text'], height=300, disabled=True)

    st.subheader("Sender Contact Information")
    # Editable sender contact fields pre-filled with parsed values
    initial_sender = ', '.join(result['parsed_sender_emails'] + result['parsed_sender_phones'])
    sender_contact = st.text_area(
        "Sender Emails / Phone Numbers (please verify or modify):",
        value=initial_sender,
        height=80
    )
    st.session_state.modified_sender_contact = sender_contact

    st.subheader("Your Contact Information")
    st.write(st.session_state.user_name)
    st.write(st.session_state.user_emails)

    if st.button("Submit Final Report"):
        # TODO: implement saving report with st.session_state.modified_sender_contact and other info
        st.success("Report submitted successfully!")
        # Reset session state for a fresh submission
        st.session_state.page = "input"
        st.session_state.pop('pipeline_result', None)
        st.rerun()

    if st.button("Edit Original Submission"):
        st.session_state.page = "input"
        st.rerun()


def run_app():
    if 'page' not in st.session_state:
        st.session_state.page = "input"

    if st.session_state.page == "input":
        input_page()
    else:
        result_page()
