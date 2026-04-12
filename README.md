# AI Educational Content Generator

## Overview
This project builds an AI and plants tutor that generates:
- Quizzes(mcq)
- Flashcards
- Audio summaries(in progress)

from educational content like text and PDFs.

## Track
Track A – Essential
# 📘 AI mcq-Quiz Generator

## 📌 Project Description
This project is an AI-powered mcq-quiz generator that converts study material into questions automatically. It helps students learn faster using interactive quizzes and smart content generation.

## Week 1 Goal
- Input text
- Generate mcq-quiz automatically
## ▶️ How to Run the Project

Follow these steps to run the AI mcq-Quiz Generator:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/eshikashetty88-creator/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2️⃣ Install Dependencies
```bash
pip install streamlit
```

(or)

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app/app.py
```

### 4️⃣ Open in Browser
After running, enter a text or topic

---

## Features (Planned)
-mcq-Quiz generation
- Flashcards
- Audio summaries (TTS)
- Study progress tracking

## Tech Stack
- Python
- Streamlit
- app

## 🔧 Import Statements
```python
import streamlit as st
import random
```
## 💻 Code Example
```python
def generate_quiz(text):
    sentences = text.split(".")
    questions = []

    for s in sentences:
        words = s.strip().split()
        if len(words) > 4:
            blank_word = random.choice(words)
            question = s.replace(choose answer")
            questions.append((question, blank_word))

    return questions
```
## 📤 Output Example

Input:
Python is which kind of language?

Output:
a:programming language
b:markup language
c:database language
d:operating language

---------------------------------------------------------------------------------------------------------------------------


📅 Week 3–4: Core Educational Agent Architecture
🎯 Goal
Transform the application into a multi-functional educational assistant capable of processing study material and generating diverse learning resources automatically.
🔹 Implementation Description (Mapped to Checklist)
##✅ Integration of Educational Tools
The system integrates document processing and quiz generation as core educational tools. Uploaded documents are processed to extract text, which is then used to generate quizzes and flashcards dynamically.

##✅ Question Difficulty Levels
Basic difficulty levels—Easy, Medium, and Hard—are implemented to categorize quiz questions. This allows learners to progressively test their understanding based on complexity.

##✅ Multiple Quiz Formats
The educational agent supports multiple quiz formats:
Multiple Choice Questions (MCQs)
True/False questions
Fill-in-the-blanks questions
These formats improve engagement and assess learning from different perspectives.

##✅ Flashcard Review System
A simple flashcard system is implemented where key AI concepts are converted into question-answer pairs. Flashcards are displayed using expandable sections for easy review and quick revision.

##✅ Multiple Document Format Support
The system handles different study material formats, including:
PDF files
TXT files
DOCX files
This ensures flexibility for users to upload various learning resources.

##✅ Study Progress Tracking
Basic study progress tracking is added by:
Evaluating quiz responses
Calculating and displaying user scores
Showing correct answers after quiz submission
This helps users measure their understanding and learning progress.
🏁 Milestone Achieved
By the end of Week 3–4, the educational agent successfully:
Generates multiple types of educational content
Supports document-based learning
Provides interactive quizzes, flashcards, and scoring
The system now functions as a core educational AI assistant designed for intelligent learning support.
# Educational Content Generator AI (Week 3–4)

## Project Overview
This project is an AI-powered educational assistant that generates quizzes and flashcards from uploaded educational documents such as PDFs.

## Features
- Upload PDF documents
- Automatic quiz generation (MCQ)
- Flashcard generation
- Quiz scoring system
- Simple and interactive Streamlit UI
- Study-friendly learning tool

## Tech Stack
- Python
- Streamlit
- PyPDF
- NLP-based text processing

## How to Run Locally
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py

## Deployment
The application is deployed on Streamlit Cloud.

🔗 **Live App Link:**  
https://ai-quiz-generator-hktmvuyz2ivbsgk9grdtxk.streamlit.app/

## Week 3–4 Objectives Completed
- Document processing (PDF upload)
- Quiz generation
- Flashcard system
- Score tracking
- Educational content generation