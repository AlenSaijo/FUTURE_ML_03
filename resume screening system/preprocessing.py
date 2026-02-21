import re

# A basic database of technical skills to look for
SKILL_DB = {
    'python', 'java', 'c++', 'html', 'css', 'javascript', 'react', 'node', 
    'sql', 'mysql', 'mongodb', 'aws', 'docker', 'kubernetes', 'git', 
    'machine learning', 'data analysis', 'pandas', 'numpy', 'scikit-learn',
    'communication', 'teamwork', 'problem solving', 'flask', 'django'
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'\s+', ' ', text)      # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)   # Remove punctuation
    return text

def extract_skills(text):
    found_skills = set()
    cleaned_text = clean_text(text)
    words = set(cleaned_text.split())
    
    # Check for single-word skills
    for word in words:
        if word in SKILL_DB:
            found_skills.add(word)
            
    # Check for multi-word skills (like "machine learning")
    for skill in SKILL_DB:
        if " " in skill and skill in cleaned_text:
            found_skills.add(skill)
            
    return found_skills