from turtle import Turtle, Screen
from player import Player
from cars import Cars
from score import Score

import time

screen= Screen()
screen.title('turtle-crossing')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

my_turtle= Player()
cars=Cars()
score=Score()




screen.listen()
screen.onkey(my_turtle.move_up, 'w')

IS_ON=True
while IS_ON:
    screen.update()
    time.sleep(cars.speed)

    cars.create()
    cars.movement()

    if my_turtle.ycor()>270:
        score.level_up()
        my_turtle.reset_game()
        cars.speed_up()

    for car in cars.cars:
        if my_turtle.distance(car)<20:
            # print('Lose')
            # score.reset_score()
            score.reset()
            cars.reset_speed()
            my_turtle.reset_game()

screen.exitonclick()