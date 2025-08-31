import streamlit as st

def run():
    st.markdown(
        "<h1 style='font-size:2.2rem;margin-bottom:0.1em;'>PhishSlayer &ndash; Thank You!</h1>",
        unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.success("Your contribution is vital in the fight against fraud and scams.")

    st.subheader("Impact So Far:")
    st.markdown(
        """
        - Over **1234 reports** submitted by users like you.
        - **987 confirmed scams** detected and prevented.
        - Average scam confidence score of **0.84** aids in prioritizing investigations.
        
        Together, these actions help keep communities safer.
        """
    )

    st.subheader("Report Distribution Map")
    st.image("src/resources/map.png", use_container_width=True)

    if st.button("Return to Homepage"):
        keys_to_keep = ("ip_permission_given",)
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]
        st.session_state.page = "home"
        st.rerun()
