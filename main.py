from turtle import Screen
from interface import Interface
from paddle import Paddle
from ball import Ball
import time
from random import randint


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PONG')

ball = Ball()
interface = Interface()
paddle = Paddle()
direction = randint(91, 269)
speed = .05

screen.listen()
screen.onkeypress(paddle.right_move_up, 'Up')
screen.onkeypress(paddle.right_move_down, 'Down')
screen.onkeypress(paddle.left_move_up, 'w')
screen.onkeypress(paddle.left_move_down, 's')

game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    if ball.pong.ycor() > 280 or ball.pong.ycor() < -280:
        direction -= 2 * direction
        speed *= 0.9

    if -345 < ball.pong.xcor() < -330:
        if 50 > ball.pong.ycor() - paddle.left_player_pad.ycor() > -50:
            direction = 180 - direction
            speed *= 0.9
    elif 345 > ball.pong.xcor() > 330:
        if 50 > ball.pong.ycor() - paddle.right_player_pad.ycor() > -50:
            direction = 180 - direction
            speed *= 0.9

    if ball.pong.distance(0, 0) > 500:
        if ball.pong.xcor() < -380:
            interface.update_score_ops()
        elif ball.pong.xcor() > 380:
            interface.update_score()
        ball.pong.teleport(0, 0)
        speed = 0.05
        direction = randint(91, 269)

    ball.move_ball(direction)

screen.exitonclick()
