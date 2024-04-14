from unittest.mock import patch
from math_quiz import MathQuiz

def test_generate_question():
    quiz = MathQuiz()
    question, answer = quiz.generate_question()
    assert "What is" in question
    assert isinstance(answer, (int, float))

def test_ask_question_correct():
    quiz = MathQuiz()
    result = quiz.ask_question("What is 1 + 2?", 3.0)
    assert result == True
    assert quiz.score == 1

def test_ask_question_incorrect():
    quiz = MathQuiz()
    result = quiz.ask_question("What is 1 + 2?", 3.0)
    assert result == False
    assert quiz.score == 0

@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 3?", 5.0))
def test_run_quiz(mock_generate_question):
    quiz = MathQuiz()
    for _ in range(5):
        result = quiz.ask_question("What is 2 + 3?", 5.0)
        assert result == True
    assert quiz.score == 5

@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_premature_stop(mock_generate_question):
    quiz = MathQuiz()
    for _ in range(5):
        result = quiz.ask_question("What is 2 + 2?", 5.0)
        assert result == False
    assert quiz.score == 0

def test_initial_score():
    quiz = MathQuiz()
    assert quiz.score == 0

def test_generate_question_structure():
    quiz = MathQuiz()
    question, answer = quiz.generate_question()
    assert isinstance(question, str)
    assert isinstance(answer, (int, float))

def test_ask_question_increments_score():
    quiz = MathQuiz()
    result = quiz.ask_question("What is 1 + 2?", 3.0)
    assert result == True
    assert quiz.score == 1

def test_ask_question_does_not_increment_score():
    quiz = MathQuiz()
    result = quiz.ask_question("What is 1 + 2?", 4.0)
    assert result == False
    assert quiz.score == 0

@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 3?", 5.0))
def test_run_quiz_increments_score(mock_generate_question):
    quiz = MathQuiz()
    for _ in range(5):
        result = quiz.ask_question("What is 2 + 3?", 5.0)
        assert result == True
    assert quiz.score == 5

@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_does_not_increment_score(mock_generate_question):
    quiz = MathQuiz()
    for _ in range(5):
        result = quiz.ask_question("What is 2 + 2?", 5.0)
        assert result == False
    assert quiz.score == 0