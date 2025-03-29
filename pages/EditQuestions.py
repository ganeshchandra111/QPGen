from tkinter import *
import tkinter as tk

class EditQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' Here you can Edit Questions ''')
        self.lable.pack(padx=10,pady=10)