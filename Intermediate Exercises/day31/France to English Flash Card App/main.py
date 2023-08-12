import tkinter
from tkinter import *
import time
import pandas as pd
import random

bgcolor='#B1DDC6'
current_card= {}

try:
    data=pd.read_csv('remain_words.csv')

except FileNotFoundError:
    original_data=pd.read_csv('french_words.csv')
    data_d=original_data.to_dict(orient='records')

else:
    data_d=data.to_dict(orient="records")


def next():
    global current_card,flip_timer
    try:
        window.after_cancel(flip_timer)
        current_card=random.choice(data_d)
        fr_word=current_card['French']
        canvas.itemconfig(language,text='French')
        canvas.itemconfig(word_card,text=fr_word)
        canvas.itemconfig(front_ground_card,image=front_img)
        flip_timer=window.after(2000,flip_card)
        print(len(data_d))

    except IndexError:
        print('well done !')

def is_known():
    global data_d

    try:
        data_d.remove(current_card)
        a=pd.DataFrame(data_d)
        a.to_csv('remain_words.csv',index=False)
        next()

    except ValueError:
        print('DONE')

def flip_card():
    en_word = current_card['English']
    canvas.itemconfig(language,text='English')
    canvas.itemconfig(word_card,text=en_word,fill='purple')
    canvas.itemconfig(front_ground_card,image=back_img)


window=tkinter.Tk()
window.title('Flashy')
window.config(padx=50,pady=40,bg=bgcolor)
flip_timer=window.after(2000,func=flip_card)

canvas=Canvas(width=800,height=526,bg=bgcolor,highlightthickness=0)
back_img=PhotoImage(file='images//card_back.png')
front_img=PhotoImage(file='images//card_front.png')

front_ground_card=canvas.create_image(400,263,image=front_img)

language=canvas.create_text(400,150,text='Title',font=('Ariel',25,'italic'),fill='green')
word_card=canvas.create_text(400,263,text='word',font=('Ariel',45,'bold'),fill='blue')

canvas.grid(row=0,columnspan=2)


wrong_image=PhotoImage(file='images//wrong.png')
unknown_button=Button(image=wrong_image,bg=bgcolor,highlightthickness=0,command=next)
unknown_button.grid(row=1,column=0)

right_img=PhotoImage(file='images//right.png')
known_button=Button(image=right_img,command=is_known,bg=bgcolor,highlightthickness=0)
known_button.grid(row=1,column=1)

next()


window.mainloop()