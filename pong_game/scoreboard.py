from turtle import Turtle

ALIGN = "center"
FONT = ("Bahnschrift Light", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self,position_x,position_y):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(position_x, position_y)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
