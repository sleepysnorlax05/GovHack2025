import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_API_TOKEN:
    raise EnvironmentError("Missing HF_API_TOKEN in environment variables")

HF_MODEL_ENDPOINT = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_hf_api(text):
    """
    Query the Hugging Face API for phishing detection.
    Args:
        text (str): The input text to classify.
    Returns:
        dict: The JSON response from the API.
    """
    payload = {"inputs": text}
    response = requests.post(HF_MODEL_ENDPOINT, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()

def predict_phishing(text):
    """
    Predict if the given text is a phishing attempt using a Hugging Face model.
    Args:
        text (str): The input text to classify.
    Returns:
        tuple: (label, score) where label is 'LABEL_0' or 'LABEL_1' 
        and score is the confidence score.
    Note:
        The text is truncated to the first 512 characters to fit model input constraints.
    """

    result = query_hf_api(text[:512])
    predictions = result[0]
    best_pred = max(predictions, key=lambda x: x['score'])
    label = best_pred['label']
    score = best_pred['score']
    return label, score