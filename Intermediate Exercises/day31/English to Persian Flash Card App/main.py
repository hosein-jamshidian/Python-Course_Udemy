from tkinter import *
import pandas as pd
import random

# TODO: Requiermants libraries.

BACKGROUND_COLOR= '#B1DDC6'
CURRENT_CARD=[]
KNOWN_LIST= []

# TODO: variables.

window= Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#TODO: set windows configuration.

# ----------------------------------------------- READING DATA --------------------------------------------

try:
    data = pd.read_csv('remain_words.csv')
except FileNotFoundError:
    data = pd.read_csv('english_words.csv').rename(columns={'Unnamed: 1': 'Persian'})

print(len(data))

#----------------------------------------------- Next Data Function --------------------------------------

def next_data():
    global CURRENT_CARD,flip_timer

    window.after_cancel(flip_timer)

    # TODO: fix bug that happend when click on button more than 1 time.

    index= random.choice(range(len(data)))
    CURRENT_CARD.append(index)

    canvas.itemconfig(front_img, image=f_img)
    canvas.itemconfig(title_txt, text="English",fill='green')
    canvas.itemconfig(word_txt,text=data['English'][CURRENT_CARD[-1]],fill='black')

    flip_timer= window.after(ms=3000, func=flip_card)

# TODO: function that use for right or wrong button.

#---------------------------------------------- Flip Card -------------------------------------------------

def flip_card():
    global CURRENT_CARD

    canvas.itemconfig(front_img,image=b_img)
    canvas.itemconfig(title_txt, text='Persian', fill='red')
    canvas.itemconfig(word_txt, text=f"{data['Persian'][CURRENT_CARD[-1]]}",fill='white')

# ----------------------------------------------- Known Words ------------------------------------------------

def is_known():
    global CURRENT_CARD

    KNOWN_LIST.append(data.iloc[CURRENT_CARD[-1]])
    data.drop(CURRENT_CARD[-1],axis=0,inplace=True)
    data.reset_index(inplace=True,drop=True)
    print(len(data))
    data.to_csv('remain_words.csv',index=0)

    next_data()

# TODO: Create and download a csv file include of unknow words.

#----------------------------------------------- UI Setup ------------------------------------------------

flip_timer=window.after(ms= 3000, func=flip_card)

# TODO: use after to pause window for 3 sec after each click on button.

canvas=Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

b_img=PhotoImage(file='images/card_back.png')
f_img= PhotoImage(file='images/card_front.png')

front_img=canvas.create_image(400, 263, image= f_img)
title_txt= canvas.create_text(400, 150, text='', fill='green', font= ('Times', 35,'bold italic'))
word_txt= canvas.create_text(400, 270, text='', fill='black', font=('Ariel',70, 'bold'))
canvas.grid(row= 0, column= 0,columnspan=2)

# TODO: create back ground image and shape of words.

r_img= PhotoImage(file='images/right.png')
right_button= Button(image=r_img, highlightthickness=0, command= is_known)
right_button.grid(row=1 ,column=0)

#TODO: create right  button.

w_img= PhotoImage(file='images/wrong.png')
wrong_button=Button(image= w_img, highlightthickness=0, command=next_data)
wrong_button.grid(row=1,column=1)

#TODO: create wrong button.

next_data()

#TODO: I decided to call 'next_data' function here to app automatically start with a word.

window.mainloop()