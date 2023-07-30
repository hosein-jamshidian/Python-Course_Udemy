from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
        self.move_speed=.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def collision_wall(self):
        self.y_move*=-1

    def collision_paddle(self):
        self.x_move*=-1
        self.move_speed*=.9

    def start_position(self):
        self.goto(0,0)
        self.move_speed=.1
        self.collision_paddle()



