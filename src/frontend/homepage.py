import streamlit as st
import os

def run():
    logo_path = 'src/resources/team_logo.jpg'
    nasc_logo_path = 'src/resources/nasc_logo.png'

    # Header: logo + single-line project title
    header_col, title_col = st.columns([1, 6])
    with header_col:
        if os.path.isfile(logo_path):
            st.image(logo_path, width=100)
        else:
            st.write("Logo Missing")
    with title_col:
        st.markdown(
            "<h1 style='margin-bottom:0; font-size:2.6rem;'>PhishSlayer &ndash; Report to Help Fight Fraud and Scams!</h1>",
            unsafe_allow_html=True)
        st.markdown("<p style='color:#999; font-size:1.2rem;'>Join thousands of Australians in protecting the community by reporting scams and fraud.</p>",
            unsafe_allow_html=True)

    # Main info block
    st.markdown("<h2 style='margin-top:2rem;'>Why Report?</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        - In 2023-24, the **Australian community lost over $2 billion** to scams and fraud.
        - Reports help authorities identify emerging scam trends early.
        - Your anonymous report powers better protections and public warnings.

        <br>
        <strong>Top Scam Types Reported:</strong>
        - Investment scams
        - Phone and SMS scams
        - Online shopping and auction fraud
        - Identity theft

        <br>
        <strong>How Your Report Helps:</strong>
        - Enables targeted investigations.
        - Drives public awareness campaigns.
        - Helps law enforcement focus resources.

        <br>
        For more details, see the <a href='https://www.nasc.gov.au/system/files/targeting-scams-report-2024.pdf' target='_blank'>2024 Targeting Scams Report</a>.
        """, unsafe_allow_html=True
    )

    # NASC logo
    if os.path.isfile(nasc_logo_path):
        st.image(nasc_logo_path, width=1200)

    # Report flow
    st.markdown("---")
    if not st.session_state.get("show_ip_permission", False):
        if st.button("Report Now"):
            st.session_state.show_ip_permission = True
            st.rerun()
    else:
        st.info("We request your permission to collect your IP address to strengthen fraud detection capabilities. Your privacy is protected under Australian laws.\n\nPlease choose whether to allow IP address collection or to remain anonymous.")
        perm_col, anon_col = st.columns(2)
        if perm_col.button("Allow IP Collection"):
            st.session_state.ip_permission_given = True
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()
        if anon_col.button("Remain Anonymous"):
            st.session_state.ip_permission_given = False
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()
