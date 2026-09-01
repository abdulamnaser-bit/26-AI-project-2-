import requests
import pyautogui
import tempfile
import base64

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_screen_image(prompt):

    with tempfile.NamedTemporaryFile(
        suffix=".png",
        delete=False
    ) as temp:

        image_path = temp.name

    img = pyautogui.screenshot(
        region=(200, 100, 1400, 800)
    )

    img.save(image_path)

    # Convert image to Base64
    with open(image_path, "rb") as img:
        image_b64 = base64.b64encode(
            img.read()
        ).decode("utf-8")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llava",
            "prompt": prompt,
            "images": [image_b64],
            "stream": False
        }
    )

    data = response.json()

    print(data)

    return data.get(
        "response",
        "Boss, I couldn't analyze the image."
    )