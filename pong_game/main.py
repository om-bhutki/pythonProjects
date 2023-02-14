import time
from turtle import Screen

from divider import Divider
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#divider = Divider()

l_paddle = Paddle(-380)
r_paddle = Paddle(380)

scoreboard_l = Scoreboard(-40, 220)
scoreboard_r = Scoreboard(40, 220)

ball = Ball()
screen.listen()
screen.onkey(key="Up", fun=l_paddle.move_up)
screen.onkey(key="Down", fun=l_paddle.move_down)
screen.onkey(key="w", fun=r_paddle.move_up)
screen.onkey(key="s", fun=r_paddle.move_down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        scoreboard_l.increase_score()
        ball.restart()
    if ball.xcor() < -400:
        scoreboard_r.increase_score()
        ball.restart()

    # if scoreboard_r.score == 5 or scoreboard_l.score == 5:
    #     is_game_on = False

screen.exitonclick()
