import re
import pytesseract
from PIL import Image

def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")
    text = pytesseract.image_to_string(image)
    return text

def parse_contact_info(text):
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    phone_pattern = r'\+?\d[\d \-\(\)]{7,}\d'
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    return emails, phones