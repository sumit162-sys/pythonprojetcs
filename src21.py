'''
Tkinter:Messagebox
'''

from tkinter import *
import tkinter.messagebox



root = Tk()

tkinter.messagebox.showinfo("Title","This is awesome")

response= tkinter.messagebox.askquestion("Question1","Do you like coffee")

if response== 'yes':
    print("Here is a coffee for you")

root.mainloop()