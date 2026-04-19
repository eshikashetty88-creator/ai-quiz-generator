from pydoc import text
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app import quiz_generator
from app import quiz_generator
import streamlit as st
from app.generator import generate_flashcards, generate_quiz, generate_audio_summary
from app.document_loader import load_pdf

st.title("AI Quiz Generator")

uploaded_file = st.file_uploader("Upload PDF")

pdf_text = ""

if uploaded_file is not None:
    st.success("PDF uploaded successfully")
    pdf_text = load_pdf(uploaded_file)

# 👉 GENERATE QUIZ
if st.button("Generate Quiz"):
    if pdf_text:
        quiz = generate_quiz(pdf_text)
        st.write(quiz)  # SHOW OUTPUT
    else:
        st.warning("Please upload a file or enter text")

# 👉 AUDIO SUMMARY
if st.button("Generate Audio Summary"):
    audio = generate_audio_summary(pdf_text)

    if audio:
        st.audio(audio, format="audio/mp3")
    else:
        st.error("Audio not generated")
        if st.button("Test Audio"):
            audio = generate_audio_summary("Hello this is a test audio")

    if audio:
        st.audio(audio, format="audio/mp3")
   
# 👉 GENERATE FLASHCARDS
if st.button("Generate Flashcards"):
    if pdf_text:
        flashcards = generate_flashcards(pdf_text)
        st.write(flashcards)
    else:
        st.warning("Please upload a file or enter text")