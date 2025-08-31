import streamlit as st

def run():
    st.title("PhishSlayer - Report Submission")
    user_name = st.text_input("Your Name")
    user_emails = st.text_area("Your Emails / Phone Numbers (comma separated)")
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
