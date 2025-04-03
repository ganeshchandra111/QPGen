from tkinter import *
import tkinter as tk

class EditMCQs(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' EditMCQs ''')
        self.lable.pack(padx=10,pady=10)

        