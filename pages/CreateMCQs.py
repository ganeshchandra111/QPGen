from tkinter import *
import tkinter as tk
from tkinter import ttk
import json,os,random,string

class CreateMCQs(tk.Frame):

    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.configure(bg="#f9f9f9")

        self.label = tk.Label(self, text="Create MCQs", font=("Segoe UI", 16, "bold"), bg="#f9f9f9", fg="#333")
        self.label.pack(padx=10, pady=20)

        self.MCQQuestionsEntryFrame = tk.Frame(self, bg="#f9f9f9")

        # Essentials (File Name & Unit Number)
        self.Esstentials = tk.Frame(self.MCQQuestionsEntryFrame, bg="#f9f9f9")

        self.fileNameFrame = tk.Frame(self.Esstentials, bg="#f9f9f9")
        tk.Label(self.fileNameFrame, text="Select or Create File:", bg="#f9f9f9", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5, pady=10)
        self.AllFiles = self.getAllFilesFromMCQsFolder()
        self.fileNameEntry = ttk.Combobox(self.fileNameFrame, width=25, values=self.AllFiles)
        self.fileNameEntry.grid(row=0, column=1, padx=5, pady=10)
        self.fileNameFrame.grid(row=0, column=0)

        self.unitNumberFrame = tk.Frame(self.Esstentials, bg="#f9f9f9")
        tk.Label(self.unitNumberFrame, text="Select Unit:", bg="#f9f9f9", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5, pady=10)
        self.options = ['Unit1', 'Unit2', 'Unit3', 'Unit4', 'Unit5']
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame, values=self.options, width=25, state="readonly")
        self.unitNumberEntry.current(0)
        self.unitNumberEntry.grid(row=0, column=1, padx=5, pady=10)
        self.unitNumberFrame.grid(row=0, column=1)

        self.Esstentials.pack()

        # Question Entry
        self.MCQquestionFrame = tk.Frame(self.MCQQuestionsEntryFrame, bg="#f9f9f9")
        tk.Label(self.MCQquestionFrame, text="Enter your question:", bg="#f9f9f9", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5, pady=10)
        self.questionEntry = tk.Entry(self.MCQquestionFrame, width=80)
        self.questionEntry.grid(row=0, column=1, padx=5, pady=10)
        self.MCQquestionFrame.pack()

        # MCQ Options
        self.MCQOptionsFrame = tk.Frame(self.MCQQuestionsEntryFrame, bg="#f9f9f9")

        def styled_option(frame, label_text):
            f = tk.Frame(frame, bg="#f9f9f9")
            tk.Label(f, text=label_text, bg="#f9f9f9", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5, pady=10)
            entry = tk.Entry(f, width=40)
            entry.grid(row=0, column=1, padx=5, pady=10)
            return f, entry

        self.Option1Frame, self.option1Entry = styled_option(self.MCQOptionsFrame, "Option-1:")
        self.Option2Frame, self.option2Entry = styled_option(self.MCQOptionsFrame, "Option-2:")
        self.Option3Frame, self.option3Entry = styled_option(self.MCQOptionsFrame, "Option-3:")
        self.Option4Frame, self.option4Entry = styled_option(self.MCQOptionsFrame, "Option-4:")

        self.Option1Frame.grid(row=0, column=0)
        self.Option2Frame.grid(row=0, column=1)
        self.Option3Frame.grid(row=1, column=0)
        self.Option4Frame.grid(row=1, column=1)

        self.MCQOptionsFrame.pack(pady=10)

        # Submit Button
        self.AddQuestion = tk.Button(
            self.MCQQuestionsEntryFrame,
            text="Add Question",
            width=50,
            font=("Segoe UI", 10, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.addQuestion
        )
        self.AddQuestion.pack(pady=20)

        # Feedback Label
        self.LastQuestionAddedFrame = tk.Frame(self.MCQQuestionsEntryFrame, bg="#f9f9f9")
        self.LastQuestionAddedNoteLable = tk.Label(
            self.LastQuestionAddedFrame,
            text="When you add a question, it will appear below.\n*Note: Only the latest added question is shown.",
            bg="#f9f9f9",
            fg="#555",
            font=("Segoe UI", 9)
        )
        self.LastQuestionAddedLable = tk.Label(self.LastQuestionAddedFrame, text="", bg="#f9f9f9", font=("Segoe UI", 10, "italic"), fg="green")
        self.LastQuestionAddedNoteLable.pack()
        self.LastQuestionAddedLable.pack()
        self.LastQuestionAddedFrame.pack(pady=20)

        self.MCQQuestionsEntryFrame.pack()

    def addQuestion(self):
        # THis quesiton adds questions into the json file 
        try:
            # print("Question added")

            self.question = self.questionEntry.get()
            self.opt1 = self.option1Entry.get()
            self.opt2 = self.option2Entry.get()
            self.opt3 = self.option3Entry.get()
            self.opt4 = self.option4Entry.get()

            # Checks if the qurestion are empty,if empty it diplays a warning, if not empty it adds the question
            if(self.question!="" or
            self.opt1!="" or
            self.opt2!="" or
            self.opt3!="" or
            self.opt4!="" ):
            
                # Get the current script's folder path
                current_folder_path = os.path.dirname(os.path.abspath(__file__))

                # Define the relative path to the data folder and .. means going back a folder just like in cd command
                data_folder_path = os.path.join(current_folder_path, '..', 'data','MCQs')

                # Ensure the data folder exists; create it if it doesn't
                if not os.path.exists(data_folder_path):
                    os.makedirs(data_folder_path)

                # Define the path for the JSON file
                self.savingFileName = self.fileNameEntry.get()
                file_path = os.path.join(data_folder_path, f'{self.savingFileName}.json')

                # # This below code gives a random string of choosen length, which can be used a key 
                # length = 5 
                # random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                # print(random_string)

                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        try:
                            data = json.load(json_file)  # Load existing JSON data
                        except json.JSONDecodeError:
                            data = {}  # if file is empty or invalid, start fresh
                else:
                    data = {}  # if file doesn't exist, start fresh

                # Add new question to the data
                # This is the json data that we are going to store in the file
                # In future this is what we can ecrypt

                new_question = {
                            'question': self.question,
                            'option1': self.opt1,
                            'option2': self.opt2,
                            'option3': self.opt3,
                            'option4': self.opt4,
                        }
                
                
                selected_unit = self.unitNumberEntry.get()

                # If the unit1 quesiton is already there is appends the new questions to that in array 
                # else it creates a new value using the unit number as the key 

                if selected_unit in data:
                    if any(q['question'] == self.question for q in data[selected_unit]):
                        self.LastQuestionAddedLable.config(
                            text="This question already exists in the selected unit!",
                            fg="red"
                            
                        )
                        return  # Stop execution if duplicate found
                    else:
                        data[selected_unit].append(new_question)
                    # data[selected_unit].append(new_question)
                else:
                    data[selected_unit] = [new_question] 

                # Save the data to the JSON file
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, indent=4)

                # print(f"Data saved to {file_path}")

                self.LastQuestionAddedLable.config(text=f'The Question you have added to file {self.fileNameEntry.get()}. In {selected_unit}\n\n\n Question: {self.question}\nOption 1: {self.opt1}\tOption 2: {self.opt2}\nOption 3: {self.opt3}\tOption 4: {self.opt4}')
            else:
                self.LastQuestionAddedLable.config(text="You have Missed some values please Entery all values",fg="red")
        except :
                self.LastQuestionAddedLable.config(text="Something went Wrong",fg="red")
                
    def getAllFilesFromMCQsFolder(self):
        # This function gets all those json files that are there in that MCQs folder
        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            # Define the relative path to the data folder and .. means going back a folder just like in cd command
            folder_path = os.path.join(current_folder_path, '..', 'data','MCQs')

            json_files = []  # Initialize an empty list

            for f in os.listdir(folder_path):
                if f.endswith(".json"):  # Check if it's a JSON file
                    json_files.append(f[:-5])  # Remove ".json" and add to the list

            # print(json_files)  # Output: ['unit1', 'unit2', 'sample']

            return json_files
        except:
            return []


