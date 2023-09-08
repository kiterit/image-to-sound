import pytesseract
from PIL import Image
import pyttsx3
import os

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/haida/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# Image and sound file paths
image_path = 'forest_drama.png'
sound_path = 'forest_sound.mp3'

# Function to perform OCR on the image
def perform_ocr(image_path):
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)
    return text

# Function to play the background sound
def show_Image(sound_path):
    os.system(f"start {sound_path}")

# Main function
def main():
    # Perform OCR on the image
    ocr_text = perform_ocr(image_path)
    print("OCR Text:", ocr_text)

    # Play the background sound
    show_Image(sound_path)

    engine = pyttsx3.init()
    engine.say(ocr_text)
    engine.runAndWait()

if _name_ == "__main__":
    main()