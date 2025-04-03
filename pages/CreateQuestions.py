from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
import json

class CreateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)


        #Variables used 
        self.marks_vari = tk.StringVar()
        self.unit_vari = tk.StringVar()
        self.bt_vari = tk.StringVar()

        


        self.lable = Label(self, text=''' This is the Questions Creations page ''')
        self.lable.grid()



        #Creating a menu to select Units 
        self.text = Label(self,text="Select Unit")
        self.units = ttk.Combobox(self,textvariable=self.unit_vari,values=[f"Unit {i}" for i in range(1,6)],state="readonly")
        self.units.current(0)  #Set Default Value as 1 (index value)

        self.text.grid(row=1, column=0)
        self.units.grid(row=1, column=1)

        
        #Creating a menu to select marks
        self.text = Label(self,text="Select Marks")
        self.marks = ttk.Combobox(self,textvariable=self.marks_vari,values=[2,5,10],state="readonly")
        self.marks.current(0) #Set Default Value as 2 (index value)

        self.text.grid(row=1, column=4,padx=10,pady=5)
        self.marks.grid(row=1,column=5,padx=10,pady=5)


        #Taking Questions
        self.text=Label(self,text="Enter Questions(Enter one question at a time)")
        self.input = Text(self,height=1,width=30)
        self.text2 = Label(self,text="Enter BT")
        self.options = ttk.Combobox(self,textvariable=self.bt_vari,values=["Understand","Analysze","Evaluate","Remember"],state='readonly')
        self.options.current(0)

        self.text.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
        self.input.grid(row=4,column=0,columnspan=2,rowspan=2,padx=10,pady=10)
        self.text2.grid(row=3,column=3,columnspan=2,padx=10,pady=10)
        self.options.grid(row=4,column=3,columnspan=2,padx=10,pady=10)


        # #Submit question to save into a json
        self.submit= Button(self,text="Submit Question",command=self.save_questions)

        self.submit.grid(row=6,column=3)


    def save_questions(self):
        
        unit = self.unit_vari.get()
        mark = self.marks_vari.get()
        question =  self.input.get('1.0',END).strip().split('/n')
        question = ''.join(question)
        bt = self.bt_vari.get()

        text = Label(self,text="")
        text.grid(row=7,column=3,columnspan=2,padx=10,pady=10)
        ques = Label(self,text="")
        ques.grid(row=8,column=3,columnspan=2,padx=10,pady=10)


        #To test if a question has been entered       
        if question=='':
            # Label(self,text="Enter Question").grid(row=7,column=3,columnspan=2,padx=10,pady=10)
            text.config(text="Enter Question")
            # ques.destroy()
            return

            
        
        # Get the current script's folder path
        current_folder_path = os.path.dirname(os.path.abspath(__file__))

        # Define the relative path to the data folder
        data_folder_path = os.path.join(current_folder_path, '..', 'data')

        # Ensure the data folder exists; create it if it doesn't
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)
        
       
        # Define the path for the JSON file
        file_path = os.path.join(data_folder_path, 'Questions.json')
        print("File created")
        
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    json_data = json.load(json_file)  # Load existing JSON data
                except json.JSONDecodeError:
                    json_data = {}  # if file is empty or invalid, start fresh
        else:
            json_data = {}  # if file doesn't exist, start fresh

        

        #Initialize 'unit' if not present in json_data
        if unit not in json_data:
                json_data[unit] = {}

        # Initialize 'mark' if not already present in the 'unit'
        if mark not in json_data[unit]:
            json_data[unit][mark] = []

        #Check For Duplicate Questions        
        for entry in json_data[unit][mark]:
            if entry["question"] == question:
                # Label(self,text="Duplicate Question").grid(row=7,column=3,columnspan=2,padx=10,pady=100)
                text.config(text="Duplicate Question")
                # ques.destroy()
                return

        # Add the question and 'bt' to the 'mark' list
        json_data[unit][mark].append({
            "question": question,
            "bt": bt
        })

        

        # Save the data to the JSON file
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)
            print(json_data)
        
        #Print file path that the json file is in
        print(f"Data saved to {file_path}")

        # text.config(text=f"Question Added \n")
        # self.ques = Label(self,text=f'Unit :{unit} , Marks :{mark} , Question :{question} , BT:{bt}')
        text.config(text=f'Question Added\nUnit : {unit} , Marks : {mark} , Question : {question} , BT : {bt}')
        # self.text.grid(row=7,column=3,columnspan=2,padx=10,pady=10)
        # self.ques.grid(row=8,column=3,columnspan=2,padx=10,pady=10)
