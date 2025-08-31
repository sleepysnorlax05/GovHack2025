# Frontend (`src/frontend`)

This directory contains the Python scripts that define the user interface of the PhishSlayer web application, built using the Streamlit framework.

### `homepage.py`

This script generates the main landing page of the application. It provides an overview of the project, explains the importance of reporting phishing scams, and guides the user through the process of submitting a report.

### `input_page.py`

This page allows users to input the suspicious content they want to analyze. Users can either paste text directly or upload a screenshot of the message. The page collects the user's name and contact information (optional) before proceeding to the analysis.

### `result_page.py`

After the user submits a message for analysis, this page displays the results. It shows the extracted text, the AI-powered prediction (scam or not a scam), and any malicious URLs or domains found in the text. Users can also review and modify the extracted information before submitting a final report.

### `thank_you_page.py`

This page is displayed after a user successfully submits a phishing report. It thanks the user for their contribution and provides some statistics on the impact of community reporting in the fight against scams.