from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import json, os


class EditQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the Edit Questions page ''')
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
        self.filebutton = Button(self.fileSelectionFrame,text="Open File",command=self.loadQuestionsFromFile)
        self.filebutton.grid(row=0,column=2,padx=5,pady=10)
        self.fileNameEntry.grid(row=0, column=1, padx=5, pady=10)
        self.fileSelectionFrame.grid(row=0, column=0,columnspan=3)

        # Select unit to store it in
        self.unitNumberFrame = Frame(self.Essentials)
        self.unitNumeberLabel = Label(self.unitNumberFrame, text="Select Unit: ").grid(row=1, column=0, padx=5, pady=10)
        self.unitOptions = [f"Unit {i}" for i in range(1, 6)]
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame, values=self.unitOptions, width=20, state="readonly")
        self.unitNumberEntry.grid(row=1, column=1, padx=5, pady=10)
        self.unitNumberFrame.grid(row=1, column=0)

        # Select the marks for the question
        self.marksFrame = Frame(self.Essentials)
        self.marksLabel = Label(self.marksFrame, text="Select Marks: ").grid(row=1, column=1, padx=5, pady=10)
        self.marksOptions = [2, 5, 10]
        self.marksEntry = ttk.Combobox(self.marksFrame, values=self.marksOptions, width=20, state="readonly")
        self.marksEntry.grid(row=1, column=2, padx=5, pady=10)
        self.marksFrame.grid(row=1, column=1)

    
        # Cognitive level also known as bloom taxamony to specify the question type as thing like understand,evaulate,etc 
        self.btFrame = Frame(self.Essentials)
        self.btLabel = Label(self.btFrame, text="Select BT: ").grid(row=1, column=2, padx=5, pady=10)
        self.btOptions = ["Understand", "Analyze", "Evaluate", "Remember"]
        self.btEntry = ttk.Combobox(self.btFrame, values=self.btOptions, width=20, state="readonly")
        self.btEntry.grid(row=1, column=3, padx=5, pady=10)
        self.btFrame.grid(row=1,column=2)

        #pack essential frame as we dont need to config it further
        self.Essentials.pack()


        #Frame to load the question frame to take questions from user
        self.questionTextFrame = Frame(self.QuestionsEntryFrame, width=100)
        self.questionEntryLabel = Label(self.questionTextFrame, text="Enter your question:")
        self.questionEntry = Text(self.questionTextFrame, height=2, width=50)
        self.questionEntryLabel.grid(row=0, column=0, padx=5, pady=5)
        self.questionEntry.grid(row=0, column=1, padx=5, pady=5)

        # pack essential as have finished the ui for questions
        self.questionTextFrame.pack()

        
        # Submit Button
        self.submitButton = Button(self.QuestionsEntryFrame, text="Edit Question", width=50, command=self.saveQuestions)
        self.submitButton.pack(pady=20)

        # To give notes and appropriate output after trying to insert data into the files
        self.LastQuestionFrame = Frame(self.QuestionsEntryFrame)
        self.LastQuestionLabel = Label(self.LastQuestionFrame, text="")
        self.LastQuestionLabel.pack()
        self.LastQuestionFrame.pack(pady=20)

        # Packing the main frame
        self.QuestionsEntryFrame.pack()



    def loadQuestionsFromFile(self):
        """Loads questions from the selected JSON file"""
        self.filename = self.fileNameEntry.get().strip()
        if not self.filename:
            messagebox.showerror("Error", "Please select a file!")
            return

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "Questions", f"{self.filename}.json")

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

        # Destroy previous frame if it exists
        if hasattr(self, "questionFrame"):
            self.questionFrame.destroy()

        # Create main frame
        self.questionFrame = Frame(self)
        self.questionFrame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Create canvas and scrollbar for scrollable content
        canvas = Canvas(self.questionFrame, height=400)
        scrollbar = Scrollbar(self.questionFrame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Add scroll with mouse wheel
        def on_mouse_scroll(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        canvas.bind_all("<MouseWheel>", on_mouse_scroll)

        #If File is empty
        if not data:
            # Label(scrollable_frame, text="No questions found.", font=("Arial", 12)).pack(pady=10)
            self.LastQuestionLabel.config(text="No questions found.")
            return

        # Display questions by unit and marks
        for unit, marks_data in data.items():
            unitFrame = Frame(scrollable_frame)
            unitFrame.pack(fill="x", padx=10, pady=10)

            Label(unitFrame, text=f'📘 Unit: {unit}', font=("Arial", 12, "bold")).pack(pady=5)

            for marks, questions in marks_data.items():
                Label(unitFrame, text=f'   📝 {marks} Marks', font=("Arial", 11, "italic")).pack(anchor="w")

                for index, q in enumerate(questions, 1):
                    #Loading the unit and marks into dictionary
                    question_data = q.copy()
                    question_data['unit'] = unit
                    question_data['marks'] = marks

                    question_text = q.get("question")
                    bt = q.get("bt")

                    questionFrame = Frame(unitFrame, relief="groove", borderwidth=2)
                    questionFrame.pack(fill="x", pady=5, padx=10)

                    Label(questionFrame, text=f"{index}. {question_text}", font=("Arial", 10, "bold"), wraplength=400, justify="left").grid(row=0, column=0, sticky="w", padx=5, pady=5)

                    Label(questionFrame, text=f"BT Level: {bt}", font=("Arial", 9)).grid(row=1, column=0, sticky="w", padx=5)

                    btnFrame = Frame(questionFrame)
                    btnFrame.grid(row=0, column=1, rowspan=2, padx=10)

                    Button(btnFrame, text="Edit", width=6, 
                        command=lambda q=question_data: self.EditQuestion(q['unit'],q['marks'],q['bt'],q['question'])).pack(pady=2)

                    Button(btnFrame, text="DEL", width=6, 
                        command=lambda q=question_data: self.deleteQuestions(q['unit'],q['marks'],q['bt'],q['question'])).pack(pady=2)


        
    def getAllFilesFromQuestionsFolder(self):
        """get all the files from the data/questions folder"""
        
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


    def EditQuestion(self,unit,marks,bt,question):
        """Selects the question and shows its values in the UI"""
        
        #Values to use when saving the question
        self.selected_unit = unit
        self.selected_marks = marks
        self.selected_bt = bt
        self.selected_question = question


        #Setting the values of the Comboboxes and text to the question value we want to edit
        self.unitNumberEntry.set(unit)
        self.marksEntry.set(marks)
        self.btEntry.set(bt)
        self.questionEntry.delete('1.0',END)
        self.questionEntry.insert('1.0',question)

        
        
    def deleteQuestions(self,unit,marks,bt,question):
        """Deletes the question"""

        #If there is no question
        if not question:
            self.LastQuestionLabel.config(text="Error: Please enter a question.")
            return

        # Setting up folder and file paths
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        file_path = os.path.join(data_folder_path, f"{self.filename}.json")

        # Load existing data if available
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        # Try to delete the question if it exists
        if unit in data and marks in data[unit]:
            questions_list = data[unit][marks]
            original_length = len(questions_list)
            # Filter out the question you want to delete
            data[unit][marks] = [x for x in questions_list if x.get("question") != question]

            if len(data[unit][marks]) < original_length:
                # Save the updated data
                with open(file_path, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4)
                self.LastQuestionLabel.config(text="Deleted Question")
            else:
                self.LastQuestionLabel.config(text="Question not found")
        else:
            self.LastQuestionLabel.config(text="Unit or marks not found")
        self.loadQuestionsFromFile()

    def saveQuestions(self):
        """Saves the edited Question"""
        
        new_unit = self.unitNumberEntry.get()
        new_marks = self.marksEntry.get()
        new_question = self.questionEntry.get("1.0", END).strip()
        new_bt = self.btEntry.get()

        #If the question feild is empty
        if not new_question:
            self.LastQuestionLabel.config(text="Error: Please enter a question.")
            return

        # Setting up folder and file paths
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        file_path = os.path.join(data_folder_path, f"{self.filename}.json")

        # Load existing data if available
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        if (new_unit == self.selected_unit and
            new_marks == self.selected_marks and
            new_question == self.selected_question and
            new_bt == self.selected_bt):

            self.LastQuestionLabel.config(text="Edit the Question")
            return


        # Find and update the question in the JSON structure
        question_updated = False
        for old_unit, unit_data in data.items():

            for old_marks, questions_list in unit_data.items():

                for question_entry in questions_list:

                    if (old_unit == self.selected_unit and
                        old_marks == self.selected_marks and
                        question_entry["question"] == self.selected_question and
                        question_entry["bt"] == self.selected_bt):
                        
                        # Update the question details
                        question_entry["question"] = new_question
                        question_entry["bt"] = new_bt

                        # If unit or marks are changed, move to the appropriate section
                        if old_unit != new_unit or old_marks != new_marks:
                            # Remove from old location
                            questions_list.remove(question_entry)

                            # Add to new location in JSON structure
                            if new_unit not in data:
                                data[new_unit] = {}
                            if new_marks not in data[new_unit]:
                                data[new_unit][new_marks] = []
                            data[new_unit][new_marks].append(question_entry)
                        question_updated = True
                        break

                if question_updated:
                    break
            if question_updated:
                break

        # Insert the data into the json file
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
            self.LastQuestionLabel.config(text="Edditted Question")

        #Empty the values in the fields unit,marks,bt and questions
        self.unitNumberEntry.set("")
        self.marksEntry.set("")
        self.btEntry.set("")
        self.questionEntry.delete('1.0',END)

        #Load the questions again
        self.loadQuestionsFromFile()
