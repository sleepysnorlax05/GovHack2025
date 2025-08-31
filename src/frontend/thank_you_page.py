import streamlit as st

def run():
    st.title("Thank You For Submitting Your Report!")
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
    # Replace with real map visualization when available
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/07/Australia_location_map_with_states_and_territories.png", caption="Map of Reported Scams by Region")

    if st.button("Return to Homepage"):
        # Reset session state except IP permission for better UX
        keys_to_keep = ("ip_permission_given",)
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]
        st.session_state.page = "home"
        st.rerun()
