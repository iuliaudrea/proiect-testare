import pytest
import math
from math_quiz import MathQuiz  # Assuming your original code is in math_quiz.py

def test_invalid_operation():
  quiz = MathQuiz()
  with pytest.raises(ValueError) as excinfo:
    quiz.generate_question(operation="invalid")
  assert "Invalid operation 'invalid'" in str(excinfo.value)

def test_division_by_zero(mocker):
  # Mock random.randint to always return 0 for denominator
  mocker.patch('random.randint', side_effect=[1, 0])
  quiz = MathQuiz()
  with pytest.raises(ZeroDivisionError):
    quiz.generate_question(operation="/")

def test_float_answer_rounding():
  quiz = MathQuiz()
  question, answer = quiz.generate_question(operation="/")
  assert answer == math.floor(answer * 100) / 100

def test_float_answer_validation():
  quiz = MathQuiz()
  with pytest.raises(ValueError) as excinfo:
    quiz.ask_question("dummy question", 3.14159)
  assert "correct_answer as a float must not have more than two decimal places." in str(excinfo.value)

def test_invalid_user_input():
  quiz = MathQuiz()
  question = "What is 1 + 1?"
  answer = quiz.ask_question(question, 2)
  assert answer is None  # No answer should be accepted for invalid input

def test_run_quiz_default():
  quiz = MathQuiz()
  quiz.run_quiz()
  # Assert score and output messages based on quiz results

def test_run_quiz_custom_questions():
  quiz = MathQuiz()
  quiz.run_quiz(num_questions=8)
  # Assert score and output messages for 8 questions

def test_pass_quiz():
  quiz = MathQuiz()
  # Simulate correct answers for all questions (use mocker or other techniques)
  quiz.run_quiz()
  assert quiz.score == 5  # Assuming default number of questions is 5

def test_fail_quiz():
  quiz = MathQuiz()
  # Simulate wrong answers for most questions (use mocker or other techniques)
  quiz.run_quiz()
  assert quiz.score < 3  # Assuming failing score is less than half the questions
