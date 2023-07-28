from turtle import Turtle,Screen
import random

screen=Screen()
screen.bgcolor("black")
screen.setup(width=500,height=400)
bet=screen.textinput(title="enter you're bet",prompt="which color do you pick ?")
#set a screen with personal size .

colors='red green blue yellow gray black'.split()


x=-200
y=-100
turtles=[]
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x, y)
    y+=50
    turtles.append(new_turtle)

is_end=False
while  not is_end:

    for turtle in turtles:
        if turtle.xcor()>230:
            is_end=True
            winning_color=turtle.pencolor()

            if bet not in colors:
                print(f"you're pick color not even right.you LOST!!")
            elif winning_color==bet:
                print(f"you Win.{winning_color} wins and you pick {bet}")
            else:
                print(f"you Lost.{winning_color} wins and you pick {bet}")

        movement = random.randint(0, 10)
        turtle.forward(movement)



screen.exitonclick()





