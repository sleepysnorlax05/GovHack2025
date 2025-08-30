import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from frontend.front_end import run_app

def main():
    """
    Main entry point for the Streamlit app.
    """
    run_app()

if __name__ == "__main__":
    main()
