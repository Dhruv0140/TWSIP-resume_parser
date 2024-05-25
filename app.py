from flask import Flask, request, render_template, redirect, url_for
from Model import ResumeParser
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

resume_parser = ResumeParser()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Determine file type and extract text accordingly
        if file.filename.endswith('.pdf'):
            text = resume_parser.extract_text_from_pdf(file_path)
        elif file.filename.endswith('.docx'):
            text = resume_parser.extract_text_from_docx(file_path)
        else:
            return "Unsupported file format", 400

        parsed_data = resume_parser.parse_resume(text)
        return render_template('index.html', parsed_data=parsed_data)


if __name__ == "__main__":
    app.run(debug=True)
