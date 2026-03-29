import pytest

from quiz_generator import generate_quiz


def test_generate_quiz_default():
    text = "This is a test passage about AI quiz generation and template-based question construction."
    quiz = generate_quiz(text)

    assert isinstance(quiz, list)
    assert len(quiz) == 5

    first_question = quiz[0]
    assert "main idea" in first_question["question"]
    assert first_question["answer"] == "A"


def test_generate_quiz_zero_questions():
    assert generate_quiz("foo", num_questions=0) == []


def test_generate_quiz_invalid_text_type():
    with pytest.raises(TypeError):
        generate_quiz(123)
