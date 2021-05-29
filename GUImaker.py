from tkinter import *
from tkinter import ttk
from tkinter import messagebox 



class GUI (object):
    def __init__(self, Variabel, Tempat, Text, X, Y):
        self.__Variabel = Variabel
        self.__Tempat = Tempat
        self.__Text = Text
        self.__X = X
        self.__Y = Y
        pass
    
    def NewLabel(self, Variabel, Tempat, Text, X, Y):
        Variabel = Label(Tempat, text=Text)
        Variabel.pack()
        Variabel.place(x=X, y=Y)


