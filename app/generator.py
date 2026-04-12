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
            "question": f"What does the following statement explain?\n\n{sent}",
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
import tempfile
from gtts import gTTS
import os
def generate_audio_summary(summary_text):
    tts = gTTS(summary_text)
    audio_file = "summary.mp3"
    tts.save(audio_file)
    return audio_file