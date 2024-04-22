from unittest.mock import patch
from math_quiz import MathQuiz
import pytest

# Produce o intrebare si un raspuns valid
def test_generate_question():
    quiz = MathQuiz()
    question, answer = quiz.generate_question()
    assert "What is" in question
    assert isinstance(answer, (int, float))


# Se verifica daca numarul de intrebari este valid conform specificatiei (inrte 1 si 10)
def test_run_quiz_with_invalid_number_of_questions():
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.run_quiz(0)  # Valoare invalidă, mai mică decât 1
    assert "Number of questions must be between 1 and 10." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        quiz.run_quiz(11)  # Valoare invalidă, mai mare decât 10
    assert "Number of questions must be between 1 and 10." in str(excinfo.value)

@patch('builtins.print')
@patch('builtins.input', return_value='4')
def test_mocked_input_output(mock_input, mock_print):
    quiz = MathQuiz()
    quiz.ask_question("What is 2 + 2?", 4)
    mock_print.assert_called_with("Correct!")


# Test pentru verificarea unui răspuns corect
@patch('builtins.input', return_value='3')
@patch('builtins.print')
def test_ask_question_correct(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    mock_print.assert_called_with("Correct!")
    assert quiz.score == 1


# Test pentru verificarea unui răspuns incorect
@patch('builtins.input', return_value='4')
@patch('builtins.print')
def test_ask_question_incorrect(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    mock_print.assert_called_with("Wrong! The correct answer was 3.0.")
    assert quiz.score == 0


# Test pentru rularea completă a quiz-ului
@patch('builtins.input', side_effect=['5', '5', '5', '5', '5'])  # Simulăm răspunsuri corecte
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 3?", 5.0))  # Mock-uim generate_question pentru a returna întotdeauna răspunsul 5
def test_run_quiz(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 5  # Acum acest test ar trebui să treacă
    mock_print.assert_any_call("Quiz completed! Your score: 5/5 (Passed)")
    mock_print.assert_any_call("Perfect score, well done!")


# Verificarea oprirei premature a quiz-ului dacă nu mai pot atinge scorul de trecere
@patch('builtins.input', side_effect=['5', '5', '5', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_premature_stop(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 0
    mock_print.assert_any_call("Can't reach passing score anymore.")
    mock_print.assert_any_call("Quiz completed! Your score: 0/5 (Failed)")

def test_initial_score():
    quiz = MathQuiz()
    assert quiz.score == 0

def test_generate_question_structure():
    quiz = MathQuiz()
    question, answer = quiz.generate_question()
    assert isinstance(question, str)
    assert isinstance(answer, (int, float))

@patch('builtins.input', return_value='3')
def test_ask_question_increments_score(mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    assert quiz.score == 1

@patch('builtins.input', return_value='4')
def test_ask_question_does_not_increment_score(mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    assert quiz.score == 0

@patch('builtins.input', side_effect=['5', '5', '5', '5', '5'])
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 3?", 5.0))
def test_run_quiz_increments_score(mock_generate_question, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 5

@patch('builtins.input', side_effect=['5', '5', '5', '5', '5'])
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_does_not_increment_score(mock_generate_question, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 0

# Test mutant 1
@patch('builtins.input', side_effect=['5', '5', '4', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_partial_score(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 1
    mock_print.assert_any_call("Good job, but you can do better!")

# Test mutant 2
def test_generate_question():
    quiz = MathQuiz()

    # Division
    question, answer = quiz.generate_question(operation='/')
    operation_string = ' '.join(question.split()[2:5]).rstrip('?')
    assert answer == eval(operation_string)

    # Else
    question, answer = quiz.generate_question(operation='+')
    operation_string = ' '.join(question.split()[2:5]).rstrip('?')
    assert answer == eval(operation_string)
