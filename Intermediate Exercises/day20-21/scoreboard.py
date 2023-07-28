from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        with open("score_memory.txt") as file :
            self.high_score=int(file.read())

        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.goto(-150,270)
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align='center',font=("COURIER", 15, "normal"))

    def score_counter(self):
        self.score+=1
        self.update_score()

    def update_high_score(self):
        if self.score>self.high_score:
            self.high_score=self.score

            with open("score_memory.txt",mode="w") as file :
                file.write(str(self.high_score))

            self.score = 0
            self.update_score()



