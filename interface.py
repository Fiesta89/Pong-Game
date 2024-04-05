from turtle import Turtle


class Interface:

    def __init__(self):
        self.point = 0
        self.opponent_point = 0
        self.line = Turtle()
        self.line.color('white')
        self.line.hideturtle()
        self.line.teleport(0, 400)
        self.line.setheading(270)
        for i in range(35):
            self.line.forward(10)
            self.line.penup()
            self.line.forward(10)
            self.line.pendown()
        self.score = Turtle()
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        self.score.teleport(50, 200)
        self.score.write(f'{self.opponent_point}', align='center', font=('Arial', 40, 'normal'))
        self.score.teleport(-50, 200)
        self.score.write(f'{self.point}', align='center', font=('Arial', 40, 'normal'))

    def update_score(self):
        self.point += 1
        self.score.clear()
        self.score.teleport(50, 200)
        self.score.write(f'{self.opponent_point}', align='center', font=('Arial', 40, 'normal'))
        self.score.teleport(-50, 200)
        self.score.write(f'{self.point}', align='center', font=('Arial', 40, 'normal'))

    def update_score_ops(self):
        self.opponent_point += 1
        self.score.clear()
        self.score.teleport(50, 200)
        self.score.write(f'{self.opponent_point}', align='center', font=('Arial', 40, 'normal'))
        self.score.teleport(-50, 200)
        self.score.write(f'{self.point}', align='center', font=('Arial', 40, 'normal'))

    def game_over(self):
        self.score.goto(0, 0)
        self.score.color('red')
        self.score.write('GAME OVER', align='center', font=('Arial', 24, 'bold'))