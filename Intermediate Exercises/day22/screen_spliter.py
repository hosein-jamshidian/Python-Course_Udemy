from turtle import Turtle
class Spliter:
    def __init__(self):
        self.list=[]
        self.y=-270

    def create(self):
        while self.y<300:
            line=Turtle()
            line.color("white")
            line.shape("square")
            line.shapesize(1, .1)
            line.penup()
            line.goto(x=0,y=self.y)
            self.list.append(line)
            self.y+=40



