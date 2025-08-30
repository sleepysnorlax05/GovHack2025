import pytesseract
from PIL import Image

def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")
    text = pytesseract.image_to_string(image)
    return text