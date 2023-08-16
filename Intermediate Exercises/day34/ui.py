from tkinter import *
from quiz import Quiz
import time

theme_color='#375362'
# ------------------------------------------------- UI Class -----------------------------------------------------------
class UI(Tk):
    def __init__(self,question:Quiz):
        '''using tk class for inheritance and aloso use qustion argument that connect us to Quiz class attributes and methods.'''
        super().__init__()

        self.question=question
        self.title('Quizzler')
        self.config(padx=20 , pady=20, bg=theme_color)
        #TODO: Set configurations.

        self.score_label = Label(text=f"Score :0", bg=theme_color, fg='white', pady=5, font=('Ariel', 10, 'bold'))
        self.score_label.grid(row=0, column=1)
        # TODO: Set Score Label.


        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text_box= self.canvas.create_text(150, 125 , text="", width=280,fill=theme_color, font=('Time', 20, 'bold italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #TODO: Set our Text box to show question's text.

        false_pic=PhotoImage(file='images/false.png')
        self.false_button=Button(image=false_pic,command=self.false_answer)
        self.false_button.grid(row=2,column=0)
        #TODO: Create False button.

        true_pic = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_pic,command=self.true_answer)
        self.right_button.grid(row=2, column=1)
        #TODO:Create True Button.

        self.next_question()
        #TODO: for showen the question from the begining.
        self.mainloop()

#--------------------------------------------------------- Next Question -----------------------------------------------
    def next_question(self):
        if self.question.still_question():
            self.score_label.config(text=f'Score : {self.question.score}')
            self.current_question=self.question.question_bank[self.question.question_number]
            q_text=self.current_question.question
            self.canvas.itemconfig(self.text_box, text=f"Q.{self.question.question_number+1}: {q_text}?")
            self.canvas.config(bg='white')
        else:
            self.canvas.config(bg='pink')
            self.canvas.itemconfig(self.text_box, text=f"DONE!\nTotal Score : {self.question.score}/{self.question.question_number}")
            self.false_button.grid_remove()
            self.right_button.grid_remove()

#------------------------------------------------------- False Button Command ------------------------------------------
    def false_answer(self):
        answer=self.question.question_bank[self.question.question_number].answer
        if answer=='False':
            self.question.score += 1
            self.canvas.config(bg='green')
            self.after(1000,self.next_question)

        else:
            self.canvas.config(bg='red')
            self.after(1000, self.next_question)
        self.question.question_number+=1

#------------------------------------------------------- True Button Command -------------------------------------------
    def true_answer(self):
        answer = self.question.question_bank[self.question.question_number].answer
        if answer == 'True':
            self.question.score += 1
            self.canvas.config(bg='green')
            self.after(1000, self.next_question)
        else:
            self.canvas.config(bg='red')
            self.after(1000, self.next_question)
        self.question.question_number += 1