# Utilities (`src/utils`)

This directory contains various utility functions that support the core functionality of the PhishSlayer application.

### `explainable_ai.py`

This script is responsible for generating user-friendly explanations of the phishing detection results. It uses a local Ollama model to provide clear and concise advice for non-technical users.

### `ip_utils.py`

This utility provides a function to retrieve the user's public IP address. This information is collected with the user's permission to help strengthen fraud detection capabilities.

### `ocr_utils.py`

This script handles Optical Character Recognition (OCR) tasks. It preprocesses uploaded images to improve accuracy and then uses Tesseract OCR to extract text, emails, phone numbers, and URLs from the images.

### `urlhaus.py`

This utility integrates with the URLhaus API from abuse.ch to check for malicious URLs and domains. It helps identify known phishing sites and malware distribution links within the suspicious text.