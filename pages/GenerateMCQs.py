from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
import os
import json
import random
from docx import Document

class GenerateMCQs(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.label = Label(self, text="Generate MCQs")
        self.label.pack(padx=10, pady=10)

        self.GenerateMCQsFrame = Frame(self)

        self.GenerateMCQsInputsFrame = Frame(self.GenerateMCQsFrame)

        self.GenerateMCQsLabel = Label(self.GenerateMCQsInputsFrame, text="Select a file: ")
        options = self.GetAllMCQFiles()
        self.GenerateMCQsFileSelect = ttk.Combobox(self.GenerateMCQsInputsFrame, values=options)
        self.GenerateMCQsButton = Button(
            self.GenerateMCQsInputsFrame, text="Generate MCQs", command=self.DisplayQuestionsInTextBox
        )

        self.GenerateMCQsLabel.grid(row=0, column=0, padx=10)
        self.GenerateMCQsFileSelect.grid(row=0, column=1, padx=10)
        self.GenerateMCQsButton.grid(row=0, column=2)

        self.GenerateMCQsInputsFrame.pack()

        self.textArea = Text(self.GenerateMCQsFrame, wrap=WORD, height=20, width=60)
        self.textArea.pack(pady=10)

        self.saveButton = Button(self.GenerateMCQsFrame, text="Save to Word", command=self.SaveQuestionsToWord)
        self.saveButton.pack(pady=5)

        self.updateMessage = Label(self.GenerateMCQsFrame)
        self.updateMessage.pack()

        self.GenerateMCQsFrame.pack()

        self.questions = []

    def GetTheDataInTheSelectedFile(self):
        selectedFile = self.GenerateMCQsFileSelect.get().strip()
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')

        if not os.path.exists(data_folder_path):
            self.updateMessage["text"] = "Data folder does not exist!"
            return {}

        filePath = os.path.join(data_folder_path, f'{selectedFile}.json')
        if not os.path.exists(filePath):
            self.updateMessage["text"] = "File does not exist!"
            return {}

        try:
            with open(filePath, 'r', encoding='utf-8') as jsonFile:
                data = json.load(jsonFile)
            return data
        except json.JSONDecodeError:
            self.updateMessage["text"] = "Invalid JSON file!"
            return {}
        except Exception as e:
            self.updateMessage["text"] = f"Error reading file: {str(e)}"
            return {}

    def GenerateMCQPaper(self, data):
        try:
            units = list(data.keys())
            selected_questions = []

            for unit in units:
                questions = data.get(unit, [])
                if len(questions) < 4:
                    self.updateMessage["text"] = f"Not enough questions in {unit}. Required: 4."
                    return []
                selected_questions.extend(random.sample(questions, 4))

            random.shuffle(selected_questions)
            return selected_questions
        except Exception as e:
            self.updateMessage["text"] = f"Error generating MCQ paper: {str(e)}"
            return []

    def DisplayQuestionsInTextBox(self):
        self.data = self.GetTheDataInTheSelectedFile()
        if not self.data:
            return

        self.questions = self.GenerateMCQPaper(self.data)
        if not self.questions:
            return

        self.textArea.delete(1.0, END)
        for i, question in enumerate(self.questions, 1):
            self.textArea.insert(END, f"Q{i}. {question['question']}\n")
            for j in range(1, 5):
                self.textArea.insert(END, f"  Option {j}: {question[f'option{j}']}\n")
            self.textArea.insert(END, "\n")

    def SaveQuestionsToWord(self):
        try:
            if isinstance(self.data, str):
                self.data = json.loads(self.data)

            if not isinstance(self.data, dict):
                self.updateMessage["text"] = "Invalid questions data format!"
                return
            # Create a Word document
            document = Document()

            # Add title
            document.add_heading('Multiple Choice Questions (MCQ) Paper', level=1)

            # print(self.questions)

            for set in range(4):
                shuffled_questions = self.questions.copy()  # Create a copy to avoid modifying the original list
                random.shuffle(shuffled_questions)  
                document.add_heading(f'SET-{set+1}', level=2)

                # Add questions
                for i, question in enumerate(shuffled_questions, 1):
                    self.question_text = question.get('question', '')
                    self.option1 = question.get('option1', '')
                    self.option2 = question.get('option2', '')
                    self.option3 = question.get('option3', '')
                    self.option4 = question.get('option4', '')

                    # Format question with placeholders
                    document.add_paragraph(f"{i}. {self.question_text}\t\t[   ]", style='Normal')
                    document.add_paragraph(
                        f"1. {self.option1}\t2. {self.option2}\t3. {self.option3}\t4. {self.option4}\n", 
                        style='Normal'
                    )

            # Open save dialog
            save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
            if save_path:
                document.save(save_path)
                self.updateMessage["text"] = f"MCQ Paper saved successfully to {save_path}"
            else:
                self.updateMessage["text"] = "Save operation canceled."

        except Exception as e:
            self.updateMessage["text"] = f"Error saving Word document: {e}"
    
    def GetAllMCQFiles(self):
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_folder_path, '..', 'data', 'MCQs')
        if not os.path.exists(folder_path):
            return []

        return [f[:-5] for f in os.listdir(folder_path) if f.endswith(".json")]
