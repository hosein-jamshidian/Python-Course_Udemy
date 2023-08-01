from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.goto(0, -260)

    def move_up(self):
        self.forward(20)

    def reset_game(self):
        self.goto(0,-260)