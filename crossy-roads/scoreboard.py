from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.shapesize(stretch_wid=5, stretch_len=5)
        self.move_speed = 0.1
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.move_speed *= 0.7
        self.level += 1
        self.clear()
        self.update_level()
