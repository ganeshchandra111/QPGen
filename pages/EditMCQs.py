from tkinter import *
import tkinter as tk
import os, json
from tkinter import ttk

class EditMCQs(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.selected_question = None  # Track which question is selected for editing

        self.lable = Label(self, text='EditMCQs')
        self.lable.pack(padx=10, pady=10)

        self.EditMCQsFrame = Frame(self)

        self.fileSelectorFrame = Frame(self.EditMCQsFrame, width=50)
        self.fileSelectLable = Label(self.fileSelectorFrame, text="Select the File: ")
        self.options = self.getAllFilesFromMCQsFolder()
        self.fileSelectDropBox = ttk.Combobox(self.fileSelectorFrame, values=self.options, state='readonly')
        if self.options:
            self.fileSelectDropBox.current(0)
        self.fileSelectButton = Button(self.fileSelectorFrame, text='Select file', command=self.PrintAllTheQuestionsWithEditButton)
        self.fileSelectLable.grid(row=0, column=0)
        self.fileSelectDropBox.grid(row=0, column=1)
        self.fileSelectButton.grid(row=0, column=2)
        self.fileSelectorFrame.pack()

        self.EditFrame = Frame(self.EditMCQsFrame)

        # This is the Question Frame
        self.EditQuestionFrame = Frame(self.EditFrame)
        self.EditQuestionLable = Label(self.EditQuestionFrame, text="Edit your question here: ")
        self.EditQuestionEntry = Entry(self.EditQuestionFrame, width=100)
        self.EditQuestionLable.grid(row=0, column=0)
        self.EditQuestionEntry.grid(row=0, column=1)
        self.EditQuestionFrame.pack(pady=5)

        # All options frame, for the option entry boxes
        self.MCQOptionsFrame = Frame(self.EditFrame, width=100)

        # Option 1
        self.Option1Frame = Frame(self.MCQOptionsFrame)
        self.option1Label = Label(self.Option1Frame, text="Option-1: ")
        self.option1Label.grid(row=0, column=0, padx=5, pady=10)
        self.option1Entry = Entry(self.Option1Frame)
        self.option1Entry.grid(row=0, column=1, padx=5, pady=10)
        self.Option1Frame.grid(row=0, column=0)

        # Option 2
        self.Option2Frame = Frame(self.MCQOptionsFrame)
        self.option2Label = Label(self.Option2Frame, text="Option-2: ")
        self.option2Label.grid(row=0, column=0, padx=5, pady=10)
        self.option2Entry = Entry(self.Option2Frame)
        self.option2Entry.grid(row=0, column=1, padx=5, pady=10)
        self.Option2Frame.grid(row=0, column=1)

        # Option 3
        self.Option3Frame = Frame(self.MCQOptionsFrame)
        self.option3Label = Label(self.Option3Frame, text="Option-3: ")
        self.option3Label.grid(row=0, column=0, padx=5, pady=10)
        self.option3Entry = Entry(self.Option3Frame)
        self.option3Entry.grid(row=0, column=1, padx=5, pady=10)
        self.Option3Frame.grid(row=1, column=0)

        # Option 4
        self.Option4Frame = Frame(self.MCQOptionsFrame)
        self.option4Label = Label(self.Option4Frame, text="Option-4: ")
        self.option4Label.grid(row=0, column=0, padx=5, pady=10)
        self.option4Entry = Entry(self.Option4Frame)
        self.option4Entry.grid(row=0, column=1, padx=5, pady=10)
        self.Option4Frame.grid(row=1, column=1)

        self.MCQOptionsFrame.pack()

        # Save Changes Button
        self.saveButton = Button(self.EditFrame, text="Save Changes", command=self.SaveChanges, width=50)
        self.saveButton.pack(pady=10)

        self.EditFrame.pack()

        self.DisplayQuestionsFrame = Frame(self.EditMCQsFrame)
        self.DisplayQuestionsNoteLable = Label(self.DisplayQuestionsFrame, text="Here you can see all of your Questions\nClick on the Edit Button to edit that particular question")
        self.DisplayQuestionsNoteLable.pack()
        self.DisplayQuestionsFrame.pack()

        self.messageLabel = Label(self, text="", fg="red")
        self.messageLabel.pack(pady=10)
        
        self.EditMCQsFrame.pack()

        # Message label at the bottom of the frame

    def updateMessage(self, msg, color="red"):
        """Update the message label with a message and optional color."""
        self.messageLabel.config(text=msg, fg=color)

    def PrintAllTheQuestionsWithEditButton(self):
        # Clear previous UI and reset message
        for widget in self.DisplayQuestionsFrame.winfo_children():
            widget.destroy()
        self.updateMessage("")

        selectedFile = self.fileSelectDropBox.get().strip()
        if not selectedFile:
            self.updateMessage("No file selected!")
            return

        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')
        if not os.path.exists(data_folder_path):
            try:
                os.makedirs(data_folder_path)
            except Exception as e:
                self.updateMessage("Error creating folder: " + str(e))
                return

        filePath = os.path.join(data_folder_path, f'{selectedFile}.json')
        data = {}
        if os.path.exists(filePath):
            try:
                with open(filePath, 'r', encoding='utf-8') as jsonFile:
                    data = json.load(jsonFile)
            except json.JSONDecodeError as e:
                self.updateMessage("Error reading JSON: " + str(e))
            except Exception as e:
                self.updateMessage("Error opening file: " + str(e))
        else:
            self.updateMessage("File does not exist: " + filePath)
            return

        # Create a scrollable frame for questions
        canvas = Canvas(self.DisplayQuestionsFrame, height=400, width=500)
        scrollbar = Scrollbar(self.DisplayQuestionsFrame, orient="vertical", command=canvas.yview)
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

        # Display questions from JSON
        try:
            for key, value in data.items():
                unitFrame = Frame(scrollable_frame)
                unitFrame.pack(fill="x", padx=10, pady=10)

                QuestionsDisplayUnitLable = Label(unitFrame, text=f'Unit: {key}', font=("Arial", 12, "bold"))
                QuestionsDisplayUnitLable.pack(pady=5)

                if not isinstance(value, list):
                    self.updateMessage("Data for key " + key + " is not a list!")
                    continue

                for index, val in enumerate(value):
                    # Validate keys in each question object
                    question = val.get('question', "No Question")
                    option1 = val.get('option1', "N/A")
                    option2 = val.get('option2', "N/A")
                    option3 = val.get('option3', "N/A")
                    option4 = val.get('option4', "N/A")

                    singleQuestionFrame = Frame(unitFrame, relief="groove", borderwidth=2)
                    singleQuestionFrame.pack(pady=5, padx=5, fill="x")

                    singleQuestionLabel = Label(singleQuestionFrame, text=question, font=("Arial", 10, "bold"), width=50, wraplength=400)
                    singleQuestionLabel.grid(row=0, column=0, pady=5, padx=5, sticky="w")

                    optionsFrame = Frame(singleQuestionFrame)
                    optionsFrame.grid(row=1, column=0, columnspan=2, pady=5)

                    Label(optionsFrame, text="A: " + option1).grid(row=0, column=0, padx=5, pady=2, sticky="w")
                    Label(optionsFrame, text="B: " + option2).grid(row=0, column=1, padx=5, pady=2, sticky="w")
                    Label(optionsFrame, text="C: " + option3).grid(row=1, column=0, padx=5, pady=2, sticky="w")
                    Label(optionsFrame, text="D: " + option4).grid(row=1, column=1, padx=5, pady=2, sticky="w")

                    # Add Edit Button with lambda to pass values
                    editButton = Button(singleQuestionFrame, text="Edit",
                        command=lambda q=question, o1=option1, o2=option2, o3=option3, o4=option4: self.EditFunction(q, o1, o2, o3, o4))
                    editButton.grid(row=0, column=1, padx=10, pady=5, sticky="e")

                    # Add Delete Button with lambda to pass values
                    DeleteButton = Button(singleQuestionFrame, text="DEL",
                        command=lambda q=question, o1=option1, o2=option2, o3=option3, o4=option4: self.DeleteQuestion(q, o1, o2, o3, o4))
                    DeleteButton.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        except Exception as e:
            self.updateMessage("Error displaying questions: " + str(e))

    def DeleteQuestion(self, question, opt1, opt2, opt3, opt4):
        selectedFile = self.fileSelectDropBox.get().strip()
        if not selectedFile:
            self.updateMessage("No file selected for deletion!")
            return

        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')
        filePath = os.path.join(data_folder_path, f'{selectedFile}.json')

        if not os.path.exists(filePath):
            self.updateMessage("File does not exist: " + filePath)
            return

        try:
            with open(filePath, 'r', encoding='utf-8') as jsonFile:
                data = json.load(jsonFile)
        except Exception as e:
            self.updateMessage("Error reading file for deletion: " + str(e))
            return

        deleted = False
        try:
            for key, value in data.items():
                if not isinstance(value, list):
                    continue
                for i, question_data in enumerate(value):
                    if (question_data.get('question') == question and
                        question_data.get('option1') == opt1 and
                        question_data.get('option2') == opt2 and
                        question_data.get('option3') == opt3 and
                        question_data.get('option4') == opt4):
                        del value[i]
                        deleted = True
                        break
                if deleted:
                    break
        except Exception as e:
            self.updateMessage("Error during deletion loop: " + str(e))
            return

        if deleted:
            try:
                with open(filePath, 'w', encoding='utf-8') as jsonFile:
                    json.dump(data, jsonFile, indent=4, ensure_ascii=False)
                self.updateMessage("Question deleted successfully!", "green")
            except Exception as e:
                self.updateMessage("Error saving file after deletion: " + str(e))
        else:
            self.updateMessage("No matching question found for deletion!")

        self.PrintAllTheQuestionsWithEditButton()

    def EditFunction(self, question, opt1, opt2, opt3, opt4):
        # Set the selected question so we can update it later
        self.selected_question = question

        # Warn if entries are not empty (unsaved changes)
        if (self.EditQuestionEntry.get().strip() or
            self.option1Entry.get().strip() or
            self.option2Entry.get().strip() or
            self.option3Entry.get().strip() or
            self.option4Entry.get().strip()):
            self.updateMessage("Overriding unsaved changes.")

        # Clear existing values safely
        for entry in [self.EditQuestionEntry, self.option1Entry, self.option2Entry, self.option3Entry, self.option4Entry]:
            entry.delete(0, END)

        # Insert new values into entries
        self.EditQuestionEntry.insert(0, question)
        self.option1Entry.insert(0, opt1)
        self.option2Entry.insert(0, opt2)
        self.option3Entry.insert(0, opt3)
        self.option4Entry.insert(0, opt4)
        self.updateMessage("")  # Clear any messages

    def SaveChanges(self):
        selectedFile = self.fileSelectDropBox.get().strip()
        if not selectedFile:
            self.updateMessage("No file selected for saving!")
            return

        if not self.selected_question:
            self.updateMessage("No question is selected for update!")
            return

        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')
        filePath = os.path.join(data_folder_path, f'{selectedFile}.json')
        if not os.path.exists(filePath):
            self.updateMessage("File not found: " + filePath)
            return

        try:
            with open(filePath, 'r', encoding='utf-8') as jsonFile:
                data = json.load(jsonFile)
        except Exception as e:
            self.updateMessage("Error loading JSON for saving: " + str(e))
            return

        # Get new values from entry fields and trim any extra spaces
        new_question = self.EditQuestionEntry.get().strip()
        new_option1 = self.option1Entry.get().strip()
        new_option2 = self.option2Entry.get().strip()
        new_option3 = self.option3Entry.get().strip()
        new_option4 = self.option4Entry.get().strip()

        if not new_question:
            self.updateMessage("Question cannot be empty!")
            return

        updated = False
        try:
            for key, value in data.items():
                if not isinstance(value, list):
                    continue
                for question_data in value:
                    if question_data.get('question') == self.selected_question:
                        question_data['question'] = new_question
                        question_data['option1'] = new_option1
                        question_data['option2'] = new_option2
                        question_data['option3'] = new_option3
                        question_data['option4'] = new_option4
                        updated = True
                        break
                if updated:
                    break
        except Exception as e:
            self.updateMessage("Error updating question data: " + str(e))
            return

        if updated:
            try:
                with open(filePath, 'w', encoding='utf-8') as jsonFile:
                    json.dump(data, jsonFile, indent=4, ensure_ascii=False)
                self.updateMessage("Changes saved successfully!", "green")
            except Exception as e:
                self.updateMessage("Error saving JSON file: " + str(e))
        else:
            self.updateMessage("No matching question was found to update.")

        # Clear the entry fields after saving
        for entry in [self.EditQuestionEntry, self.option1Entry, self.option2Entry, self.option3Entry, self.option4Entry]:
            entry.delete(0, END)
        

        self.selected_question = None  # Reset the selected question
        self.PrintAllTheQuestionsWithEditButton()

    def getAllFilesFromMCQsFolder(self):
        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')
            json_files = []
            if os.path.exists(folder_path):
                for f in os.listdir(folder_path):
                    if f.endswith(".json"):
                        json_files.append(f[:-5])
            else:
                self.updateMessage("Folder not found: " + folder_path)
            return json_files
        except Exception as e:
            self.updateMessage("Error getting JSON files: " + str(e))
            return []

