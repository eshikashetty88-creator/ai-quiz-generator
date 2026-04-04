def generate_quiz(text):
    return [
        {
            "question": f"What is the main idea of: {text[:50]}?",
            "options": {
                "A": "It describes a key concept from the text",
                "B": "It talks about an unrelated topic",
                "C": "It is a random statement",
                "D": "It is not mentioned in the text"
            },
            "answer": "A"
        },
        {
            "question": "What is the main purpose of the text?",
            "options": {
                "A": "To entertain",
                "B": "To inform about a concept",
                "C": "To confuse readers",
                "D": "To advertise something"
            },
            "answer": "B"
        },
        {
            "question": "Which of the following is a key point discussed?",
            "options": {
                "A": "A detail from the text",
                "B": "An unrelated idea",
                "C": "A fictional story",
                "D": "A random guess"
            },
            "answer": "A"
        },
        {
            "question": "Why is this concept important?",
            "options": {
                "A": "It has no importance",
                "B": "It helps understand the topic better",
                "C": "It is only for fun",
                "D": "It is unrelated"
            },
            "answer": "B"
        },
        {
            "question": "How can this be applied in real life?",
            "options": {
                "A": "It cannot be applied",
                "B": "It is only theoretical",
                "C": "It can be used in practical situations",
                "D": "It is useless"
            },
            "answer": "C"
        }
    ]
import random

# ---------------------------------
# QUIZ GENERATOR (PDF BASED)
# ---------------------------------

def generate_quiz(text, quiz_type="MCQ", level="Easy"):
    """
    Generates quiz questions from PDF text.
    Returns a LIST (never None).
    """

    if not text or len(text.strip()) < 50:
        return []

    sentences = [
        s.strip()
        for s in text.replace("\n", " ").split(".")
        if len(s.strip()) > 40
    ]

    if not sentences:
        return []

    # number of questions based on difficulty
    if level == "Easy":
        count = 3
    elif level == "Medium":
        count = 5
    else:
        count = 7

    selected = random.sample(sentences, min(count, len(sentences)))

    quiz = []

    for sent in selected:
        quiz.append({
            "question": f"What does the following statement describe?\n\n{sent}",
            "options": [
                "Artificial Intelligence concept",
                "Computer hardware process",
                "Networking protocol",
                "Operating system function"
            ],
            "answer": "Artificial Intelligence concept"
        })

    return quiz


# ---------------------------------
# FLASHCARD GENERATOR
# ---------------------------------

def generate_flashcards(text):
    """
    Generates flashcards from PDF text.
    Returns a LIST (never None).
    """
    if not text or len(text.strip()) < 50:
        return []

    keywords = ["Artificial Intelligence", "Machine Learning", "Neural Network", "Deep Learning"]
    flashcards = []

    for key in keywords:
        if key.lower() in text.lower():
            flashcards.append({
                "term": key,
                "definition": f"{key} is an important concept in AI used for intelligent systems."
            })

    if not flashcards:
        flashcards.append({
            "term": "Artificial Intelligence",
            "definition": "Artificial Intelligence enables machines to simulate human intelligence."
        })

    return flashcards