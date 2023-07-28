from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))



