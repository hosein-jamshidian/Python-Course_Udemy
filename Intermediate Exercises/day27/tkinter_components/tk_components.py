import tkinter

window=tkinter.Tk()
window.title("My First tkinter!")
window.minsize(width=500,height=500)

#label

my_label=tkinter.Label(text="hello",font=("Arial",20,'italic'))
my_label.grid(column=0,row=0)


#button


def button_click_bye():
    new=input.get()
    my_label.config(text=new)

button= tkinter.Button(text='click on me',command=button_click_bye)
button.grid(column=2, row=2)

#entry

input=tkinter.Entry(width=10)
input.insert(1,string="email")
print(input.get())
input.grid(column=4, row=4)


#text

text=tkinter.Text(height=5,width=15)
text.focus()
text.insert(tkinter.END,"hi print me !")
print(text.get("2.0",tkinter.END ))
text.grid(column=6, row=6)

#spinbox
def spinbox_user():
    print(spinbox.get())

spinbox=tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_user)
spinbox.grid(column=8, row=8)

#scale

def scale_user(value):
    print(value)

scale=tkinter.Scale(from_=0,to=100,command=scale_user)
scale.grid(column=10, row=10)

#checbutton

def checkbutton_user():
    print(check_state.get())

check_state=tkinter.IntVar()
check_button=tkinter.Checkbutton(text="is on ?",variable=check_state,command=checkbutton_user)
# check_state.get()
check_button.grid(column=8, row=12)


#radio_button

def radio_used():
    print(radio_state.get())

radio_state=tkinter.IntVar()
radio_button1=tkinter.Radiobutton(text='Option2',value=2,variable=radio_state,command=radio_used)
radio_button2=tkinter.Radiobutton(text='Option3',value=3,variable=radio_state,command=radio_used)
radio_button1.grid(column=6, row=14)
radio_button2.grid(column=4, row=16)
#listbox

def listbox_user(event):
    print(listbox.get(listbox.curselection()))

listbox=tkinter.Listbox(height=4)
fruits=["apple","orange","pear","watermelone","banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_user)
listbox.grid(column=2, row=18)

window.mainloop()