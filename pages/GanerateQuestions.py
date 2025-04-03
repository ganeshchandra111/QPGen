from tkinter import *
import tkinter as tk
import json
import os

class GenerateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)
        self.create_form()  # Call the method correctly

    def create_form(self):
        Label(self, text="Fill The Details").grid(row=0, column=1, columnspan=4, pady=10)

        Label(self, text="College Name:").grid(row=1, column=0, sticky="w")
        
        # Define JSON file path
        current_folder = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_folder, "..", "data")
        
        if not os.path.exists(json_file_path):
            os.makedirs(json_file_path)

        file_path = os.path.join(json_file_path, 'collegeName.json')
        
        # Load College Name from JSON safely
        college_name = "Default College"  # Default name
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    college_name = data.get("CollegeName", "Default College")
            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Using default college name.")

        # Display College Name
        Label(self, text=f"{college_name}").grid(row=1, column=1, sticky="w", columnspan=3)

        Label(self, text="Year:").grid(row=2, column=0, sticky="w")
        year = Entry(self, width=10)
        year.grid(row=2, column=1, pady=5)

        Label(self, text="Semester:").grid(row=2, column=2, sticky="w")
        semester = Entry(self, width=10)
        semester.grid(row=2, column=3, pady=5)

        Label(self, text="Mode of Exam:").grid(row=2, column=4, sticky="w")
        mode_of_exam = Entry(self, width=10)
        mode_of_exam.grid(row=2, column=5, pady=5)

        Label(self, text="Max Marks:").grid(row=2, column=6, sticky="w")
        max_marks = Entry(self, width=10)
        max_marks.grid(row=2, column=7, pady=5)

        Label(self, text="Branch:").grid(row=3, column=0, sticky="w")
        branch = Entry(self, width=10)
        branch.grid(row=3, column=1, pady=5)

        Label(self, text="Subject:").grid(row=3, column=2, sticky="w")
        subject = Entry(self, width=10)
        subject.grid(row=3, column=3, pady=5)

        Label(self, text="Date:").grid(row=3, column=4, sticky="w")
        date = Entry(self, width=10)
        date.grid(row=3, column=5, pady=5)

        Label(self, text="Duration:").grid(row=3, column=6, sticky="w")
        duration = Entry(self, width=10)
        duration.grid(row=3, column=7, pady=5)

        next_button = Button(self, text="Next", width=10)
        next_button.grid(row=4, column=1, columnspan=4, pady=20)

# Initialize the main Tkinter window

