# app.py
# --------------------------------------------------
# Flask web app for AI Resume Scanner
# --------------------------------------------------

from flask import Flask, render_template, request
import pdfplumber
from resume_scanner import calculate_score

app = Flask(__name__)

def extract_text_from_pdf(file) -> str:
    """Extract text from uploaded PDF resume."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        job_description = request.form["job_description"]
        resumes = request.files.getlist("resumes")

        for resume in resumes:
            resume_text = extract_text_from_pdf(resume)

            score, matched, missing = calculate_score(
                resume_text,
                job_description
            )

            results.append({
                "name": resume.filename,
                "score": score,
                "matched": matched,
                "missing": missing
            })

        # Rank resumes (highest score first)
        results.sort(key=lambda x: x["score"], reverse=True)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
