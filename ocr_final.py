import pytesseract
#from main import *
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def ocr(img_name):
    img = Image.open(img_name)
    text = pytesseract.image_to_string(img  , lang='eng')
    return text;


