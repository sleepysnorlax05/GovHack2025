# PhishSlayer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PhishSlayer is a lightweight application designed to help users instantly check suspicious emails, SMS, or social media messages for phishing attempts. It combines rule-based detection, AI-assisted analysis, and open threat intelligence databases to provide clear, explainable results.

![PhishSlayer Web App](https://i.imgur.com/TDkCcdX.png)

## The Problem

In 2024, Australians reported losses of **$2.03 billion** to scams, with phishing alone accounting for **$84.5 million** in losses. Many individuals and small to medium-sized enterprises (SMEs) lack the tools and resources to quickly and effectively verify suspicious content, leading to significant financial and reputational damage. PhishSlayer aims to address this challenge by providing a user-friendly and reliable solution for identifying and reporting phishing attempts.

## Features

* **Text and Image Analysis:** Users can either paste suspicious text or upload a screenshot. The application uses Optical Character Recognition (OCR) to extract text and URLs from images.
* **AI-Powered Detection:** A machine learning model analyzes the text for phishing patterns, such as urgent language, suspicious links, and other common scam indicators.
* **Threat Intelligence Integration:** The app cross-references extracted domains and URLs with open-source threat intelligence databases like URLhaus to identify known malicious links.
* **Explainable Results:** PhishSlayer provides a clear risk assessment (High, Medium, or Low) along with a simple explanation of why a message is considered suspicious.
* **Community Reporting:** Users can submit reports of phishing attempts, contributing to a growing database of scams and helping to protect the wider community.

## Application Architecture

The PhishSlayer application follows a hybrid detection pipeline:

1.  **Input Layer:** The user provides input by either pasting text or uploading a screenshot. OCR is used to extract text and URLs from images.
2.  **Rule-Based Engine:** The system detects common phishing indicators, such as urgent language, mismatched domains, shortened links, and suspicious top-level domains (TLDs).
3.  **AI-Assisted Analysis:**
    * **Natural Language Processing (NLP):** Analyzes the text for language patterns associated with risk, such as urgency, threats, or unexpected rewards.
    * **Classification Model:** Uses the `mrm8488/bert-tiny-finetuned-sms-spam-detection` model to classify the text as a potential scam.
4.  **Threat Intelligence Check:** The application cross-references extracted URLs and domains with open threat intelligence databases, including PhishTank, APWG, and URLhaus.
5.  **Output Layer:** The user is presented with a risk level (High, Medium, or Low), a summary of the evidence found, and a recommended course of action.

![Workflow Diagram](https://i.imgur.com/00I2soI.png)

## Getting Started

### Prerequisites

* Docker
* Docker Compose
* Python 3.10+

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/sleepysnorlax05/GovHack2025.git](https://github.com/sleepysnorlax05/GovHack2025.git)
    cd GovHack2025
    ```

2.  **Set up environment variables:**

    Create a `.env` file in the project root and add your Hugging Face API token:

    ```
    HF_API_TOKEN=your_hugging_face_api_token
    ```

3.  **Build and run the application:**

    ```bash
    docker-compose up --build
    ```

    The application will be available at `http://localhost:8501`.

## Future Development

* **Integration with government databases:** Connect with consumer protection and cybersecurity agencies to enhance threat intelligence.
* **Multi-language support:** Expand the application to support multiple languages and protect a wider range of communities.
* **Community reporting system:** Implement a crowdsourcing system for users to report new phishing samples and strengthen the detection models.
* **Browser extension and chatbot:** Develop a browser extension and chatbot to provide real-time scanning and protection within daily workflows.
* **Continuous AI learning:** Continuously improve the classification models with new phishing variants and user feedback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.