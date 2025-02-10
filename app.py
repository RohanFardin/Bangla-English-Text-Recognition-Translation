import os
import easyocr
from flask import Flask, request, render_template, redirect, jsonify
from deep_translator import GoogleTranslator
import re

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['bn', 'en'], gpu=False)

def process_image(image_path):
    img = reader.readtext(image_path, paragraph=True)
    text = '\n'.join(word[1] for word in img)
    return text

def get_button_text(text):
    has_bangla = bool(re.search(r"[\u0980-\u09FF]", text))
    has_english = bool(re.search(r"[A-Za-z]", text))

    if has_bangla and not has_english:
        return "Translate to English"
    elif has_english and not has_bangla:
        return "Translate to Bangla"
    elif has_bangla and has_english:
        return "Translate"
    else:
        return ""

def translation(text):
    has_bangla = bool(re.search(r"[\u0980-\u09FF]", text))
    has_english = bool(re.search(r"[A-Za-z]", text))

    if has_bangla and not has_english:
        translated_text = GoogleTranslator(source="bn", dest="en").translate(text)
    elif has_english and not has_bangla:
        translated_text = GoogleTranslator(source="en", dest="bn").translate(text)
    elif has_bangla and has_english:
        translated_text = GoogleTranslator(source="auto", dest="en").translate(text)
    else:
        return "No translatable text found", ""

    # Determine button text based on translated text
    new_has_bangla = bool(re.search(r"[\u0980-\u09FF]", translated_text))
    new_has_english = bool(re.search(r"[A-Za-z]", translated_text))

    if new_has_bangla and not new_has_english:
        button_text = "Translate to English"
    elif new_has_english and not new_has_bangla:
        button_text = "Translate to Bangla"
    elif new_has_bangla and new_has_english:
        button_text = "Translate"
    else:
        button_text = ""

    return translated_text, button_text

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_text = process_image(filepath)
            button_text = get_button_text(extracted_text)
            return render_template("index.html", uploaded_image=file.filename, text=extracted_text, button_text=button_text)

    return render_template("index.html", uploaded_image=None, text=None, button_text=None)

@app.route("/translate", methods=["POST"])
def translate_text():
    text = request.json.get("text", "")
    translated_text, button_text = translation(text)
    return jsonify({"translated_text": translated_text, "button_text": button_text})

if __name__ == "__main__":
    app.run(debug=True)