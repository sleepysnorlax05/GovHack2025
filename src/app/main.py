import streamlit as st

st.title("XPhish Vision - Phishing Detection Demo")

st.write("Upload a screenshot of suspicious SMS or email to start.")

uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_column_width=True)
    st.success("File received! Next steps coming soon...")
