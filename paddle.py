from turtle import Turtle


class Paddle:
    def __init__(self):
        self.orientation = 0
        self.paddles = []
        for i in range(2):
            paddle = Turtle('square')
            paddle.color('white')
            paddle.penup()
            paddle.setheading(90)
            paddle.shapesize(1, 5)
            self.paddles.append(paddle)
        self.left_player_pad = self.paddles[0]
        self.left_player_pad.teleport(-350, 0)
        self.right_player_pad = self.paddles[1]
        self.right_player_pad.teleport(350, 0)

    def left_move_up(self):
        if self.left_player_pad.ycor() < 250:
            self.left_player_pad.forward(20)

    def left_move_down(self):
        if self.left_player_pad.ycor() > -250:
            self.left_player_pad.backward(20)

    def right_move_up(self):
        if self.right_player_pad.ycor() < 250:
            self.right_player_pad.forward(20)

    def right_move_down(self):
        if self.right_player_pad.ycor() > -250:
            self.right_player_pad.backward(20)

    def auto_movement(self):
        if self.right_player_pad.ycor() == 280:
            self.orientation += 1
        elif self.right_player_pad.ycor() == -280:
            self.orientation -= 1
        if self.orientation == 0:
            self.right_player_pad.forward(20)
        elif self.orientation == 1:
            self.right_player_pad.backward(20)



