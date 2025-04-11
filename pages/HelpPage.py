from tkinter import *
import tkinter as tk

class HelpPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is how you can use this software ''')
        self.lable.pack(padx=10,pady=10)

        self.canvasFrame = Frame(self)

        # Create canvas and scrollbar for scrollable content
        canvas = Canvas(self.canvasFrame, height=400)
        scrollbar = Scrollbar(self.canvasFrame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(self.canvasFrame)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left",fill=BOTH, expand=True)
        scrollbar.pack(side='right',fill='y')

        # Add scroll with mouse wheel
        def on_mouse_scroll(event):
            try:
                canvas.yview_scroll(-1 * (event.delta // 120), "units")
            except:
                pass
        canvas.bind_all("<MouseWheel>", on_mouse_scroll)

        # Create Questions Frame
        self.createQuestionsFrame = Frame(scrollable_frame)
        
        self.createQuestionsHeadingLabel = Label(self.createQuestionsFrame, text="Create Questions", font=("Arial", 13, "bold"))
        self.createQuestionsLabel = Label(self.createQuestionsFrame,text=
        "1.In the create Page You can First select the file you want to store the questions or can create by typing the file name in the subject box.\n" \
        "2.Then you can select what unit you want the questions to be in by selecting a unit from the dropbox menu.\n" \
        "3.You can do the same for Marks and also for Bloom Taxamony\n" \
        "4.After That you can Type the question into the Text box and save the question\n" \
        "5.If successfully saved then you can see the output as question saved or if unsuccessful it will show the error that might have occured\n"
        ,justify='left', font=("Arial", 10))

        self.createQuestionsHeadingLabel.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.createQuestionsLabel.grid(row=1, column=0, sticky='w', padx=11)

        self.createQuestionsFrame.pack(fill='x', pady=10)

        # Generate Questions Frame
        self.genQuestionsFrame = Frame(scrollable_frame)

        self.genQuestionsHeadingLabel = Label(self.genQuestionsFrame, text="Generate Questions", font=("Arial", 13, "bold"))
        self.genQuesitonsLabel = Label(self.genQuestionsFrame, text=
        "1.In the Generate Page You need the enter the nessecary details like Year,Semester,Branch,Subject,Date,Max Marks \n" \
        "2.After that you need Select the mode of exam (Mid,Sem) from the drop box menu \n" \
        "3.Now select the subject file from the select file from the drop box menu \n" \
        "4.Click on the generate questions to generate questions for the particular exam (mid,sem) \n" \
        "5.If you are want to make changes to the generated questions \n" \
        "6.You can edit the questions there itself but it will not save the changes to the data in the file \n" \
        "7.Click the save to word button if you are satisfied with the generated questions \n" \
        "8.Select the destination of where you want to save the file in \n" \
        ""
        ,justify='left', font=("Arial", 10))

        self.genQuestionsHeadingLabel.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.genQuesitonsLabel.grid(row=1, column=0, sticky='w', padx=11)

        self.genQuestionsFrame.pack(fill='x', pady=10)

        #Edit Questions Frame
        self.editQuestionsFrame = Frame(scrollable_frame)

        self.editQuestionsHeadingLabel = Label(self.editQuestionsFrame,text="Edit Questions",font=("Arial",13,"bold"))
        self.editQuestionsLabel = Label(self.editQuestionsFrame,text=
        "1.In Edit Questions Page You can select the subject which you want to edit the questions of \n" \
        "2.Click Open File which will load all the questions of the subject which you have entered. \n" \
        "3.You can scroll across the loaded questions from the subject and choose what you want to do with the questions \n" \
        "4.After deciding what questions you want to change you can either the edit button beside the question or the delete button the question from \n    the subject's question bank \n" \
        "5.If you click edit all the criteria is loaded into the inputs and you can just edit the question by either selecting the dropboxes or by changing \n    the text of question \n" \
        "6.After editing the question you can click edit question which prompts the output text as editted Question if Successfull or will prompt with \n    the approipate error \n" \
        "7.If you click delete button the question is then deleted from the question bank and will prompt deleted question \n" \
        "8.The Questions are loaded again after performing actions to indicate the changes has been done to questions in the subject \n"
        ,justify='left',font=("Arial",10))

        self.editQuestionsHeadingLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        self.editQuestionsLabel.grid(row=1,column=0,sticky='w',padx=11)

        self.editQuestionsFrame.pack(fill='x', pady=10)

        #Create MCQ Frame
        self.createMCQFrame = Frame(scrollable_frame)

        self.createMCQHeadingLabel = Label(self.createMCQFrame,text="Create MCQs",font=("Arial",13,"bold"))
        self.createMCQLabel = Label(self.createMCQFrame,text=
        "1.In the Create MCQs Page You can either select or create a subject to store to the MCQs by either typing the subject name or selecting it \n    from the drop box \n" \
        "2.Then you can select what unit the MCQ belongs to by selecting the unit from the drop box named select unit \n" \
        "3.You can now type the question of the MCQ in the questions text box and the options of the questions in the options box \n" \
        "4.After that you can click the button Add Questions to add that MCQ into the question bank \n" \
        "5.If successfull it will give the output added question into the subject or give appropriate error if not saved \n"
        ,justify='left',font=("Arial",10))

        self.createMCQHeadingLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        self.createMCQLabel.grid(row=1,column=0,sticky='w',padx=11)

        self.createMCQFrame.pack(fill='x', pady=10)

        #Generate MCQ Frame
        self.genMCQFrame = Frame(scrollable_frame)

        self.genMCQHeadingLabel = Label(self.genMCQFrame,text="Generate MCQs",font=("Arial",13,"bold"))
        self.genMCQLabel = Label(self.genMCQFrame,text=
        "1.In Generate MCQs page You select the file of which you want to generate questions from \n" \
        "2.After selecting the file you can click the generate MCQs Button to generate questions \n" \
        "3.20 MCQs are then genereated from the questions present in the file you selected \n" \
        "4.If you are want to make changes to the generated questions \n" \
        "5.You can edit the questions there itself but it will not save the changes to the data in the file \n" \
        "6.Click the save to word button if you are satisfied with the generated questions \n" \
        "7.Select the destination of where you want to save the file in \n" \
        "8.Check the saved file to see all the four sets of MCQs in the file \n" \
        "9.You can also create a question bank by adding some extra questions to the generated questions by clicking the create question bank button \n    and save it into a word doucment in the specified path \n"
        ,justify='left',font=("Arial",10))

        self.genMCQHeadingLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        self.genMCQLabel.grid(row=1,column=0,sticky='w',padx=11)

        self.genMCQFrame.pack(fill='x', pady=10)

        #Edit MCQ Frame
        self.editMCQFrame = Frame(scrollable_frame)

        self.editMCQHeadingLabel = Label(self.editMCQFrame,text="Edit MCQs",font=("Arial",13,"bold"))
        self.editMCQLabel = Label(self.editMCQFrame,text=
        "1.In the edit MCQs Page You select the file in which you want to change the Questions or Options of \n" \
        "2.You click the button load questions to load all the questions in the file \n" \
        "3.Select the question to which you want to make changes to and click on either edit or delete button \n" \
        "4.If you click the edit button the questions of and options of that question are loaded into the entry boxes where you can make changes to them \n" \
        "5.After making changes to the question you can select the save changes button to save the changes to the question that you have done  \n    that you have done \n" \
        "6.If the question change is saved successfully then it will output changes saved successfully and if not saved then it will propt an \n    appropriate error \n" \
        "7.The questions are then loaded again to show the changes done to the question \n" \
        "8.If you select the Delete Questions button the question is deleted from the file and the questions are loaded again to show the changed done \n    to the file \n"
        ,justify='left',font=("Arial",10))

        self.editMCQHeadingLabel.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        self.editMCQLabel.grid(row=1,column=0,sticky='w',padx=11)

        self.editMCQFrame.pack(fill='x', pady=10)

        self.canvasFrame.pack(side='left',anchor='n',fill='both',expand=True)
        


