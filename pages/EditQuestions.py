from tkinter import *
import tkinter as tk
from tkinter import ttk,scrolledtext,messagebox
import json, os


class EditQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the Questions GenerationPage page ''')
        self.lable.pack(padx=10,pady=10)


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
        self.filebutton = Button(self.fileSelectionFrame,text="Open File",command=self.loadQuestions)
        self.filebutton.grid(row=0,column=2,padx=5,pady=10)
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
        self.submitButton = Button(self.QuestionsEntryFrame, text="Edit Question", width=50, command=self.EditQuestion)
        self.submitButton.pack(pady=20)

        # To give notes and appropriate output after trying to insert data into the files
        self.LastQuestionFrame = Frame(self.QuestionsEntryFrame)
        # self.LastQuestionNoteLabel = Label(
        #     self.LastQuestionFrame, text="When you add a question, it will be displayed below.\n*Note: Only the latest added question will be shown."
        # )
        self.LastQuestionLabel = Label(self.LastQuestionFrame, text="")
        # self.LastQuestionNoteLabel.pack()
        self.LastQuestionLabel.pack()
        self.LastQuestionFrame.pack(pady=20)

        # Packing the main frame
        self.QuestionsEntryFrame.pack()

    def displayQuestions(self, data):
        """Refreshes the frame and displays updated questions in a scrollable list."""
        
        # Check if the frame already exists, destroy it to refresh
        if hasattr(self, "questionFrame"):
            self.questionFrame.destroy()

        # Create a new frame for questions
        self.questionFrame = Frame(self)
        self.questionFrame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Scrollable Text Widget
        textArea = scrolledtext.ScrolledText(self.questionFrame, width=70, height=20, wrap=WORD, font=("Arial", 12))
        textArea.pack(padx=10, pady=10, fill=BOTH, expand=True)

        if not data:
            textArea.insert(END, "No questions found.\n")
            return

        # Display Questions by Unit and Marks
        for unit, marks_data in data.items():
            textArea.insert(END, f"\n📌 {unit}:\n", "bold")
            for marks, questions in marks_data.items():
                textArea.insert(END, f"  ➖ {marks} Marks:\n", "italic")
                for idx, question in enumerate(questions, 1):
                    q_text = question.get("question", "Unknown Question")
                    bt_text = question.get("bt", "N/A")
                    textArea.insert(END, f"    {idx}. {q_text} (BT: {bt_text})\n")

        textArea.tag_configure("bold", font=("Arial", 12, "bold"))
        textArea.tag_configure("italic", font=("Arial", 11, "italic"))


    def loadQuestions(self):
        """Loads questions from the selected JSON file and refreshes UI."""
        filename = self.fileNameEntry.get().strip()
        if not filename:
            messagebox.showerror("Error", "Please select a file!")
            return

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "Questions", f"{filename}.json")

        if not os.path.exists(file_path):
            messagebox.showerror("Error", "File not found!")
            return

        # Load JSON Data
        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON file!")
            return

        # Refresh the UI with new data
        self.displayQuestions(data)

    
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


    def EditQuestion(self):
        print("HELLo")