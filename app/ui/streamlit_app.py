import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app import quiz_generator
from app import quiz_generator
import streamlit as st
from app.generator import generate_quiz, generate_audio_summary
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
    audio_file = generate_audio_summary(pdf_text)

    import os
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
    else:
        st.error("Audio file not created")
        
