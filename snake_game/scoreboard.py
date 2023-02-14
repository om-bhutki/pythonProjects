from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(None)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=5)
        self.goto(0, 260)
        self.score = 0
        self.highscore = 0
        with open(file="highscore.txt", mode="r") as file:
            self.highscore = int(file.read())

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file="highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
