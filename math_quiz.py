import random
import math

class MathQuiz:
    def __init__(self):
        self.score = 0

    def generate_question(self):
        operations = ['+', '-', '*', '/']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(operations)
        if operation == '/':
            correct_answer = math.floor(num1 / num2 * 100) / 100  # Trunchierea la primele două zecimale
            question = f"What is {num1} {operation} {num2}? (Maximum of the two MSD.)"
        else:
            correct_answer = eval(f"{num1} {operation} {num2}")
            question = f"What is {num1} {operation} {num2}?"
        return question, correct_answer

    def ask_question(self, question, correct_answer):
        while True:
            try:
                user_answer = float(input(question + " "))
                break
            except ValueError:
                print("Please enter a valid number.")

        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    def run_quiz(self, num_questions=5):
        # resetam scorul la inceputul fiecarui quiz, intruct se poate rula de mai multe ori pentru aceeasi instanta a clasei
        self.score = 0
        i = 0
        num_wrong_answers = 0
        max_wrong_answers = num_questions // 2 + 1

        if not 1 <= num_questions <= 10:
            raise ValueError("Number of questions must be between 1 and 10.")

        while i < num_questions:
            question, correct_answer = self.generate_question()
            self.ask_question(question, correct_answer)
            i += 1
            # Verificăm dacă jucătorul a răspuns suficient de multe întrebări greșit
            if self.score < (i - num_wrong_answers):
                num_wrong_answers += 1
                if num_wrong_answers >= max_wrong_answers:
                    print("Can't reach passing score anymore.")
                    break

        # Un `if-else` lanț pentru a oferi feedback bazat pe scorul final.
        if self.score >= num_questions / 2:
            print(f"Quiz completed! Your score: {self.score}/{num_questions} (Passed)")
        else:
            print(f"Quiz completed! Your score: {self.score}/{num_questions} (Failed)")

        if self.score > 0 and self.score < num_questions:
            print("Good job, but you can do better!")
        elif self.score == num_questions:
            print("Perfect score, well done!")


if __name__ == "__main__":
    # Example usage
    quiz = MathQuiz()
    quiz.run_quiz()
