from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score=1
        self.color('white')
        with open('records.txt') as file:
            self.high_score=int(file.readline())
        self.penup()
        self.hideturtle()
        self.goto(-90,250)
        self.write(arg=f"LEVEL: {self.score}    HIGH_SCORE: {self.high_score}", align= 'center', font=('COURIER', 20, 'normal'))

    def level_up(self):
        self.clear()
        self.score+=1
        self.write(arg=f"LEVEL: {self.score}    HIGH_SCORE: {self.high_score}", align= 'center', font=('COURIER', 20, 'normal'))

    # def reset_score(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(arg=f"Game Over\nYou Reach level {self.score}👌", align='center', font=('COURIER', 20, 'normal'))
    #     self.score = 1

    def reset(self):
        if self.high_score< self.score:
            self.high_score=self.score
            with open('records.txt',mode='w') as file:
                file.write(f'{self.high_score}')
        self.clear()
        self.score=0
        self.level_up()



