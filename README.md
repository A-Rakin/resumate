# 🤖 ResuMate

An AI-powered Resume Screening System that automatically analyzes, ranks, and scores resumes against a given job description using NLP and semantic similarity.

This project helps recruiters and hiring teams quickly identify the most relevant candidates by combining skill matching with transformer-based semantic understanding.

## 🚀 Features

### 📄 Resume Processing
• Upload multiple PDF resumes
• Automatic text extraction from PDF files
• Resume parsing and cleaning

### 🧠 AI-Powered Analysis
• Uses Sentence-BERT (SBERT) for semantic similarity
• Skill-based matching (matched & missing skills)
• Semantic understanding of context and experience

### 📊 Smart Scoring
• Automatically ranks resumes by relevance score
• Weighted scoring: 70% semantic similarity + 30% skill match
• Match score displayed as percentage
• Identifies matched and missing skills

### 🎨 User Experience
• Clean & modern UI with responsive design
• Upload multiple files at once
• Clear visual ranking system
• Detailed analysis for each resume

### ⚡ Performance
• Built with Flask (lightweight & fast)
• Fast processing with parallel analysis
• No external API required (runs locally)

## 🧠 How It Works

### Processing Pipeline:
1. **Text Extraction**: Extracts text from uploaded PDF resumes
2. **Text Cleaning**: Cleans & preprocesses text using SpaCy
3. **Semantic Analysis**: Computes semantic similarity between resume & job description
4. **Skill Matching**: Calculates skill overlap score
5. **Final Scoring**: Combines both using weighted scoring

### Scoring Formula:
```bash
Final Score = (0.7 × Semantic Similarity) + (0.3 × Skill Match)
```


### Results Display:
• ✅ Match score (%)
• ✅ Matched skills
• ❌ Missing skills
• 📈 Ranked resume list

## 🛠 Tech Stack

### **Backend**
• **Python** - Core programming language
• **Flask** - Web framework
• **SpaCy** - NLP and text processing
• **Sentence Transformers (SBERT)** - Semantic similarity
• **Scikit-learn** - Machine learning utilities
• **pdfplumber** - PDF text extraction

### **Frontend**
• **HTML** - Structure and content
• **CSS** - Styling and modern UI
• **Jinja2 Templates** - Server-side rendering
• **JavaScript** - Interactive features

## 🎮 How to Use

### 📥 Upload Resumes
1. **Select PDF files**
   • Click "Upload Resumes" button
   • Select multiple PDF files
   • Or drag & drop files directly

2. **Enter job description**
   • Paste the job posting text
   • Include key requirements
   • Add preferred skills

3. **Start Analysis**
   • Click "Analyze Resumes" button
   • Wait for AI processing
   • View ranked results

### 📊 Results Dashboard
• **Ranked List**: Resumes sorted by match score
• **Match Score**: Percentage compatibility
• **Matched Skills**: ✅ Skills found in resume
• **Missing Skills**: ❌ Skills not in resume
• **Detailed View**: Click each resume for details

### 🔧 Advanced Features
• **Filter Results**: Sort by score, experience, or skills
• **Export Results**: Download analysis as CSV
• **Batch Processing**: Analyze multiple job descriptions

## 📦 Installation

### Prerequisites
• Python 3.8 or higher
• pip package manager
