import streamlit as st
import PyPDF2

# -------------------------
# PDF TEXT EXTRACTION
# -------------------------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# -------------------------
# BASIC AI MCQ QUIZ (STATIC – WEEK 1–2)
# -------------------------
def generate_ai_mcq():
    return [
        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automated Information",
                "Advanced Internet",
                "Applied Informatics"
            ],
            "answer": "Artificial Intelligence"
        },
        {
            "question": "Which of the following is an application of AI?",
            "options": [
                "Voice Assistants",
                "Calculator",
                "Text Editor",
                "File Manager"
            ],
            "answer": "Voice Assistants"
        },
        {
            "question": "Which language is commonly used in AI development?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "SQL"
            ],
            "answer": "Python"
        }
    ]


# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="AI Quiz Generator", layout="centered")

st.title("📘 AI Quiz Generator (Week 1–2)")
st.write("Upload a PDF and generate basic AI quiz questions")

uploaded_file = st.file_uploader("📄 Upload PDF", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF uploaded successfully")

    if st.button("📝 Generate Quiz"):
        quiz = generate_ai_mcq()

        st.subheader("📚 AI Quiz (MCQ)")
        for i, q in enumerate(quiz, start=1):
            st.markdown(f"### Q{i}. {q['question']}")
            st.radio(
                "Select an answer:",
                q["options"],
                key=f"q{i}"
            )
            st.caption(f"✔ Correct Answer: {q['answer']}")
            st.divider()
import streamlit as st
import PyPDF2
import random
import re

# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# -----------------------------
# CREATE MCQ QUESTIONS FROM TEXT
# -----------------------------
def generate_mcq_from_text(text):
    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 40]

    if len(sentences) < 2:
        return []

    questions = []
    selected = random.sample(sentences, min(3, len(sentences)))

    for sent in selected:
        question = f"What does the following statement describe?\n\n{sent[:120]}..."
        options = [
            "Artificial Intelligence",
            "Machine Learning",
            "Data Science",
            "Computer Networks"
        ]
        answer = "Artificial Intelligence"

        questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    return questions


# -----------------------------
# CREATE FLASHCARDS FROM TEXT
# -----------------------------

def generate_flashcards(text):
    keywords = [
        "Artificial Intelligence",
        "Machine Learning",
        "Neural Network",
        "Deep Learning",
        "Natural Language Processing"
    ]

    flashcards = []

    for word in keywords:
        if word.lower() in text.lower():
            flashcards.append({
                "title": word,
                "content": f"{word} is a key concept in Artificial Intelligence used to build intelligent systemsAI (Artificial Intelligence) is the simulation of human intelligence by machines, designed to perform tasks like learning, reasoning, problem-solving, and decision-making. These systems use algorithms and data to mimic cognitive skills, improving efficiency in areas such as natural language processing, image recognition, and automation ."
            })

        return flashcards
# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="AI Quiz Generator", layout="centered")

st.title("🤖 AI Quiz & Flashcard Generator (Week 3–4)")
st.write("Upload an AI-related PDF to generate quizzes and flashcards")

uploaded_pdf= st.file_uploader("📄 Upload PDF", type=["pdf"], key="main_pdf_uploader")

if uploaded_pdf:
    text = extract_text_from_pdf(uploaded_pdf)
    st.success("✅ Document loaded successfully")

    # QUIZ SECTION
    st.subheader("📝 Quiz Generator")
    if st.button("Generate Quiz"):
        quiz = generate_mcq_from_text(text)

        if quiz:
            for i, q in enumerate(quiz, start=1):
                st.markdown(f"### Q{i}. {q['question']}")
                st.radio(
                    "Choose an option:",
                    q["options"],
                    key=f"quiz_{i}"
                )
                st.caption(f"✔ Correct Answer: {q['answer']}")
                st.divider()
        else:
            st.warning("Not enough content in PDF to generate quiz.")

    # FLASHCARD SECTION
    st.subheader("📚 Flashcards")
    if st.button("Generate Flashcards"):
        flashcards = generate_flashcards(text)

        for card in flashcards:
            with st.expander(card["title"]):
                st.write(card["content"])
    else:
        st.info("Click the button to generate flashcards based on key AI concepts found in the PDF.")