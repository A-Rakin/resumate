# resume_scanner.py
# --------------------------------------------------
# Core AI logic for resume–job description matching
# --------------------------------------------------

import re
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP models
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Skill knowledge base (extend freely)
SKILLS = {
    "python", "sql", "machine learning", "deep learning",
    "data analysis", "data visualization", "nlp",
    "tensorflow", "pytorch", "statistics",
    "cloud computing", "aws", "azure", "docker"
}

def clean_text(text: str) -> str:
    """Lowercase, clean, lemmatize, remove stopwords."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    doc = nlp(text)
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(tokens)

def extract_skills(text: str) -> set:
    """Extract known skills from text."""
    found = set()
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return found

def calculate_score(resume_text: str, jd_text: str):
    """
    Calculate final resume score.
    Returns:
        score (0–100),
        matched_skills,
        missing_skills
    """

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    # Semantic similarity (SBERT)
    embeddings = model.encode([resume_clean, jd_clean])
    semantic_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    # Skill matching
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)

    matched_skills = resume_skills & jd_skills
    missing_skills = jd_skills - resume_skills

    skill_score = len(matched_skills) / max(len(jd_skills), 1)

    # Weighted final score
    final_score = (0.7 * semantic_score) + (0.3 * skill_score)

    return round(final_score * 100, 2), matched_skills, missing_skills
