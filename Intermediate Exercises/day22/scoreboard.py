from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(position)
        self.write(self.score,align='center',font=("COURIER", 30, "normal"))

    def scoring(self):
        self.clear()
        self.score+=1
        self.write(self.score, align='center', font=("COURIER", 30, "normal"))



