import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=315, y=random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
