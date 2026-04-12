import streamlit as st
from app.quiz_generator import generate_quiz

st.title("AI Quiz Generator")

text = st.text_area("Enter study text")

if st.button("Generate Quiz"):
    quiz = generate_quiz(text)
    for q in quiz:
        st.write(q)
        from gtts import gTTS
import tempfile
from app.generator import generate_audio_summary
def generate_audio_summary(text):
    summary = text[:800]
    tts = gTTS(summary)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name