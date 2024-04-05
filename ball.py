from turtle import Turtle
from random import randint
forbidden = (90, 180, 270,)


class Ball:
    def __init__(self):
        self.pong = Turtle('circle')
        self.pong.color('white')
        self.pong.penup()

    def move_ball(self, direction):
        self.pong.setheading(direction)
        self.pong.forward(10)




