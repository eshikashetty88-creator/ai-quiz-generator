import streamlit as st
from app.quiz_generator import generate_quiz

st.title("AI Quiz Generator")

text = st.text_area("Enter study text")

if st.button("Generate Quiz"):
    quiz = generate_quiz(text)
    for q in quiz:
        st.write(q)
        from gtts import gTTS
from app.generator import generate_audio_summary
from app.document_loader import load_pdf

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    pdf_text = load_pdf(uploaded_file)
    st.success("PDF uploaded successfully")

    if st.button("🔊 Generate Audio Summary"):
        audio_file = generate_audio_summary(pdf_text)
        st.audio(audio_file)