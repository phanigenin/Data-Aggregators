__author__ = 'phani'
__author__ = 'phani'
from tkinter import *
from tkinter import *
from tkinter.ttk import *

top = Tk()

def helloCallBack():
   tkinter.tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()