import requests
from tkinter import *

window=Tk()
window.title('Kanye😁✌️')
window.config(padx=50, pady=50)

# ------------------------------------------ Button Command Fuction ---------------------------------------------------
def next():
    response = requests.get(url='https://api.kanye.rest')
    quote = response.json()['quote']
    print(quote)
    canvas.itemconfig(kanye_quotes,text=quote)

#------------------------------------------- Set UI -------------------------------------------------------------------
canvas=Canvas(width=300, height=414)
bg_img= PhotoImage(file='../background.png')
canvas.create_image(150,207,image=bg_img)
kanye_quotes=canvas.create_text(150,190,text='',width=250,fill='white',font=('Time',20,'normal'))
canvas.grid(row=0, column=0)

kanye_img=PhotoImage(file='../kanye.png')
kanye_button= Button(image=kanye_img,command=next)
kanye_button.grid(row=1, column=0)
next()

window.mainloop()