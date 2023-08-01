from turtle import Turtle
import random

COLORS='blue red green yellow white pink purple brown gray'.split()

class Cars(Turtle):
    def __init__(self,):
        super().__init__()

        self.cars=[]
        self.speed=.1


    def create(self):
        choice=random.randint(1,6)
        if choice==1:
            car=Turtle('square')
            car.shapesize(stretch_len=2,stretch_wid=.8)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(310,random.randint(-250,250))
            self.cars.append(car)

    def movement(self):
        for car in self.cars:
            x_new= car.xcor()-20
            car.goto(x_new, car.ycor())

    def speed_up(self):
        self.speed*=.8
    def reset_speed(self):
        self.speed=.1