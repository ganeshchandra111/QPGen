from tkinter import *
import tkinter as tk
from tkinter import ttk
import json, os


class CreateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.label = Label(self, text="This is the Questions Creation page")
        self.label.pack(padx=10, pady=10)

        # Main Frame that contains all the other frames in the page
        self.QuestionsEntryFrame = Frame(self)

        #Defining a frame named essentials to input take essential stuff
        #It contains frames like subject , unit , marks, cognitive level
        self.Essentials = Frame(self.QuestionsEntryFrame)


        # To select subject file or create a new subject file from the data/questions folder
        self.fileSelectionFrame = Frame(self.Essentials)
        self.fileSelectionLabel = Label(self.fileSelectionFrame, text="Select or create a Subject: ").grid(row=0, column=0, padx=5, pady=10)
        #Get sbuject files from data/questions folder
        self.allFiles = self.getAllFilesFromQuestionsFolder()   
        self.fileNameEntry = ttk.Combobox(self.fileSelectionFrame, width=20, values=self.allFiles)
        self.fileNameEntry.grid(row=0, column=1, padx=5, pady=10)
        self.fileSelectionFrame.grid(row=0, column=0,columnspan=3)

        # Select unit to store it in
        self.unitNumberFrame = Frame(self.Essentials)
        self.unitNumeberLabel = Label(self.unitNumberFrame, text="Select Unit: ").grid(row=1, column=0, padx=5, pady=10)
        self.unitOptions = [f"Unit {i}" for i in range(1, 6)]
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame, values=self.unitOptions, width=20, state="readonly")
        self.unitNumberEntry.current(0)
        self.unitNumberEntry.grid(row=1, column=1, padx=5, pady=10)
        self.unitNumberFrame.grid(row=1, column=0)

        # Select the marks for the question
        self.marksFrame = Frame(self.Essentials)
        self.marksLabel = Label(self.marksFrame, text="Select Marks: ").grid(row=1, column=1, padx=5, pady=10)
        self.marksOptions = [2, 5, 10]
        self.marksEntry = ttk.Combobox(self.marksFrame, values=self.marksOptions, width=20, state="readonly")
        self.marksEntry.current(0)
        self.marksEntry.grid(row=1, column=2, padx=5, pady=10)
        self.marksFrame.grid(row=1, column=1)

    
        # Cognitive level also known as bloom taxamony to specify the question type as thing like understand,evaulate,etc 
        self.btFrame = Frame(self.Essentials)
        self.btLabel = Label(self.btFrame, text="Select BT: ").grid(row=1, column=2, padx=5, pady=10)
        self.btOptions = ["Understand", "Analyze", "Evaluate", "Remember"]
        self.btEntry = ttk.Combobox(self.btFrame, values=self.btOptions, width=20, state="readonly")
        self.btEntry.current(0)
        self.btEntry.grid(row=1, column=3, padx=5, pady=10)
        self.btFrame.grid(row=1,column=2)

        #pack essential frame as we dont need to config it further
        self.Essentials.pack()


        #Frame to load the question frame to take questions from user
        self.questionFrame = Frame(self.QuestionsEntryFrame, width=100)
        self.questionEntryLabel = Label(self.questionFrame, text="Enter your question:")
        self.questionEntry = Text(self.questionFrame, height=2, width=50)
        self.questionEntryLabel.grid(row=0, column=0, padx=5, pady=5)
        self.questionEntry.grid(row=0, column=1, padx=5, pady=5)

        # pack essential as have finished the ui for questions
        self.questionFrame.pack()

        
        # Submit Button
        self.submitButton = Button(self.QuestionsEntryFrame, text="Add Question", width=50, command=self.addQuestion)
        self.submitButton.pack(pady=20)

        # To give notes and appropriate output after trying to insert data into the files
        self.LastQuestionFrame = Frame(self.QuestionsEntryFrame)
        self.LastQuestionNoteLabel = Label(
            self.LastQuestionFrame, text="When you add a question, it will be displayed below.\n*Note: Only the latest added question will be shown."
        )
        self.LastQuestionLabel = Label(self.LastQuestionFrame, text="")
        self.LastQuestionNoteLabel.pack()
        self.LastQuestionLabel.pack()
        self.LastQuestionFrame.pack(pady=20)

        # Packing the main frame
        self.QuestionsEntryFrame.pack()

    def addQuestion(self):

        """Handles saving the entered question into the selected JSON file."""

        #Convert the data of the entry tag to be usable data for the program
        filename = self.fileNameEntry.get().strip()
        if not filename:
            self.LastQuestionLabel.config(text="Error: Please enter or select a file name.")
            return

        #Variables used to get the values from the frames
        unit = self.unitNumberEntry.get()
        marks = self.marksEntry.get()
        question = self.questionEntry.get("1.0", END).strip()
        bt = self.btEntry.get()

        if not question:
            self.LastQuestionLabel.config(text="Error: Please enter a question.")
            return

        # Setting up folder and file paths
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        file_path = os.path.join(data_folder_path, f"{filename}.json")

        # Load existing data if available
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        # Initialize unit if not present
        if unit not in data:
            data[unit] = {}

        # Initialize marks if not present
        if marks not in data[unit]:
            data[unit][marks] = []

        # Check for duplicate question
        for entry in data[unit][marks]:
            if entry["question"] == question:
                self.LastQuestionLabel.config(text="Error: Duplicate question exists.")
                return

        # Add new question
        data[unit][marks].append({"question": question, "bt": bt})

        # Insert the data into the json file
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        # Message displayed if the question is inserted into the data folder
        self.LastQuestionLabel.config(
            text=f"Question Added!\nFile: {filename}\nUnit: {unit}, Marks: {marks}, BT: {bt}\n\nQuestion: {question}"
        )

    def getAllFilesFromQuestionsFolder(self):
        
        #get all the files from the data/questions folder
        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

            json_files = []  # Initialize an empty list

            if not os.path.exists(folder_path):
                return []

            for f in os.listdir(folder_path):
                if f.endswith(".json"):  # Check if it's a JSON file
                    json_files.append(f[:-5])  # Remove ".json" and add to the list

            return json_files
        except:
            return []
