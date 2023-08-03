import pandas as pd
from turtle import Turtle, Screen

screen=Screen()
screen.title('U.S state game')
screen.bgpic('blank_states_img.gif')

# suggest= screen.textinput(title=f'{}/50 States Correct', prompt="what another state name:").title()

pointer=Turtle()
pointer.hideturtle()
pointer.penup()
pointer.color('black')

df=pd.read_csv('50_states.csv')

uncorrect_guess=0
Correct_answer=0
GAME_ON=True

while (Correct_answer<=50)and(GAME_ON):
    suggest = screen.textinput(title=f'{Correct_answer}/50 States Correct', prompt="what another state name:").title()
    if suggest in list(df['state']):
        Correct_answer+=1
        print(f'{suggest} is in my list.')
        x = int(df[df['state'] == f'{suggest}']['x'])
        y = int(df[df['state'] == f'{suggest}']['y'])
        pointer.goto(x, y)
        pointer.write(arg=f'{suggest}', align='center', font=('COURIER', 8, 'normal'))
    else:
        print(f'till here you have {uncorrect_guess} worng guess')
        uncorrect_guess+=1

    if uncorrect_guess ==3:
        GAME_ON=False


pointer.clear()
pointer.color('red')
pointer.goto(0,0)
pointer.write(arg=f'Total guesses: {Correct_answer+uncorrect_guess}\n\nWrong guesses: {uncorrect_guess}\n\nTrue guesses:{Correct_answer}', align='center', font=('TIME', 15, 'normal'))
screen.exitonclick()
