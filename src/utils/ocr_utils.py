import re
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

def parse_contact_info(text):
    """
    Extract email addresses and phone numbers from text using regex.
    """
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'\+?\d[\d \-\(\)]{7,}\d'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return list(set(emails)), list(set(phones))
