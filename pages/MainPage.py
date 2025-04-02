from tkinter import *
import tkinter as tk
import os
import json

class MainPage(tk.Frame):

    def show_name(self):
        name = self.collegeName.get()

        # Get the current script's folder path
        current_folder_path = os.path.dirname(os.path.abspath(__file__))

        # Define the relative path to the data folder
        data_folder_path = os.path.join(current_folder_path, '..', 'data')

        # Ensure the data folder exists; create it if it doesn't
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        # Define the path for the JSON file
        file_path = os.path.join(data_folder_path, 'collegeName.json')

        # Save the data to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump({'CollegeName': name}, json_file, indent=4)

        print(f"Data saved to {file_path}")


    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the main page ''')
        self.lable.pack(padx=10,pady=10)

        self.CollegeNameFrame = tk.Frame(self) #THsi is a Frame for collge name entry 
        self.collegeName = tk.Entry(self.CollegeNameFrame,width=100)
        self.collegeNameButton = tk.Button(self.CollegeNameFrame, text="Submit College Name",command=self.show_name)

        # Packing the widgets
        self.collegeName.grid(row=0,column=0,padx=10,pady=10)
        self.collegeNameButton.grid(row=0, column=1,padx=10, pady=10)
        self.CollegeNameFrame.pack(padx=10,pady=10)

