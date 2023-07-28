from turtle import Turtle

INITIAL_POSITION=[(-40,0),(-20,0),(0,0)]


class Snake():
    def __init__(self):
        self.snake_list=[]
        self.initial_snake()
        self.head=self.snake_list[0]
        self.move_speed=.1


    def create_snake(self,position):
        turtle=Turtle(shape="square")
        turtle.penup()
        turtle.color("yellow")
        turtle.goto(position)
        self.snake_list.append(turtle)

    def initial_snake(self):
        for position in INITIAL_POSITION:
            self.create_snake(position)

    def extend(self):
        self.create_snake(self.snake_list[-1].position())
        self.move_speed*=.8


    def reset_snake(self):
        for snake in self.snake_list:
            snake.goto(1000,1000)
        self.snake_list.clear()
        self.initial_snake()
        self.head = self.snake_list[0]
        self.move_speed=.1

    def move(self):
        for index in range(len(self.snake_list)-1,0,-1):
            position=self.snake_list[index- 1].position()
            self.snake_list[index].goto(position)
        self.snake_list[0].forward(10)


    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
             self.head.setheading(0)



