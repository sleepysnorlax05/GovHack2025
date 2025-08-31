import streamlit as st

def run():
    # Unified header
    st.markdown(
        "<h1 style='font-size:2.2rem;margin-bottom:0.1em;'>PhishSlayer &ndash; Report Submission</h1>",
        unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='color:#999;'>Tell us who you are and upload the evidence you'd like scanned and checked.</p>", unsafe_allow_html=True)
    
    user_name = st.text_input("Your Name")
    user_emails = st.text_area("Your Emails / Phone Numbers (comma separated)", height=70)
    uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])

    if st.button("Proceed"):
        if not uploaded_file:
            st.error("Please upload a screenshot before proceeding.")
            return
        st.session_state.user_name = user_name
        st.session_state.user_emails = user_emails
        st.session_state.uploaded_file = uploaded_file
        st.session_state.page = "result"
        st.rerun()
