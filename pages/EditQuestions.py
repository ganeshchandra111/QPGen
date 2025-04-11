from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import json, os


class EditQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)
        self.pack(padx=20, pady=20)

        # Title Label
        self.label = ttk.Label(self, text="This is the Edit Questions Page", font=("Arial", 16, "bold"))
        self.label.pack(pady=(0, 10))

        # Main Frame that contains all the other frames in the page
        self.QuestionsEntryFrame = ttk.Frame(self)

        # Essentials Frame
        self.Essentials = ttk.Frame(self.QuestionsEntryFrame)

        # Subject File Selection Frame
        self.fileSelectionFrame = ttk.Frame(self.Essentials)
        ttk.Label(self.fileSelectionFrame, text="Select or create a Subject:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.allFiles = self.getAllFilesFromQuestionsFolder()   
        self.fileNameEntry = ttk.Combobox(self.fileSelectionFrame, width=20, values=self.allFiles, state="readonly")
        self.filebutton = ttk.Button(self.fileSelectionFrame, text="Open File", command=self.loadQuestionsFromFile)
        self.fileNameEntry.grid(row=0, column=1, padx=10, pady=10)
        self.filebutton.grid(row=0, column=2, padx=10, pady=10)
        self.fileSelectionFrame.grid(row=0, column=0, columnspan=3)

        # Unit Number Frame
        self.unitNumberFrame = ttk.Frame(self.Essentials)
        ttk.Label(self.unitNumberFrame, text="Select Unit:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.unitOptions = [f"Unit {i}" for i in range(1, 6)]
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame, values=self.unitOptions, width=20, state="readonly")
        self.unitNumberEntry.grid(row=1, column=1, padx=10, pady=10)
        self.unitNumberFrame.grid(row=1, column=0)

        # Marks Frame
        self.marksFrame = ttk.Frame(self.Essentials)
        ttk.Label(self.marksFrame, text="Select Marks:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.marksOptions = [2, 5, 10]
        self.marksEntry = ttk.Combobox(self.marksFrame, values=self.marksOptions, width=20, state="readonly")
        self.marksEntry.grid(row=1, column=1, padx=10, pady=10)
        self.marksFrame.grid(row=1, column=1)

        # Bloom's Taxonomy Frame
        self.btFrame = ttk.Frame(self.Essentials)
        ttk.Label(self.btFrame, text="Select BT:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.btOptions = ["Understand", "Analyze", "Evaluate", "Remember"]
        self.btEntry = ttk.Combobox(self.btFrame, values=self.btOptions, width=20, state="readonly")
        self.btEntry.grid(row=1, column=1, padx=10, pady=10)
        self.btFrame.grid(row=1, column=2)

        # Pack Essentials Frame
        self.Essentials.pack(pady=10)

        # Question Text Entry Frame
        self.questionTextFrame = ttk.LabelFrame(self.QuestionsEntryFrame, text="Question Entry", padding=(10, 10))
        ttk.Label(self.questionTextFrame, text="Enter your question:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.questionEntry = Text(self.questionTextFrame, height=5, width=50, font=("Courier", 10))
        self.questionEntry.grid(row=0, column=1, padx=10, pady=10)
        self.questionTextFrame.pack(pady=10)

        # Submit Button
        self.submitButton = tk.Button(
            self.QuestionsEntryFrame,
            text="Edit Question",
            width=30,
            font=("Segoe UI", 10, "bold"),
            bg="#28a745",  # Green background
            fg="white",  # White text
            activebackground="#218838",  # Darker green for hover
            activeforeground="white",  # White text on hover
            relief="flat",  # Flat button design
            cursor="hand2",  # Hand cursor on hover
            command=self.saveQuestions
        )
        self.submitButton.pack(pady=(10, 20))

        # Output Message Frame
        self.LastQuestionFrame = ttk.LabelFrame(self.QuestionsEntryFrame, text="Output")
        self.LastQuestionLabel = ttk.Label(self.LastQuestionFrame, text="", foreground="green")
        self.LastQuestionLabel.pack()
        self.LastQuestionFrame.pack(pady=5)

        # Pack Main Frame
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


        # Create a scrollable frame for questions
        canvas = Canvas(self.questionFrame, height=400, width=500)
        scrollbar = Scrollbar(self.questionFrame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind mouse wheel scrolling
        def on_mouse_scroll(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        canvas.bind_all("<MouseWheel>", on_mouse_scroll)
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        #If File is empty
        if not data:
            # Label(scrollable_frame, text="No questions found.", font=("Arial", 12)).pack(pady=10)
            self.LastQuestionLabel.config(text="No questions found.")
            return

        for unit, marks_data in data.items():
                unitFrame = Frame(scrollable_frame)
                unitFrame.pack(fill="x", padx=10, pady=10)

                # Unit label (updated for consistency with the other UI)
                Label(unitFrame, text=f'📘 Unit: {unit}', font=("Arial", 12, "bold")).pack(pady=5)

                for marks, questions in marks_data.items():
                    # Marks label with slight modification for consistency
                    Label(unitFrame, text=f'   📝 {marks} Marks', font=("Arial", 11, "italic")).pack(anchor="w")

                    for index, q in enumerate(questions, 1):
                        # Prepare data for the buttons
                        question_data = q.copy()
                        question_data['unit'] = unit
                        question_data['marks'] = marks

                        question_text = q.get("question")
                        bt = q.get("bt")

                        # Frame for each question
                        questionFrame = Frame(unitFrame, relief="groove", borderwidth=2)
                        questionFrame.pack(fill="x", pady=5, padx=10)

                        # Question label with the updated UI style
                        Label(questionFrame, text=f"{index}. {question_text}", font=("Arial", 10, "bold"), wraplength=400, justify="left").grid(row=0, column=0, sticky="w", padx=5, pady=5)

                        # BT Level label (updated style)
                        Label(questionFrame, text=f"BT Level: {bt}", font=("Arial", 9)).grid(row=1, column=0, sticky="w", padx=5)

                        # Buttons Frame
                        btnFrame = Frame(questionFrame)
                        btnFrame.grid(row=0, column=1, rowspan=2, padx=10)

                        # Edit button
                        Button(btnFrame, text="Edit", width=6, 
                            command=lambda q=question_data: self.EditQuestion(q['unit'], q['marks'], q['bt'], q['question'])).pack(pady=2)

                        # Delete button
                        Button(btnFrame, text="DEL", width=6, 
                            command=lambda q=question_data: self.deleteQuestions(q['unit'], q['marks'], q['bt'], q['question'])).pack(pady=2)

        
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
