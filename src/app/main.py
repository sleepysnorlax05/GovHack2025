import sys
import os
import streamlit as st

# Add project root to Python path
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from src.utils.ocr_utils import extract_text_from_image, parse_contact_info

st.title("Phishing Detection Demo")

st.write("Upload a screenshot of suspicious SMS or email to start.")

uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)
    
    # Reset file pointer to beginning
    uploaded_file.seek(0)
    
    # Process the image
    text = extract_text_from_image(uploaded_file)
    st.write("Extracted Text Preview:")
    st.text(text[:300])

    emails, phones = parse_contact_info(text)
    st.write("Detected Emails:", emails)
    st.write("Detected Phone Numbers:", phones)