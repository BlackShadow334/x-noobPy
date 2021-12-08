from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel1.grid(row=0, column=0)


def myClick():
    myLabel2 = Label(root, text="My name is rupesh anand")
    myLabel2.grid(row=1, column=1)


myButton = Button(root, text="click me", command=myClick)
myButton.grid()
root.mainloop()



