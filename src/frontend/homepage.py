import streamlit as st

def run():
    st.title("Report to help fight fraud!")
    st.write("Protect your community by reporting fraud, scams, and bad business practices.")
    st.image("https://via.placeholder.com/1000x300.png?text=Homepage+Banner")

    # Show "Report Now" button only if not showing the IP permission banner
    if not st.session_state.get("show_ip_permission", False):
        if st.button("Report Now"):
            st.session_state.show_ip_permission = True
            st.rerun()

    # Show IP permission popup after button click
    elif st.session_state.get("show_ip_permission", False) and "ip_permission_given" not in st.session_state:
        st.info(
            """
            We would like to retrieve your IP address to enhance fraud detection.
            Your data will be securely handled in compliance with Australian privacy laws.

            Please choose to allow IP collection or remain anonymous.
            """
        )
        col1, col2 = st.columns(2)
        if col1.button("Allow IP Collection"):
            st.session_state.ip_permission_given = True
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()
        if col2.button("Remain Anonymous"):
            st.session_state.ip_permission_given = False
            st.session_state.show_ip_permission = False
            st.session_state.page = "input"
            st.rerun()

    # This else block disables other UI when permission banner shows
    else:
        st.stop()
