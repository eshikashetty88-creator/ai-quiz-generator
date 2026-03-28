# AI Educational Content Generator

## Overview
This project builds an AI-powered tutor that generates:
- Quizzes
- Flashcards
- Audio summaries

from educational content like text and PDFs.

## Track
Track A – Essential
# 📘 AI Quiz Generator

## 📌 Project Description
This project is an AI-powered quiz generator that converts study material into questions automatically. It helps students learn faster using interactive quizzes and smart content generation.

## Week 1 Goal
- Input text
- Generate quiz automatically
## ▶️ How to Run the Project

Follow these steps to run the AI Quiz Generator:

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
streamlit run app.py
```

### 4️⃣ Open in Browser
After running, open:
http://localhost:8501

---

## Features (Planned)
- Quiz generation
- Flashcards
- Audio summaries (TTS)
- Study progress tracking

## Tech Stack
- Python
- Streamlit
- LangChain (later)
- SQLite

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
            question = s.replace(blank_word, "_____")
            questions.append((question, blank_word))

    return questions
```
## 📤 Output Example

Input:
Python is a programming language. It is easy to learn.

Output:
Q1: Python is a _____ language  
Q2: It is easy to _____
## Status
🚧 Week 1 – Building basic quiz generator

