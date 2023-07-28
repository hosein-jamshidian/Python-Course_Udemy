from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import Score



screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("blue")


snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


snake.initial_snake()

is_on=True
while is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()


    if snake.head.distance(food)< 20 :
        food.refresh_food()
        score.score_counter()
        snake.extend()


    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        snake.reset_snake()
        score.update_high_score()


    for component in snake.snake_list[1:]:
        if snake.head.distance(component) < 5:
            snake.reset_snake()
            score.update_high_score()


screen.exitonclick()
