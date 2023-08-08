from tkinter import *

#TODO: import all modules from tkinter library.

screen=Tk()
screen.minsize(width=250, height=150)
screen.config(padx=20,pady=20)

#TODO: create screen use tkinter class and prepare config figure size.

miles_input=Entry(width=10)
miles_input.grid(row=0 ,column=0)

#TODO: create an entry to get miles value.

miles_label=Label(text='Miles', font=('Helvetica', 10, 'bold italic'))
miles_label.grid(row=0, column=1)

# TODO: label that show the 'Miles' text in our program.

equal_label=Label(text='is equal to', font=('Helvetica', 10, 'bold italic'))
equal_label.grid(row=1, column=0)

#TODO: label that show the 'is equal to' text in our program.

km_output=Label(text='0', font=('Arial', 10, 'italic'))
km_output.grid(row=1, column=1)
km_output.config(padx=20,pady=20)

#TODO: the value number show the kilometer that based on input miles value that user give.

km_label= Label(text='KM', font=('Helvetica', 10, 'bold italic'))
km_label.grid(row=1, column=2)

#TODO: label that show the 'KM' text in our program.

def change_km_output():
    km_output['text']=round(float(miles_input.get())*1.609344,2)
    #OR my_label.config(text="New Label!")

#TODO: the function convert the miles value to kilometers value.

button=Button(text= 'Calculate',command=change_km_output, highlightthickness=1)
button.grid(row=2, column=1)

#TODO: create calculate button.

screen.mainloop()
