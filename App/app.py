from flask import Flask, render_template, request, redirect, url_for
import os
import PyPDF2
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.stream as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to split text into sentences
def split_text_into_sentences(text):
    # Split text into sentences using a simple rule based on periods, question marks, and exclamation marks
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def load_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file.readlines()]
    return data

model = tf.keras.models.load_model('models/negation_model.h5')

def predict(new_sentence):
    # Tokenize and preprocess the data
    sentences = load_from_file('models/sen.txt')
    tokenizer = Tokenizer()  # Initialize a tokenizer
    tokenizer.fit_on_texts(sentences)  # Fit the tokenizer on the input sentences to build vocabulary
    sequences = tokenizer.texts_to_sequences(sentences)  # Convert input sentences to sequences of integers
    max_sequence_length = max(len(seq) for seq in sequences)  # Find the maximum sequence length
    new_sequence = tokenizer.texts_to_sequences([new_sentence])
    new_X = pad_sequences(new_sequence, maxlen=max_sequence_length)
    prediction = model.predict(new_X)
    
    if prediction[0][0] >= 0.5:
        return("Affirmed" , f"| Confidence:{100*prediction[0][0]:.4f}%")
    else:
        return("Negated" , f"| Confidence:{100-prediction[0][0]:.4f}%")


# Inference
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            text = extract_text_from_pdf(file)
            sentences = split_text_into_sentences(text)
            negation_results = []

            for sentence in sentences:
                negation_result = predict(sentence)
                negation_results.append(negation_result)

            return render_template('predict.html', text=text, sentences=sentences, negation_results=negation_results)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
