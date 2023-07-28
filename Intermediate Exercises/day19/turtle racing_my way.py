from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(600,400)

COLORES = 'red blue green purple black brown'.split()

def make_choice():
    user_choice = screen.textinput(title="make you're bet", prompt='which color do you pick? '.lower())
    if user_choice not in COLORES:
        print(f"You're Choice Not In Turtle Colores.\n{tuple(COLORES)}")
        user_choice = screen.textinput(title='ERROR', prompt=f'Choose One Of These Colores: {tuple(COLORES)}')
    return user_choice

def make_turtle():
    TURTLES = []
    i = -230
    for t in range(6):
        hosein=Turtle(shape='turtle')
        hosein.penup()
        hosein.color(COLORES[t])
        i+=65
        hosein.goto(-280,i)
        TURTLES.append(hosein)
    return TURTLES

def check_winner(turtle):
    if user_choice == turtle.color():
        print(f'GAME DONE.\nYou Bet On {user_choice} Turtle And You Win !CONGRATUATION! ')
        GAME_ON = False
    else:
        print(f"GAME DONE.\nYou Bet On '{user_choice}' But '{turtle.pencolor()}' Win This Game!")
        GAME_ON = False
    return GAME_ON

user_choice=make_choice()
TURTLES=make_turtle()

GAME_ON=True
while GAME_ON:
        if user_choice not in COLORES:
            print('Please Try Correct Color')
            GAME_ON=False

        else:
            for t in TURTLES:
                if t.xcor()>260:
                    GAME_ON=check_winner(t)
                else:
                    number = random.randint(0, 5)
                    TURTLES[number].forward(10)

screen.exitonclick()
