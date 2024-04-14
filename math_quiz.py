import random


class MathQuiz:
    def __init__(self):
        self.score = 0

    def generate_question(self):
        operations = ['+', '-', '*', '/']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(operations)
        question = f"What is {num1} {operation} {num2}?"
        correct_answer = eval(f"{num1} {operation} {num2}")
        return question, correct_answer

    def ask_question(self, question, correct_answer):
        answer = float(input(question))
        if answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

    def run_quiz(self, num_questions=5):
        i = 0
        max_score = num_questions
        while i < num_questions and self.score + (num_questions - i) >= max_score / 2:
            question, correct_answer = self.generate_question()
            self.ask_question(question, correct_answer)
            i += 1
            if self.score < i / 2:  # O altă condiție: dacă scorul curent este sub jumătatea întrebărilor puse
                print("Can't reach passing score anymore.")
                break

        # Un `if-else` lanț pentru a oferi feedback bazat pe scorul final.
        if self.score >= num_questions / 2:
            print(f"Quiz completed! Your score: {self.score}/{num_questions} (Passed)")
        else:
            print(f"Quiz completed! Your score: {self.score}/{num_questions} (Failed)")

        # If cu două condiții.
        if self.score > 0 and self.score < num_questions:
            print("Good job, but you can do better!")
        elif self.score == num_questions:
            print("Perfect score, well done!")


if __name__ == "__main__":
    # Example usage
    quiz = MathQuiz()
    quiz.run_quiz()
