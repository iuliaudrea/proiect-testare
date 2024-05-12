from unittest.mock import patch
from math_quiz import MathQuiz
import pytest

### Teste pentru metoda run_quiz

# Se verifica daca numarul de intrebari este valid conform specificatiei (inrte 1 si 10)
def test_run_quiz_with_invalid_number_of_questions():
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.run_quiz(0)  # Valoare invalidă, mai mică decât 1
    assert "Number of questions must be between 1 and 10." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        quiz.run_quiz(11)  # Valoare invalidă, mai mare decât 10
    assert "Number of questions must be between 1 and 10." in str(excinfo.value)

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

# Verificarea trecerii testului cu scor mai mic decat maximul
@patch('builtins.input', side_effect=['4', '4', '4', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_premature_stop(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 3
    mock_print.assert_any_call("Good job, but you can do better!")
    mock_print.assert_any_call("Quiz completed! Your score: 3/5 (Passed)")

# Verificarea opririi premature a quiz-ului dacă nu mai pot atinge pragul de trecere
@patch('builtins.input', side_effect=['5', '5', '5', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_premature_stop(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 0
    mock_print.assert_any_call("Can't reach passing score anymore.")
    mock_print.assert_any_call("Quiz completed! Your score: 0/5 (Failed)")


### Teste pentru metoda ask_question

# Test pentru verificarea unui raspuns corect
@patch('builtins.input', return_value='3')
@patch('builtins.print')
def test_ask_question_correct(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    mock_print.assert_called_with("Correct!")
    assert quiz.score == 1


# Test pentru verificarea unui raspuns incorect
@patch('builtins.input', return_value='4')
@patch('builtins.print')
def test_ask_question_incorrect(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.0)
    mock_print.assert_called_with("Wrong! The correct answer was 3.0.")
    assert quiz.score == 0

# Test pentru raspuns invalid
def test_ask_question_user_invalid_response():
    quiz = MathQuiz()
    with patch('builtins.input', side_effect=['abc', '3.14']), patch('builtins.print') as mock_print:
        quiz.ask_question("What is π to two decimal places?", 3.14)
        mock_print.assert_any_call("Please enter a valid number.")
        assert mock_print.call_args_list[-1][0][0] == "Correct!"
        assert quiz.score == 1

# Test pentru parametru parametru invalid (non-numeric)
def test_ask_question_invalid_correct_answer():
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.ask_question("How many continents are there?", 'seven')
    assert "Expected a number for correct_answer" in str(excinfo.value)

# Test pentru parametru cu mai multe zecimale
def test_ask_question_correct_answer_with_more_than_two_decimals():
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.ask_question("Test question for validation:", 3.14159)
    assert "must not have more than two decimal places" in str(excinfo.value)


##### Teste pentru metoda generate_question

# Test pentru a verifica ca se genereaza o intrebare valdia
# @pytest.mark.parametrize("operation", ['+', '-', '*', '/'])
# def test_generate_question_with_valid_operation(operation):
#     quiz = MathQuiz()
#     question, answer = quiz.generate_question(operation)
#     assert question.startswith('What is ')
#     assert operation in question
#     if operation == '/':
#         assert question.endswith('(Maximum of the two MSD.)')  # verificare sufix impartire
#     assert isinstance(answer, float) if operation == '/' else isinstance(answer, int)

# # Test pentru a verifica comportamentul implicit
# def test_generate_question_with_no_operation():
#     quiz = MathQuiz()
#     question, answer = quiz.generate_question()
#     assert any(op in question for op in ['+', '-', '*', '/'])

# # Test pentru o operatie invalida
# def test_generate_question_with_invalid_operation():
#     quiz = MathQuiz()
#     with pytest.raises(ValueError):
#         quiz.generate_question(operation='invalid_operation')

# # Test pentru a verifica comportamentul funcției pentru toate operațiile valide
# # și confirmă că răspunsurile sunt calculate și trunchiate corect
# def test_generate_question_results():
#     quiz = MathQuiz()
#     for operation in ['+', '-', '*', '/']:
#         _, answer = quiz.generate_question(operation)
#         # Verificăm dacă răspunsul este un număr și că este corect calculat pentru operația dată
#         assert isinstance(answer, (int, float)), "Răspunsul trebuie să fie un număr."
#         # Pentru împărțire, verificăm trunchierea la două zecimale
#         if operation == '/':
#             assert round(answer, 2) == answer, "Răspunsul împărțirii nu este corect trunchiat."


@patch('builtins.input', side_effect=['0.666'])
@patch('builtins.print')
def test_division_high_precision(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 6 / 9? (Maximum of the two MSD.)", 0.66)
    mock_print.assert_called_with("Correct!")

@patch('builtins.input', side_effect=['0.67'])
@patch('builtins.print')
def test_division_wrong_precision(mock_print, mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 6 / 9? (Maximum of the two MSD.)", 0.66)
    mock_print.assert_called_with("Wrong! The correct answer was 0.66.")

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

# # Test mutant 1
# max_wrong_answers = num_questions // 2 + 2
@patch('builtins.input', side_effect=['4', '4', '5', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_early_quit(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 2
    mock_print.assert_any_call("Can't reach passing score anymore.")
    mock_print.assert_any_call("Quiz completed! Your score: 2/5 (Failed)")

# Test mutant 2
# if self.score >= num_questions / 3:
@patch('builtins.input', side_effect=['4', '4', '4', '5', '5'])
@patch('builtins.print')
@patch.object(MathQuiz, 'generate_question', return_value=("What is 2 + 2?", 4.0))
def test_run_quiz_final_answer(mock_generate_question, mock_print, mock_input):
    quiz = MathQuiz()
    quiz.run_quiz(5)
    assert quiz.score == 3
    mock_print.assert_any_call("Quiz completed! Your score: 3/5 (Passed)")

############# Teste Structurale #############

# correct_answer = 'trei' si user_input nu este relevant
def test_ask_question_with_string_correct_answer():
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.ask_question("What is 1 + 2?", 'trei')
    assert "Expected a number for correct_answer" in str(excinfo.value)


# correct_answer = 5 și user_input = 5
@patch('builtins.input', return_value='5')
def test_ask_question_with_integer_answers(mock_input):
    quiz = MathQuiz()
    try:
        quiz.ask_question("What is 2 + 3?", 5)
    except ValueError:
        pytest.fail("Unexpected ValueError raised")  # Testul va esua daca se arunca o exceptie
    assert quiz.score == 1


# correct_answer = 3.2 si user_input = 'trei'
def test_ask_question_with_float_correct_answer_and_string_input():
    quiz = MathQuiz()
    with patch('builtins.input', side_effect=['trei', '3.2']), patch('builtins.print') as mock_print:
        quiz.ask_question("What is 1 + 2?", 3.2)
        mock_print.assert_any_call("Please enter a valid number.")
        assert mock_print.call_args_list[-1][0][0] == "Correct!"
        assert quiz.score == 1
        

# correct_answer = 3.222 si user_input = 3.2
@patch('builtins.input', return_value='3.2')
def test_ask_question_with_float_answers(mock_input):
    quiz = MathQuiz()
    with pytest.raises(ValueError) as excinfo:
        quiz.ask_question("What is 1 + 2?", 3.222)
    assert "correct_answer as a float must not have more than two decimal places" in str(excinfo.value)
    assert quiz.score == 0  # scorul nu ar trebui să creasca ptr ca rsspunsul corect nu a fost dat


# correct_answer = 3.2 si user_input = 7.2
@patch('builtins.input', return_value='7.2')
def test_ask_question_with_different_float_inputs(mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.2)
    assert quiz.score == 0


# correct_answer = 3.2 si user_input = 3.2
@patch('builtins.input', return_value='3.2')
def test_ask_question_with_equal_float_inputs(mock_input):
    quiz = MathQuiz()
    quiz.ask_question("What is 1 + 2?", 3.2)
    assert quiz.score == 1


# correct_answer = -2 si user_input = x2
def test_ask_question_with_negative_integer_and_string_input():
    quiz = MathQuiz()
    with patch('builtins.input', side_effect=['x2', '-2']), patch('builtins.print') as mock_print:
        quiz.ask_question("What is 2 - 4?", -2)
        mock_print.assert_any_call("Please enter a valid number.")
        assert mock_print.call_args_list[-1][0][0] == "Correct!"
        assert quiz.score == 1


# # correct_answer = -3 si user_input = -3.222
# def test_ask_question_with_negative_float_answers_and_input():
#     quiz = MathQuiz()
#     with patch('builtins.input', return_value = '-3.222'):
#         quiz.ask_question("What is 2 - 5?", -3)
#         assert quiz.score == 0
