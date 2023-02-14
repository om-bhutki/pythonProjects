import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move)
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(scoreboard.move_speed)
    car_manager.generate_cars()
    car_manager.car_move()
    if player.ycor() == 280:
        scoreboard.level_up()
        player.goto(0, -280)
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


#
screen.exitonclick()
