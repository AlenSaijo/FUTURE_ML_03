from flask import Flask, render_template
import os
from pdf_extractor import extract_text_from_pdf
from preprocessing import clean_text, extract_skills
from similarity import calculate_match_score

app = Flask(__name__)

# --- CONFIGURATION ---
JOB_DESCRIPTION = """
We are looking for a Python Developer with experience in Machine Learning.
Key skills required: Python, Scikit-learn, SQL, Pandas, and Git.
Good communication skills are a plus.
"""
UPLOAD_FOLDER = 'resumes'
# ---------------------

@app.route('/')
def index():
    results = []
    
    # Get target skills from Job Description
    job_skills = extract_skills(JOB_DESCRIPTION)

    # Check if folder exists
    if os.path.exists(UPLOAD_FOLDER):
        files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.pdf')]

        for filename in files:
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            
            # 1. Extract & Clean
            resume_text = extract_text_from_pdf(file_path)
            cleaned_resume = clean_text(resume_text)
            
            # 2. Get Skills
            candidate_skills = extract_skills(cleaned_resume)
            missing_skills = job_skills - candidate_skills
            
            # 3. Calculate Score
            score = calculate_match_score(cleaned_resume, clean_text(JOB_DESCRIPTION))
            
            # 4. Add to list
            results.append({
                "name": filename,
                "score": score,
                "found_skills": ", ".join(list(candidate_skills)),
                "missing_skills": ", ".join(list(missing_skills)) if missing_skills else "None"
            })

    # Sort by Score (High to Low)
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    
    return render_template('index.html', results=results, job_desc=JOB_DESCRIPTION)

if __name__ == '__main__':
    app.run(debug=True, port=8080)