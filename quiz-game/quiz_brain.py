import html


class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list
        self.score = 0
        self.current_question = None
        self.user_answer: bool

    def start_quiz(self):
        return self.quiz_number < len(self.quiz_list)

    def next_question(self):
        try:
            self.current_question = self.quiz_list[self.quiz_number]
        except IndexError:
            return f"Your score: {self.score}/{self.quiz_number}"
        else:
            self.quiz_number += 1

        return f"Q.{self.quiz_number}: {html.unescape(self.current_question.text)}. (True/False)?"
        # real_ans = current_question.answer
        # if user_ans == real_ans:
        #     print("You got it right!")
        #     self.score += 1
        # else:
        #     print("You got it wrong!")
        # print(f"Your score: {self.score}/{self.quiz_number}")
        # print(f"Correct answer was: {real_ans}")

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


        # print(f"Your current score is: {self.score}/{self.quiz_number}")
        # print("\n")
