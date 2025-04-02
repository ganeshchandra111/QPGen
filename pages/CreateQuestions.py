from tkinter import *
from tkinter import ttk
import tkinter as tk

class CreateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)


        #Variables used 
        self.marks_vari = tk.StringVar()
        self.unit_vari = tk.StringVar()
        self.ques = tk.StringVar()


        self.lable = Label(self, text=''' This is the Questions Creations page ''')
        self.lable.grid(padx=10,pady=10)



        #Creating a menu to select Units 
        self.text = Label(self,text="Select Unit")
        self.units = ttk.Combobox(self,textvariable=self.unit_vari,values=[f"Unit {i}" for i in range(1,6)],state="readonly")
        self.units.current(0)  #Set Default Value as 1 (index value)

        self.text.grid(row=1, column=0, sticky="w")
        self.units.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        
        #Creating a menu to select marks
        self.text = Label(self,text="Select Marks")
        self.marks = ttk.Combobox(self,textvariable=self.marks_vari,values=[2,5,10],state="readonly")
        self.marks.current(0) #Set Default Value as 2 (index value)

        self.text.grid(row=2, column=0, sticky="w")
        self.marks.grid(row=2,column=1,padx=10,pady=5, sticky='w')


        #Taking Questions
        self.text=Label(self,text="Enter Questions(Enter one question at a time)")
        self.input = Entry(self)

        self.text.grid(row=3,columnspan=2)
        self.input.grid(row=4,columnspan=2,rowspan=2)

        #Submit question to save into a json
        self.submit= Button(self,text="Submit Question",command=self.save_questions)

        self.submit.grid(row=4,column=3)


    def save_questions(self):

        self.question =  self.input.get()
        print(self.question) 