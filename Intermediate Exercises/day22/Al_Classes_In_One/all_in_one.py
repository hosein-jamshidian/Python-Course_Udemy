from turtle import Turtle, Screen
import time
import random

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        if self.ycor()<240 :
            self.goto(self.xcor(),self.ycor()+20)
    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(),self.ycor()-20)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_move=10
        self.y_move=10
        self.sleep_time=.08

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    def hit_wall(self):
        self.y_move*=-1
    def hit_paddle(self):
        self.x_move*=-1
        self.sleep_time-=.01
    def refresh(self):
        self.goto(0,0)
        self.hit_paddle()
        self.sleep_time=.08

class Reward(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score=0
        self.p2_score=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(arg=f'P1 score : {self.p1_score}', align='center', font=('Arial', 24, 'normal'))
        self.goto(250, 250)
        self.write(arg=f'P2 score : {self.p2_score}', align='center', font=('Arial', 24, 'normal'))


    def p1_scoring(self):
        self.p1_score+=1
        self.update_score()
    def p2_scoring(self):
        self.p2_score += 1
        self.update_score()

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)


p1=Paddle((-350,0))
p2=Paddle((350,0))
ball=Ball()
score=Reward()

screen.listen()
screen.onkey(key='w',fun=p1.go_up)
screen.onkey(key='s',fun=p1.go_down)
screen.onkey(key='Up',fun=p2.go_up)
screen.onkey(key='Down',fun=p2.go_down)

SLEEP_TIME=.1

ON=True
while ON:
    screen.update()
    time.sleep(ball.sleep_time)
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.hit_wall()
    if ball.distance(p2)<50 and ball.xcor() >320 or ball.distance(p1)<50 and ball.xcor()<-320:
        ball.hit_paddle()
    if ball.xcor()>380:
        score.p1_scoring()
        ball.refresh()
    if ball.xcor()<-380 :
        score.p2_scoring()
        ball.refresh()

screen.exitonclick()