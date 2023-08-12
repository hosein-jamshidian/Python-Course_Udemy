from tkinter import *
from tkinter import messagebox
import random
import json

#TODO: import requierments library.

window=Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

#TODO: set configuration.

#----------------------------------------- Generate Password ---------------------------------------------

def generate_pass():
    '''clear password entry and next create a strong password for user.'''
    password_entry.delete(0,END)

    password_entry.clipboard_clear()
    letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    numbers='1 2 3 4 5 6 7 8 9 0'.split()
    symbols='! @ $ % ^ & * . - + ?'.split()

    letters_password= [random.choice(letters) for index in range(random.randint(8,10))]
    numbers_password= [random.choice(numbers) for index in range(random.randint(2,4))]
    symbols_password= [random.choice(symbols) for index in range(random.randint(2,4))]
    password= letters_password+ numbers_password+ symbols_password

    random.shuffle(password)
    password_entry.insert(0,''.join(password))

#TODO: create 'generate_pass function to create a password with strong strategy.

#----------------------------------------- Add Button Configuration --------------------------------------

def add():
    '''add inforamtion like website and password and username to a text file named database and then clear enteries.'''
    WEBSITE=web_entry.get()
    USERNAME=username_entry.get()
    PASSWORD=password_entry.get()

    new_data={
        WEBSITE:{
            'username': USERNAME,
            'password': PASSWORD
        }
    }

    if len(WEBSITE)<1  or len(PASSWORD)<1:
        messagebox.showerror(title="DATABASE ERROR", message="oops! one of you're entry is not completed.")
    else:
        allow=messagebox.askokcancel(title="DATABASE INFO",message=f"Does '{WEBSITE}' website \nfor '{USERNAME}' user \nwith '{PASSWORD}' password \nis right ??")
        if allow:

            try:
                with open('database.json',mode='r') as file :
                    data= json.load(file)
            #TODO: using try to read data from our json file.

            except:
                with open('database.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            #TODO: using except for that moment our json file is empty or not exist.

            else:
                data.update(new_data)
                with open('database.json',mode='w') as file:
                    json.dump(data, file, indent=4)
            #TODO: using else for append new data to our json file.

            finally:
                password_entry.delete(0, END)
                web_entry.delete(0, END)
            #TODO: using finally for clear password and website entry.

        else:
            messagebox.showerror(title='DATABASE Error',message="Nothing added to database.\nYou just click on cancel for some reason.")
            password_entry.delete(0, END)
            web_entry.delete(0, END)

#TODO: create 'add' function to add user information to database taxt file .

# ------------------------------------------ Search Button Configuration------------------------------------

def search():
    WEBSITE = web_entry.get()
    with open('database.json',mode='r') as file :
        data=json.load(file)
    try:
        output= [v for k,v in data.items() if k==WEBSITE]
        if len(output)<1:
            raise ValueError

    except ValueError:
        messagebox.showerror(title='Error',message='No Data File Found')

    else:
        messagebox.showinfo(title=f'{WEBSITE}', message=f"Password: {output[0]['password']}\nUsername: {output[0]['username']}")

#TODO: create search button to search for username and password that user save this information before.

#------------------------------------------- UI Setup ------------------------------------------------------

canvas=Canvas(width= 200,height= 200 )
get_image=PhotoImage(file='logo.png')
logo_image= canvas.create_image(100,100,image=get_image)
canvas.grid(row=0, column=1)

#TODO: create our logo picture.

web_label=Label(text='Website:',font=('Times',10,'bold italic'))
web_label.grid(row=1, column=0)

#TODO: create website label.

web_entry=Entry(width=32)
web_entry.focus()
web_entry.grid(row=1, column=1)

#TODO: create website Entry.
#
search_button=Button(text="Search", width=15, command=search)
search_button.grid(row=1,column=2,columnspan=2)

#TODO: create search button.

username_label= Label(text='Email/Username:',font=('Times',10,'bold italic'))
username_label.grid(row=2, column=0)

#TODO: create email/username label.

username_entry=Entry(width=52)
username_entry.insert(0,'jamshidian@gmail.com')
username_entry.grid(row=2, column=1,columnspan=2)

#TODO: create email/username Entry.

password_label= Label(text='Password:',font=('Times',10,'bold italic'))
password_label.grid(row=3, column=0)

#TODO: create password label.

password_entry=Entry(width=32)
password_entry.grid(row=3, column=1)

#TODO: create password Entry.

generate_button=Button(text='Generate Password  ', highlightthickness=0,command=generate_pass)
generate_button.grid(row=3, column=2)

#TODO: create 'generate_password' button.

add_button=Button(text='Add',width=44, command=add)
add_button.grid(row=4, column=1,columnspan=2)

#TODO: create 'Add' button.

window.mainloop()