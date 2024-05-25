# Resume Parser Application

This project is a Resume Parser application built using Python and Natural Language Processing (NLP). The application extracts relevant information from uploaded resumes, such as name, contact details, skills, and experience.

## Project Structure

```
ResumeParser/
├── app.py
├── model.py
├── templates/
│   └── index.html
├── uploads/
│   ├── example_resume1.pdf
│   ├── example_resume2.pdf
├── output/
│   └── parsed_output.mp4
├── README.md

```

### File Descriptions

- `app.py`: This is the main script for running the web application. It sets up the Flask server and handles HTTP requests and responses, including file uploads.
- `model.py`: This script contains the logic for parsing resumes, including loading the model, extracting information, and formatting the output.
- `templates/index.html`: This is the HTML template for the web application's user interface.
- `uploads/`: This folder contains example resumes used for testing the application.
- `output/parsed_output.mp4`: This is a video demonstrating the output of the resume parser.

## Prerequisites

- Python 3.6 or higher
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/resume-parser.git
    cd resume-parser
    ```

2. **Set up a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

## Running the Application

1. **Start the Flask server:**
    ```sh
    python app.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000
    ```

3. **Upload a resume** in PDF format and see the parsed information.

## Detailed Descriptions

### `app.py`

This script sets up a Flask web application. The main routes are defined here, including the route for file uploads and displaying the parsed information.

### `model.py`

This script contains the core logic for parsing resumes. It utilizes NLP techniques to extract information such as personal details, skills, work experience, and education.

### `index.html`

A basic HTML form to upload resumes and display the parsed output.

### `uploads/`

This folder contains example resumes for testing the application. You can add more resumes to this folder to test the parser with different formats.

### `output/parsed_output.mp4`

A video demonstrating the output of the resume parser, showcasing how the application works and the kind of information it extracts.

## Future Enhancements

- Improve the accuracy of the parser with more sophisticated NLP models.
- Add support for different resume formats (e.g., DOCX).
- Enhance the user interface with CSS and JavaScript for a better user experience.
- Integrate with a database to store parsed resume information for future reference.
- Implement additional features such as keyword extraction and matching resumes to job descriptions.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.
