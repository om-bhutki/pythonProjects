from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="Some question text",
                                                font=("Arial", 20, "italic"),
                                                width=280
                                                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        img1 = PhotoImage(file="images/true.png")
        img2 = PhotoImage(file="images/false.png")
        self.right_btn = Button(image=img1, highlightthickness=0, command=self.right_pressed)
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn = Button(image=img2, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        quiz_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=quiz_text)
        self.canvas.config(bg="white")

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

