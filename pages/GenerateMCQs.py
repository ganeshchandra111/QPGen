from tkinter import *
import tkinter as tk

class GenerateMCQs(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' Here in this page you can generate the MCQs ''')
        self.lable.pack(padx=10,pady=10)

        