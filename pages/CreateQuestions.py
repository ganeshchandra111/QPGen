from tkinter import *
import tkinter as tk
from tkinter import ttk
import json, os

class CreateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot, bg="#f7f9fa")  # Match main bg

        self.label = Label(self, text="📝 Create Questions", font=("Segoe UI", 16, "bold"), bg="#f7f9fa", fg="#2c3e50")
        self.label.pack(padx=10, pady=20)

        self.QuestionsEntryFrame = Frame(self, bg="#f7f9fa")

        # --- Essentials Section ---
        self.Essentials = Frame(self.QuestionsEntryFrame, bg="#f7f9fa")

        # Subject / File Selection
        self.fileSelectionFrame = Frame(self.Essentials, bg="#f7f9fa")
        Label(
            self.fileSelectionFrame, text="Subject:", font=("Segoe UI", 10),
            bg="#f7f9fa", fg="#2c3e50"
        ).grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.allFiles = self.getAllFilesFromQuestionsFolder()
        self.fileNameEntry = ttk.Combobox(self.fileSelectionFrame, width=25, values=self.allFiles, state="normal")
        self.fileNameEntry.grid(row=0, column=1, padx=5, pady=10)
        self.fileSelectionFrame.grid(row=0, column=0, columnspan=3, sticky="w")

        # Unit Number
        self.unitNumberFrame = Frame(self.Essentials, bg="#f7f9fa")
        Label(self.unitNumberFrame, text="Unit:", font=("Segoe UI", 10), bg="#f7f9fa", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.unitOptions = [f"Unit {i}" for i in range(1, 6)]
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame, values=self.unitOptions, width=25, state="readonly")
        self.unitNumberEntry.current(0)
        self.unitNumberEntry.grid(row=0, column=1, padx=5, pady=10)
        self.unitNumberFrame.grid(row=1, column=0, sticky="w")

        # Marks
        self.marksFrame = Frame(self.Essentials, bg="#f7f9fa")
        Label(self.marksFrame, text="Marks:", font=("Segoe UI", 10), bg="#f7f9fa", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.marksOptions = [2, 5, 10]
        self.marksEntry = ttk.Combobox(self.marksFrame, values=self.marksOptions, width=25, state="readonly")
        self.marksEntry.current(0)
        self.marksEntry.grid(row=0, column=1, padx=5, pady=10)
        self.marksFrame.grid(row=1, column=1, sticky="w")

        # BT / Cognitive Level
        self.btFrame = Frame(self.Essentials, bg="#f7f9fa")
        Label(self.btFrame, text="Bloom's Taxonomy:", font=("Segoe UI", 10), bg="#f7f9fa", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.btOptions = ["Understand", "Analyze", "Evaluate", "Remember"]
        self.btEntry = ttk.Combobox(self.btFrame, values=self.btOptions, width=25, state="readonly")
        self.btEntry.current(0)
        self.btEntry.grid(row=0, column=1, padx=5, pady=10)
        self.btFrame.grid(row=1, column=2, sticky="w")

        self.Essentials.pack(padx=20, pady=10)

        # --- Question Text Input ---
        self.questionFrame = Frame(self.QuestionsEntryFrame, bg="#f7f9fa")
        Label(self.questionFrame, text="Enter your question:", font=("Segoe UI", 10), bg="#f7f9fa", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=5)
        self.questionEntry = Text(self.questionFrame, height=3, width=60, font=("Segoe UI", 10))
        self.questionEntry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.questionFrame.pack(pady=10)

        # --- Submit Button ---
        self.submitButton = Button(
            self.QuestionsEntryFrame,
            text="➕ Add Question",
            font=("Segoe UI", 10, "bold"),
            bg="#2ecc71", fg="white",
            activebackground="#27ae60", activeforeground="white",
            relief="flat", padx=10, pady=5,
            width=30,
            command=self.addQuestion
        )
        self.submitButton.pack(pady=20)

        # --- Last Added Question Preview ---
        self.LastQuestionFrame = Frame(self.QuestionsEntryFrame, bg="#f7f9fa")
        self.LastQuestionNoteLabel = Label(
            self.LastQuestionFrame,
            text="Last added question will appear below:",
            font=("Segoe UI", 9, "italic"),
            fg="#7f8c8d", bg="#f7f9fa"
        )
        self.LastQuestionLabel = Label(
            self.LastQuestionFrame,
            text="",
            wraplength=600,
            font=("Segoe UI", 10),
            bg="#f7f9fa",
            fg="#2c3e50"
        )
        self.LastQuestionNoteLabel.pack()
        self.LastQuestionLabel.pack()
        self.LastQuestionFrame.pack(pady=10)

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
