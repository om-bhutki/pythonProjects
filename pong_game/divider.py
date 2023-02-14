from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 16, "normal")
COORDS = [260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0, -20, -40, -60, -80, -100, -120, -140,
          -160, -180, -200, -220, -240, -260]


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.create_divider()

    def create_divider(self):
        for position in COORDS:
            self.color("white")
            self.hideturtle()
            self.penup()
            self.goto(0, position)
            self.write("|", font=FONT, align=ALIGN)
