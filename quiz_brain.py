class QuizBrain:

    def __init__(self, qeustions_list):
        self.qeustions_list = qeustions_list
        self.qeustion_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.qeustion_number < len(self.qeustions_list)

    def next_question(self):
        user_answer = input(
            f"Q.{self.qeustion_number + 1}: {self.qeustions_list[self.qeustion_number].q_text}. (True/False)?: ")
        self.qeustion_number += 1
        correct_answer = self.qeustions_list[self.qeustion_number].q_answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f" You current score is: {self.score} / {self.qeustion_number}")
        print("\n")