# Models (`src/models`)

This directory contains the code related to the machine learning model used for phishing detection.

### `detection_model.py`

This script interfaces with a pre-trained phishing detection model hosted on the Hugging Face Hub (`mrm8488/bert-tiny-finetuned-sms-spam-detection`). Key functions include:

* `query_hf_api(text)`: Sends a request to the Hugging Face API with the input text and retrieves the model's prediction.
* `predict_phishing(text)`: Processes the API response to determine the final prediction label (`Scam` or `Not Scam`) and the confidence score.