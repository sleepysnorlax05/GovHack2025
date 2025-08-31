import streamlit as st

def run():
    st.title("Report to Help Fight Fraud and Scams!")
    st.markdown(
        """
        **Join thousands of Australians in protecting the community**
        by reporting scams, fraud, and suspicious activities.
        
        ### Why Report?
        
        - In 2023-24, the **Australian community lost over $2 billion** to scams and fraud.
        - Reports help authorities identify emerging scam trends early.
        - Your anonymous report powers better protections and public warnings.
        
        ### Top Scam Types Reported:
        - **Investment scams**
        - **Phone and SMS scams**
        - **Online shopping and auction fraud**
        - **Identity theft**
        
        ### How Your Report Helps
        - Enables targeted investigations.
        - Drives public awareness campaigns.
        - Helps law enforcement focus resources.
        
        For more details, see the [2024 Targeting Scams Report](https://www.nasc.gov.au/system/files/targeting-scams-report-2024.pdf).
        """
    )
    st.image("src/resources/nasc_logo.png", caption="National Scam Reporting Centre")

    if not st.session_state.get("show_ip_permission", False):
        if st.button("Report Now"):
            st.session_state.show_ip_permission = True
            st.rerun()
    else:
        st.info(
            """
            We request your permission to collect your IP address to strengthen fraud detection capabilities.
            Your privacy is protected under Australian laws.
            
            Please choose whether to allow IP address collection or to remain anonymous.
            """
        )
        col1, col2 = st.columns(2)
        if col1.button("Allow IP Collection"):
            st.session_state.ip_permission_given = True
            # IP retrieval handled externally
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()
        if col2.button("Remain Anonymous"):
            st.session_state.ip_permission_given = False
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()
