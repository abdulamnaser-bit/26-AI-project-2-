import pyautogui
import pytesseract
from PIL import Image
import tempfile
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def read_screen():

    try:

        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as temp:

            path = temp.name

        pyautogui.screenshot(path)

        img = Image.open(path)

        # Convert to grayscale
        img = img.convert("L")

        # Enlarge image for OCR
        width, height = img.size

        img = img.resize(
            (width * 2, height * 2)
        )

        # Better OCR mode
        text = pytesseract.image_to_string(
            img,
            config="--oem 3 --psm 6"
        )

        print("\n===== SCREEN TEXT =====")
        print(text)
        print("=======================\n")

        os.remove(path)

        return text.strip()

    except Exception as e:

        print("VISION ERROR:", e)

        return "Boss, I couldn't read the screen."