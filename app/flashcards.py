def generate_flashcards(text):
    flashcards = []

    sentences = text.split(".")
    for s in sentences[:5]:
        if len(s.strip()) > 20:
            flashcards.append({
                "question": "What does this mean?",
                "answer": s.strip()
            })

    return flashcards