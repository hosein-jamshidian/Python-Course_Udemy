from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score=1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-230,250)
        self.write(arg=f"LEVEL: {self.score}", align= 'center', font=('COURIER', 20, 'normal'))

    def level_up(self):
        self.clear()
        self.score+=1
        self.write(arg=f"LEVEL: {self.score}", align= 'center', font=('COURIER', 20, 'normal'))

    def reset_score(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game Over\nYou Reach level {self.score}👌", align='center', font=('COURIER', 20, 'normal'))
        self.score = 1