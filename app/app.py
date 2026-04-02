import streamlit as st

st.title("📘 MCQ Quiz Generator")

topic = st.text_input("Enter a topic:")

# Store quiz in session
if "quiz" not in st.session_state:
    st.session_state.quiz = None
    st.session_state.submitted = False

def generate_mcq(topic):
    return [
        {
            "question": f"What is {topic}?",
            "options": ["Concept", "Process", "Device", "None"],
            "answer": "Concept"
        },
        {
            "question": f"Why is {topic} important?",
            "options": ["Useful", "Not useful", "Harmful", "None"],
            "answer": "Useful"
        },
        {
            "question": f"Where is {topic} used?",
            "options": ["Education", "Industry", "Research", "All of the above"],
            "answer": "All of the above"
        },
        {
            "question": f"How does {topic} work?",
            "options": ["Step-by-step", "Randomly", "Not applicable", "None"],
            "answer": "Step-by-step"
        },
        {
            "question": f"what is the primary function of photosynyhesis?",
            "options":["break down glucose","produce oxygen","convert light energy to chemical energy","absorb minerals"],
            "answer":"convert light energy to chemical energy"
        },
        {
            "question": f"which pigment is responsible for the green color in plants?",
            "options":["chlorophyll","carotenoids","anthocyanins","xanthophyll"],
            "answer":"chlorophyll"
        },
        {
            "question": f"what are the main products of photosynthesis?",
            "options":["glucose and oxygen","carbon dioxide and water","glucose and carbon dioxide","oxygen and water"],
            "answer":"glucose and oxygen"
        },
        {
            "question": f"where does photosynthesis primarily occur in plant cells?",
            "options":["mitochondria","chloroplasts","nucleus","ribosomes"],
            "answer":"chloroplasts"
        },
        
        {
            "question": f"what is the role of sunlight in photosynthesis?",
            "options":["provides energy","breaks down glucose","absorbs water","produces carbon dioxide"],
            "answer":"provides energy"
        },
        {
            "question": f"what is the significance of photosynthesis for life on Earth?",
            "options":["produces food","produces oxygen","regulates climate","all of the above"],
            "answer":"all of the above"
        },
    ]

# Generate quiz only once
if st.button("Generate Quiz"):
    if topic:
        st.session_state.quiz = generate_mcq(topic)
        st.session_state.submitted = False
    else:
        st.warning("Enter a topic")

# Show quiz
if st.session_state.quiz:
    user_answers = []

    for i, q in enumerate(st.session_state.quiz):
        st.write(f"Q{i+1}: {q['question']}")
        choice = st.radio(
            f"Select answer for Q{i+1}",
            q["options"],
            key=f"q{i}"
        )
        user_answers.append(choice)

    if st.button("Submit Answers"):
        score = 0
        for i, q in enumerate(st.session_state.quiz):
            if user_answers[i] == q["answer"]:
                score += 1

        st.success(f"✅ Your Score: {score}/{len(st.session_state.quiz)}")