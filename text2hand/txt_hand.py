import pytesseract
from PIL import Image
import os
import pywhatkit as kit
# Change the directory to the location where image is present
os.chdir(r"C:\Users\UserName\Downloads")
# Set the Path of Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\UserName\AppData\Local\Tesseract-OCR\tesseract.exe"
img = Image.open("ImageName.png")  # Load the Image
text = pytesseract.image_to_string(img)  # Convert Image to Text
# Convert Text to Hand Written Text
kit.text_to_handwriting(text, rgb=[0, 0, 250])
