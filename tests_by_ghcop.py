import unittest
from math_quiz import MathQuiz

class TestMathQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = MathQuiz()

    # Structural tests
    def test_initial_score(self):
        self.assertEqual(self.quiz.score, 0)

    def test_generate_question(self):
        question, answer = self.quiz.generate_question()
        self.assertIsInstance(question, str)
        self.assertIn(question.split()[1], ['+', '-', '*', '/'])
        self.assertIsInstance(answer, (int, float))

    def test_generate_question_with_operation(self):
        question, answer = self.quiz.generate_question('+')
        self.assertIn('+', question)

    def test_generate_question_with_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.quiz.generate_question('x')

    # Functional tests
    def test_run_quiz(self):
        with unittest.mock.patch('builtins.input', return_value='5'):
            self.quiz.run_quiz(1)
            self.assertEqual(self.quiz.score, 1)

    def test_run_quiz_with_wrong_answer(self):
        with unittest.mock.patch('builtins.input', return_value='0'):
            self.quiz.run_quiz(1)
            self.assertEqual(self.quiz.score, 0)

    def test_run_quiz_with_invalid_num_questions(self):
        with self.assertRaises(ValueError):
            self.quiz.run_quiz(0)
        with self.assertRaises(ValueError):
            self.quiz.run_quiz(11)

if __name__ == '__main__':
    unittest.main()