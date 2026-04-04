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

📅 Week 3–4: Quiz Generation, Flashcards & Score Evaluation
During Week 3 and Week 4, the project was enhanced with advanced AI-based learning features focused on content understanding, assessment, and progress tracking.
🔹 Key Features Implemented
PDF Upload & Text Extraction
Users can upload AI-related PDF documents.
Text is extracted automatically using document processing techniques.
AI-Based Quiz Generator (MCQs)
Multiple-choice questions are generated from the uploaded content.
Each quiz includes questions, multiple options, and correct answers.
Users can attempt quizzes directly in the application.
Quiz Scoring System
User responses are evaluated.
Final score is calculated and displayed after quiz submission.
Correct answers are shown for learning reinforcement.
Flashcard Generator
Important AI concepts are converted into flashcards.
Each flashcard displays a concept title and its explanation.
Improves quick revision and concept clarity.
Interactive Streamlit Interface
Buttons for generating quizzes and flashcards.
Expandable cards for better UI/UX.
Real-time feedback messages (success, score display).
🔹 Technologies Used
Python
Streamlit (Frontend & UI)
PDF Processing
AI-based text analysis
GitHub for version control
🔹 Outcome
By the end of Week 3–4, the application evolved into a complete AI-powered learning assistant capable of:
Reading study material from PDFs
Generating quizzes and flashcards
Evaluating user performance with scores
