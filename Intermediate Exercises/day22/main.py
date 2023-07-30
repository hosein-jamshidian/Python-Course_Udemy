from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from screen_spliter import Spliter
import time


screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("gray")
screen.tracer(0)

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))


ball=Ball()

r_score=Score((100,260))
l_score=Score((-100,260))


spliter=Spliter()
spliter.create()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_on=True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.collision_wall()

    if ball.distance(r_paddle)<30 and ball.xcor()>340 or ball.distance(l_paddle)<30 and ball.xcor()<-340:
        ball.collision_paddle()

    if ball.xcor()>380:
        ball.start_position()
        l_score.scoring()
    if ball.xcor()<-380:
        ball.start_position()
        r_score.scoring()


screen.exitonclick()