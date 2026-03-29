import streamlit as st
from app.quiz_generator import generate_quiz

st.title("AI Quiz Generator")

text = st.text_area("Enter study text")

if st.button("Generate Quiz"):
    quiz = generate_quiz(text)
    for q in quiz:
        st.write(q)