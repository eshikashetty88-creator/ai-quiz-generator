# AI Educational Content Generator

## Overview
This project builds an AI-powered tutor that generates:
- Quizzes
- Flashcards
- Audio summaries

from educational content like text and PDFs.

## Track
Track A – Essential

## Week 1 Goal
- Input text
- Generate quiz automatically

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
## status
week1 - setup & basic quiz generator

## Team
- ESHIKA
- JEEVITHA
- CHANDAN
## Status
🚧 Week 1 – Building basic quiz generator
import streamlit as st
from quiz_generator import generate_quiz

st.title("ai quiz generator")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

text = st.text_area("enter study text")

if st.button("Generate Quiz"):
    if text:
        quiz = generate_quiz(text)
        st.subheader("Generated Quiz")
        for q in quiz:
            st.write(q)
    else:
        st.warning("Please enter some text to generate a quiz.")
