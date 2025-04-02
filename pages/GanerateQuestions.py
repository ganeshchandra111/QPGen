from tkinter import *
import tkinter as tk

class GenerateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the Questions GenerationPage page ''')
        self.lable.pack(padx=10,pady=10)

        