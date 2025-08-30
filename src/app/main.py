import os
import sys
import streamlit as st
from dotenv import load_dotenv

# Set up proper imports for a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.ocr_utils import extract_text_from_image, parse_contact_info
from src.models.detection_model import predict_phishing

# Load environment variables
load_dotenv()

def main():
    """
    Streamlit app for phishing detection from image uploads.
    1. Upload an image (screenshot of SMS/email).
    2. Extract text using OCR.
    3. Parse for emails and phone numbers.
    4. Predict if the message is a phishing attempt.
    5. Display results.
    """
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

        label, score = predict_phishing(text)
        label_map = {'LABEL_0': 'Not Scam', 'LABEL_1': 'Scam'}
        outcome = label_map.get(label, "Unknown")
        st.write(f"Phishing Prediction: **{outcome}** (Confidence: {score:.2f})")

if __name__ == "__main__":
    main()