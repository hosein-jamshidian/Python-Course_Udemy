from turtle import Turtle
import pandas as pd

df=pd.read_csv('50_states.csv')

# TODO: csv file consist of states name and x,y coordinate in image.

class Pointer(Turtle):
    def __init__(self):
        super().__init__()

        self.wrong_guess_num=0
        self.correct_list=[]

        self.hideturtle()
        self.penup()
        self.color('black')

#TODO: create Pointer class for writing states name in image

    def apply_name(self,suggest):
        if suggest in list(df['state']) and (suggest not in self.correct_list):
            x = int(df[df['state'] == f'{suggest}']['x'])
            y = int(df[df['state'] == f'{suggest}']['y'])
            self.goto(x, y)
            self.write(arg=f'{suggest}', align='center', font=('COURIER', 8, 'normal'))
            self.correct_list.append(suggest)

        elif suggest in self.correct_list:
            self.wrong_guess_num += 1
            print(f'you say {suggest} one more time before. so pay attention because i have to get one more life and till now you have still {4-self.wrong_guess_num} more lifes!')

        else:
            self.wrong_guess_num+=1
            print(f'till now you said {self.wrong_guess_num} wrong guesses and have {4-self.wrong_guess_num} more lifes!')

#TODO: create function that check you're suggest and write it down on the image.

    def final_results(self):
        self.clear()
        self.color('red')
        self.goto(0, 0)
        self.write(arg=f'Wrong guesses: {self.wrong_guess_num}\n\nTrue guesses:{len(self.correct_list)}',align='center', font=('TIME', 15, 'normal'))

#TODO: last announcement that show total results.

    def residual_state(self):
        res= [state for state in list(df['state']) if state not in self.correct_list]
        res=pd.DataFrame(res,columns=['state'])
        res.to_csv('residual_states.csv')

#TODO: create csv file which have untelling states.