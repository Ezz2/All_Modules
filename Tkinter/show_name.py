# By Ezz

from tkinter import *

root = Tk()
root.geometry("400x200")

# Creating A LAbel Widget
myLabel = Label(root, text="My Name's Ezz")
myLabel_Hello = Label(root, text="Hello")
myLabel3 = Label(root, text="                      ")
myLabel4 = Label(root, text="                      ")

myLabel_Hello.grid(row=1, column=8)
myLabel3.grid(row=1, column=1)

myLabel.grid(row=2, column=8)
myLabel4.grid(row=1, column=5)


root.mainloop()
