import os
import pandas as pd
from pdf_extractor import extract_text_from_pdf
from preprocessing import clean_text, extract_skills
from similarity import calculate_match_score

# --- CONFIGURATION: DEFINE THE JOB HERE ---
JOB_DESCRIPTION = """
We are looking for a Python Developer with experience in Machine Learning.
Key skills required: Python, Scikit-learn, SQL, Pandas, and Git.
Good communication skills are a plus.
"""
# ------------------------------------------

def main():
    resume_folder = "resumes"
    results = []

    # 1. Extract Skills from the Job Description
    job_skills = extract_skills(JOB_DESCRIPTION)
    print(f"Target Skills for Job: {job_skills}\n")
    print("-" * 50)

    # 2. Loop through all resumes in the folder
    if not os.path.exists(resume_folder):
        print(f"Error: Folder '{resume_folder}' not found. Please create it and add PDFs.")
        return

    files = [f for f in os.listdir(resume_folder) if f.endswith('.pdf')]

    for filename in files:
        file_path = os.path.join(resume_folder, filename)
        
        # A. Extract Text
        resume_text = extract_text_from_pdf(file_path)
        
        # B. Clean & Extract Skills
        cleaned_resume = clean_text(resume_text)
        candidate_skills = extract_skills(cleaned_resume)
        
        # C. Calculate Missing Skills (Skill Gap Analysis)
        missing_skills = job_skills - candidate_skills
        
        # D. Calculate Match Score
        score = calculate_match_score(cleaned_resume, clean_text(JOB_DESCRIPTION))
        
        # Store Data
        results.append({
            "Name": filename,
            "Score (%)": score,
            "Skills Found": ", ".join(list(candidate_skills)),
            "Missing Skills": ", ".join(list(missing_skills)) if missing_skills else "None"
        })

    # 3. Create Ranking (Sort by Score)
    if results:
        df = pd.DataFrame(results)
        df = df.sort_values(by="Score (%)", ascending=False)
        
        print("\n=== RESUME RANKING REPORT ===\n")
        # Print a nice table
        print(df.to_string(index=False))
        
        # Optional: Save to CSV
        df.to_csv("ranking_report.csv", index=False)
        print("\nReport saved to 'ranking_report.csv'")
    else:
        print("No resumes found to process.")

if __name__ == "__main__":
    main()