from tkinter import *

# TODO: import libraries.

REPS= 0
TIMER= None

#TODO: requierment variables

window=Tk()
window.title('Pomodoro 🍅')
window.config(padx=100, pady=50,bg='oldlace')

# TODO: set window's configuration.

def tik_tok(t):
    '''count down the timer!'''
    global TIMER

    min=int(t/60)
    sec=int(t%60)

    if min<10 and sec<10:
        canvas.itemconfig(clock_canvas, text=f'0{min}:0{sec}')
    elif min>10 and sec<10:
        canvas.itemconfig(clock_canvas, text=f'{min}:0{sec}')
    elif min<10 and sec>10:
        canvas.itemconfig(clock_canvas, text=f'0{min}:{sec}')
    else:
        canvas.itemconfig(clock_canvas, text=f'{min}:{sec}')

    #importan part: create count down system for timer .
    if t > 0:
        TIMER= window.after(2, tik_tok,t-1)
    else :
        start_timer()
        check_mark.config(text=int(REPS / 2) * '👍')

#TODO: create tik_tok function to show the time.

def start_timer():
    '''check what is our step?'''
    global REPS
    REPS+=1

    work_min= 25*60
    short_rest_min= 5*60
    long_rest_min= 20*60

    if REPS % 8 == 0:
        label.config(text='REST FOR 20 MIN', fg='red')
        tik_tok(long_rest_min)
        REPS=0

    elif REPS % 2 == 0 :
        label.config(text='REST FOR 5 MIN', fg='red')
        tik_tok(short_rest_min)

    else:
        label.config(text='WORK HARD', fg='green')
        tik_tok(work_min)

#TODO: create function 'start_timer' for command argument in start_button.

def reset_timer():
    '''reset game to begin'''
    global REPS, TIMER

    #use this build-in function to stop timer
    window.after_cancel(TIMER)
    REPS=0
    canvas.itemconfig(clock_canvas, text='00:00')
    label.config(text='Timer', fg='teal', bg='oldlace',font=('Times', 20, 'italic'))
    check_mark.config(text='')

#TODO: create function that make reset button works.

label= Label(text='Timer', fg='teal', bg='oldlace',font=('Times', 20, 'italic'))
label.grid(row=0, column=1)

# TODO: create timer label.

canvas=Canvas(width=200, height=224, bg='oldlace', highlightthickness=0)
tomato_image= PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)

clock_canvas= canvas.create_text(100,130,text='00:00',fill='white',font=('Times', 22, 'bold italic'))
canvas.grid(row=1, column=1)

# TODO: create tomato image and set timer text.

start_button= Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

# TODO: create 'start_button'.

reset_button= Button(text='Reset', command=reset_timer)
reset_button.grid(row=2 ,column=2)

#TODO: create 'reset button'.

check_mark=Label(text='',highlightthickness=0,fg='teal',bg='oldlace')
check_mark.grid(row=2, column=1)

#TODO: create check mark which show to user that what is user step?

window.mainloop()