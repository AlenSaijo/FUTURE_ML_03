# FUTURE_ML_03
FUTURE INTERN TASK 03
Resume Screening System
An automated recruitment tool designed to parse, analyze, and rank candidate resumes against specific job descriptions using Natural Language Processing (NLP) and Machine Learning.

🚀 Features
Automated Parsing: Extracts text content from multiple PDF resumes simultaneously.

Advanced Preprocessing: Cleans data by removing stop words, special characters, and formatting noise.

Similarity Scoring: Utilizes Cosine Similarity to calculate the mathematical distance between resume content and job requirements.

Web Interface: User-friendly dashboard built with Flask for easy file uploads.

Exportable Analytics: Generates a ranking_report.xlsx for recruiters to download and review.

🛠️ Technical Stack
Backend: Python, Flask

NLP & ML: Scikit-learn (TfidfVectorizer), NLTK, PyMuPDF (or your PDF extractor)

Frontend: HTML5, CSS3 (Bootstrap)

Data Handling: Pandas, Openpyxl (for Excel reports)

📁 Project Structure
Plaintext
├── app.py              # Flask Web Server
├── main.py             # Logic Orchestration
├── pdf_extractor.py    # PDF Text Extraction Module
├── preprocessing.py    # NLP Cleaning Logic
├── similarity.py       # ML Ranking Algorithm
├── templates/          # HTML Web Pages
└── resumes/            # Directory for uploaded resumes
⚙️ How to Run
Clone the repository:

Bash
git clone https://github.com/your-username/resume-screening-system.git
Install dependencies:

Bash
pip install -r requirements.txt
Launch the application:

Bash
python app.py
Open http://127.0.0.1:5000 in your browser.
