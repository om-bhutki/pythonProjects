from turtle import Turtle

SNAKE_CORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts_list = []
        self.create_snake()
        self.head = self.snake_parts_list[0]

    def create_snake(self):
        for snake in SNAKE_CORDS:
            self.add_snake_parts(snake)

    def add_snake_parts(self,position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_parts_list.append(snake_body)

    def reset(self):
        for parts in self.snake_parts_list:
            parts.goto(1000,1000)

        self.snake_parts_list.clear()
        self.create_snake()
        self.head = self.snake_parts_list[0]

    def extend(self):
        self.add_snake_parts(self.snake_parts_list[-1].position())

    def move(self):
        for snake_parts in range(len(self.snake_parts_list) - 1, 0, -1):
            new_x = self.snake_parts_list[snake_parts - 1].xcor()
            new_y = self.snake_parts_list[snake_parts - 1].ycor()
            self.snake_parts_list[snake_parts].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

