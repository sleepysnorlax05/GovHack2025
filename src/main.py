import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st

def main():
    page = st.session_state.get("page", "home")

    if page == "home":
        from src.frontend.homepage import run as homepage
        homepage()
    elif page == "input":
        from src.frontend.input_page import run as input_page
        input_page()
    elif page == "result":
        from src.frontend.result_page import run as result_page
        result_page()
    elif page == "thank_you":
        from src.frontend.thank_you_page import run as thank_you_page
        thank_you_page()
    else:
        st.error("Unknown page.")

if __name__ == "__main__":
    main()
