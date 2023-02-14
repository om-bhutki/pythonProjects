from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for keys in question_data:
    question_bank.append(Question(keys["question"], keys["correct_answer"]))

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
while quiz.start_quiz():
    quiz.next_question()
print("Game ended.")
print(f"Total score: {quiz.score}/{quiz.quiz_number}")

