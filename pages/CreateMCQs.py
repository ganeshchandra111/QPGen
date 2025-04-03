from tkinter import *
import tkinter as tk
from tkinter import ttk
import json,os,random,string

class CreateMCQs(tk.Frame):

    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' Here you can create MCQs This is the CreateMCQs page ''')
        self.lable.pack(padx=10,pady=10)

        # this is the main frame that is there in this entire page, everything that is diplayed in this page
        # can be found within this frame
        self.MCQQuestionsEntryFrame = Frame(self)

        # Essentials meaning the filename and unit number
        self.Esstentials = Frame(self.MCQQuestionsEntryFrame) 

        # this code is the UI for the user to enter the file name, this also displayes the files that are in that folder
        self.fileNameFrame = Frame(self.Esstentials)
        self.fileNameLabel = Label(self.fileNameFrame,text="Select a file or create new one: ").grid(row=0, column=0,padx=5, pady=10)
        self.AllFiles = self.getAllFilesFromMCQsFolder()
        self.fileNameEntry = ttk.Combobox(self.fileNameFrame,width=20,values=self.AllFiles)
        self.fileNameEntry.grid(row=0, column=1,padx=5, pady=10)
        self.fileNameFrame.grid(row=0, column=0)

        # this code askes user to select the unit number
        self.unitNumberFrame = Frame(self.Esstentials)
        self.unitNumeberLabel = Label(self.unitNumberFrame,text="Select Unit: ").grid(row=0, column=0,padx=5, pady=10)
        self.options=['Unit1',"unit2","unit3","unit4","unit5"]
        self.unitNumberEntry = ttk.Combobox(self.unitNumberFrame,values=self.options,width=20,state="readonly")
        self.unitNumberEntry.current(0)
        self.unitNumberEntry.grid(row=0, column=1,padx=5, pady=10)
        self.unitNumberFrame.grid(row=0,column=1)
        
        self.Esstentials.pack()
        
        # This is where the questions entry start
        self.MCQquestionFrame = Frame(self.MCQQuestionsEntryFrame,width=100)
        self.questionEntryLable = Label(self.MCQquestionFrame,text="Enter your question: ")
        self.questionEntry = Entry(self.MCQquestionFrame, width=100)
        self.questionEntryLable.grid(row=0,column=0)
        self.questionEntry.grid(row=0, column=1)

        # All options frame, in this frame all the options will be located and displayed likewise
        self.MCQOptionsFrame = Frame(self.MCQQuestionsEntryFrame,width=100)

        #This the frame which holds a single option1 entry box
        self.Option1Frame = Frame(self.MCQOptionsFrame)
        self.option1Label = Label(self.Option1Frame,text="Option-1: ").grid(row=0,column=0,padx=5,pady=10)
        self.option1Entry = Entry(self.Option1Frame)
        self.option1Entry.grid(row=0,column=1,padx=5,pady=10)
        self.Option1Frame.grid(row=0,column=1)

        #This the frame which holds a single option2 entry box
        self.Option2Frame = Frame(self.MCQOptionsFrame)
        self.option2Label = Label(self.Option2Frame,text="Option-2: ").grid(row=0,column=0,padx=5,pady=10)
        self.option2Entry = Entry(self.Option2Frame)
        self.option2Entry.grid(row=0,column=1,padx=5,pady=10)
        self.Option2Frame.grid(row=0,column=1)

        #This the frame which holds a single option3 entry box
        self.Option3Frame = Frame(self.MCQOptionsFrame)
        self.option3Label = Label(self.Option3Frame,text="Option-3: ").grid(row=0,column=0,padx=5,pady=10)
        self.option3Entry = Entry(self.Option3Frame)
        self.option3Entry.grid(row=0,column=1,padx=5,pady=10)
        self.Option3Frame.grid(row=0,column=1)

        #This the frame which holds a single option4 entry box
        self.Option4Frame = Frame(self.MCQOptionsFrame)
        self.option4Label = Label(self.Option4Frame,text="Option-4: ").grid(row=0,column=0,padx=5,pady=10)
        self.option4Entry = Entry(self.Option4Frame)
        self.option4Entry.grid(row=0,column=1,padx=5,pady=10)
        self.Option4Frame.grid(row=0,column=1)

        # Here are are packing and arraging the main elements 
        self.MCQquestionFrame.pack()        
        self.Option1Frame.grid(row=0,column=0)
        self.Option2Frame.grid(row=0,column=1)
        self.Option3Frame.grid(row=1,column=0)
        self.Option4Frame.grid(row=1,column=1)
        self.MCQOptionsFrame.pack()

        #BUTTON
        self.AddQuestion = Button(self.MCQQuestionsEntryFrame,text="Add Question",width=50, command=self.addQuestion)
        self.AddQuestion.pack()

        # THis code handels the the text that is displyed in the bottom of the Frame, 
        # this shows the last question that is enterd 
        # This also shows the warning and errors if there are any 
        self.LastQuestionAddedFrame=Frame(self.MCQQuestionsEntryFrame)
        self.LastQuestionAddedNoteLable = Label(self.LastQuestionAddedFrame,text="When you add a quesiton that will be displayed down here\n*Note* only the latest added Question will be displayed")
        self.LastQuestionAddedLable = Label(self.LastQuestionAddedFrame)
        self.LastQuestionAddedNoteLable.pack()
        self.LastQuestionAddedLable.pack()
        self.LastQuestionAddedFrame.pack(pady=20)

        # Here the main frame of this page ends, this page holds everything that is there in this page
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
                            text="This question already exists in the selected unit!"
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
                self.LastQuestionAddedLable.config(text="You have Missed some values please Entery all values")
        except :
                self.LastQuestionAddedLable.config(text="Something went Wrong")
                
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

            print(json_files)  # Output: ['unit1', 'unit2', 'sample']

            return json_files
        except:
            return []


