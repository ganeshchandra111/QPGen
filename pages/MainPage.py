from tkinter import *
import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the main page ''')
        self.lable.pack(padx=10,pady=10)