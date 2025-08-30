import streamlit as st

def run():
    st.title("Thank You For Submitting Your Report!")
    st.success("Your contribution helps fight fraud.")

    st.subheader("Current Phishing & Scam Statistics")
    st.write("- Total reports submitted: 1234")
    st.write("- Total scams detected: 987")
    st.write("- Average confidence score: 0.84")

    st.subheader("Report Distribution Map (placeholder)")
    st.image("https://via.placeholder.com/700x400.png?text=Heatmap+Placeholder")

    if st.button("Return to Homepage"):
        # Clear session state except IP consent for smoother UX
        keys_to_keep = ("ip_permission_given",)
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]
        st.session_state.page = "home"
        st.rerun()