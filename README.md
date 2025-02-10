# Bangla-English OCR and Translator

This is a Flask-based web application that allows users to upload images containing Bangla and English text. The application extracts the text using EasyOCR and provides an option to translate between Bangla and English.

## Features

- Upload an image to extract Bangla and English text
- Display the extracted text on the webpage
- Translate the extracted text between Bangla and English

## Technologies Used

- Python
- Flask
- EasyOCR
- DeepTranslator
- HTML, CSS, JavaScript

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/RohanFardin/Bangla-English-Text-Recognition.git
cd Bangla-English-Text-Recognition
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

#### Required Libraries:

- Flask
- EasyOCR
- DeepTranslator

If `requirements.txt` is missing, install them manually:

```sh
pip install flask easyocr deep-translator
```

### 4. Run the Application

```sh
python app.py
```

The application will start at `http://127.0.0.1:5000/`.

## Project Structure

```
Bangla-English-Text-Recognition/
│-- templates/
│   ├── index.html (Frontend UI)
│-- static/uploads/ (Uploaded images are stored here)
│-- app.py (Main application file)
│-- .gitignore (Files to ignore in Git)
│-- requirements.txt (Dependencies list)
```

## How to Use

1. Open http\://127.0.0.1:5000/ in a browser.
2. Upload an image containing Bangla or English text.
3. The extracted text will be displayed on the screen.
4. Click the translation button to translate between Bangla and English.

## Deployment

To deploy on a cloud platform, you may need to configure:

- Gunicorn (for production server):
  ```sh
  pip install gunicorn
  gunicorn -w 4 app:app
  ```
- Deploy on services like **Heroku, AWS, or Render**.

## .gitignore

Ensure you have the following in `.gitignore` to avoid committing unnecessary files:

```
venv/
__pycache__/
static/uploads/*
*.pyc
.env
```

## Future Improvements

- Add support for more languages.
- Enhance the UI with better styling.
- Deploy on cloud for public use.

---

**Author:** Rohan Fardin\
GitHub: [github.com/RohanFardin](https://github.com/RohanFardin)

