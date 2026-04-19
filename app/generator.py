def generate_quiz(text):
    return 

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        )
        return prompt.format(text=te

Create 5 multiple choice questions (MCQs) based ONLY on the given text.

Rules:
- No generic questions
- Each question must be factual from the text
- Provide 4 options (A, B, C, D)
- Only one correct answer
-menction correct answer at the end of each question

Format:

Q1: Question
A) Option
B) Option
C) Option
D) Option
Answer: A

Text:
{text}
"""
    )

import random
from turtle import st

# -------------------------------
# QUIZ GENERATOR
# -------------------------------

def generate_quiz(text, level="Easy"):
    if not text or len(text.strip()) < 50:
        return []

    sentences = [
        s.strip()
        for s in text.replace("\n", " ").split(".")
        if len(s.strip()) > 40
    ]

    if level == "Easy":
        q_count = 3
    elif level == "Medium":
        q_count = 5
    else:
        q_count = 7

    selected = random.sample(sentences, min(q_count, len(sentences)))

    quiz = []

    for sent in selected:
        quiz.append({
            "question": f"\n\n{sent}",
            "options": [
                "Artificial Intelligence concept",
                "Computer Hardware topic",
                "Networking concept",
                "Operating System feature"
            ],
            "answer": "Artificial Intelligence concept"
        })

    return quiz


# -------------------------------
# FLASHCARD GENERATOR
# -------------------------------

def generate_flashcards(text):
    if not text or len(text.strip()) < 50:
        return []

    sentences = [
        s.strip()
        for s in text.replace("\n", " ").split(".")
        if len(s.strip()) > 40
    ]

    flashcards = []

    for sent in sentences[:5]:
        flashcards.append({
            "question": "Explain this concept:",
            "answer": sent
        })

    return flashcards

# -------------------------------
# AUDIO SUMMARY GENERATOR
# -------------------------------
from gtts import gTTS
import tempfile
import streamlit as st

def generate_audio_summary(text):
    try:
        if not text:
            return None

        summary = text[:200]

        tts = gTTS(text=summary, lang='en')

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        with open(temp_file.name, "rb") as f:
            audio_bytes = f.read()

        return audio_bytes

    except Exception as e:
        st.error(f"Audio Error: {e}")
        return None