'''
Tkinter:Handling buttons
'''

from tkinter import *

root = Tk()

def dosomething():
    print("You clicked the button")

button1= Button(root,text="click here",command=dosomething)
button1.pack()

root.mainloop()