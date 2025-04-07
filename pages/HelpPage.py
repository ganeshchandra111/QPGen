from tkinter import *
import tkinter as tk

class HelpPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is how you can use this software ''')
        self.lable.pack(padx=10,pady=10)