from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

user_1 = QuizBrain(question_bank)

while user_1.still_has_questions():
    user_1.next_question()

print("You have completed the quiz")
print(f"Your final score was:{user_1.score} / {user_1.qeustion_number} ")