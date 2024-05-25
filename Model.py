import re
import nltk
from nltk.corpus import stopwords
import pdfplumber  # pdfplumber
from docx import Document

nltk.download('stopwords')
nltk.download('punkt')

class ResumeParser:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
    
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    
    def extract_text_from_docx(self, docx_path):
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    
    def parse_resume(self, text):
        lines = text.split('\n')
        data = {
            'name': None,
            'email': None,
            'phone': None,
            'skills': []
        }
        
        # Extract email and phone
        for line in lines:
            if not data['email']:
                email = re.search(r'[\w\.-]+@[\w\.-]+', line)
                if email:
                    data['email'] = email.group(0)
            if not data['phone']:
                phone = re.search(r'\(?\b[0-9]{3}[-.\s)]*[0-9]{3}[-.\s]*[0-9]{4}\b', line)
                if phone:
                    data['phone'] = phone.group(0)
        
        # Extract skills (simple example)
        for line in lines:
            words = nltk.word_tokenize(line)
            filtered_words = [word for word in words if word.lower() not in self.stop_words]
            if 'skills' in line.lower():
                data['skills'].extend(filtered_words)
        
        return data
