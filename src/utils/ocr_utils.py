import re
from typing import List, Tuple
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def preprocess_image(image_path):
    """
    Preprocess image for better OCR accuracy:
    - Convert to grayscale
    - Increase contrast
    - Denoise with median filter
    - Resize for clarity
    """
    image = Image.open(image_path).convert('L')
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    image = image.filter(ImageFilter.MedianFilter())

    base_width = 1200
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)

    return image

def extract_text(image_path):
    """
    Extract text from preprocessed image using Tesseract OCR with PSM=6.
    """
    processed_img = preprocess_image(image_path)
    custom_config = '--psm 6'
    text = pytesseract.image_to_string(processed_img, config=custom_config)
    return text

def parse_contact_info(text: str) -> Tuple[List[str], List[str]]:
    """
    Extract emails and phone numbers from text.
    """
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_pattern = re.compile(r"\+?\d[\d -]{8,}\d")

    emails = email_pattern.findall(text)
    phones = phone_pattern.findall(text)
    return emails, phones

def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text using regex.
    """
    url_pattern = re.compile(r"(https?://[^\s]+)|(www\.[^\s]+)", re.IGNORECASE)
    matches = url_pattern.findall(text)
    urls = [u for tup in matches for u in tup if u]
    return urls

def extract_text_and_links(image_file):
    text = extract_text(image_file)
    emails, phones = parse_contact_info(text)
    urls = extract_urls(text)
    return {
        "extracted_text": text,
        "sender_emails": emails,     # Only sender emails from image/text
        "sender_phones": phones,
        "extracted_urls": urls       # Only URLs from image/text
    }

