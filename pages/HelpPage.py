import tkinter as tk
from tkinter import Label, Frame, Canvas, Scrollbar

class HelpPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot, bg="#f7f9fa")

        self.label = Label(
            self,
            text="This is how you can use this software",
            font=("Segoe UI", 14, "bold"),
            fg="#2c3e50",
            bg="#f7f9fa"
        )
        self.label.pack(padx=10, pady=20, anchor="w")

        self.canvasFrame = Frame(self, bg="#f7f9fa")

        canvas = Canvas(self.canvasFrame, height=400, bg="#f7f9fa", highlightthickness=0)
        scrollbar = Scrollbar(self.canvasFrame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#f7f9fa")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def on_mouse_scroll(event):
            try:
                canvas.yview_scroll(-1 * (event.delta // 120), "units")
            except:
                pass
        canvas.bind_all("<MouseWheel>", on_mouse_scroll)

        def update_wraplength(event):
            new_wraplength = event.width - 60
            for widget in scrollable_frame.winfo_children():
                if isinstance(widget, Label) and widget.cget("wraplength"):
                    widget.configure(wraplength=new_wraplength)

        canvas.bind("<Configure>", update_wraplength)


        def add_section(frame, heading, text):
            heading_label = Label(
                frame,
                text=heading,
                font=("Segoe UI", 14, "bold"),
                fg="#34495e",
                bg="#f7f9fa",
                justify="left",
                anchor="w"
            )
            text_label = Label(
                frame,
                text=text,
                font=("Segoe UI", 10),
                fg="#34495e",
                bg="#f7f9fa",
                justify="left",
                anchor="w",
            )
            heading_label.pack(padx=20, pady=(10, 4), anchor="w")
            text_label.pack(padx=40, pady=(0, 10), anchor="w")

        add_section(scrollable_frame, "Create Questions",
        "1.In the create Page You can First select the file you want to store the questions or can create by typing the file name in the subject box.\n" \
        "2.Then you can select what unit you want the questions to be in by selecting a unit from the dropbox menu.\n" \
        "3.You can do the same for Marks and also for Bloom Taxamony\n" \
        "4.After That you can Type the question into the Text box and save the question\n" \
        "5.If successfully saved then you can see the output as question saved or if unsuccessful it will show the error that might have occured\n"
        )

        add_section(scrollable_frame, "Generate Questions",
        "1.In the Generate Page You need the enter the nessecary details like Mode of Examination ,Subject, Set Number , Subject file \n" \
        "2.After that you need Select the mode of exam (Mid,Sem) from the drop box menu \n" \
        "3.Now select the subject file from the select file from the drop box menu \n" \
        "4.Click on the generate questions to generate questions for the particular exam (mid,sem) \n" \
        "5.You can edit the questions there itself but it will not save the changes to the data in the file \n" \
        "6.Click the save to word button if you are satisfied with the generated questions \n" \
        "7.Select the destination of where you want to save the file in \n"
        )

        add_section(scrollable_frame, "Edit Questions",
        "1.In Edit Questions Page You can select the subject which you want to edit the questions of \n" \
        "2.Click Open File which will load all the questions of the subject which you have entered. \n" \
        "3.You can scroll across the loaded questions from the subject and choose what you want to do with the questions \n" \
        "4.After deciding what questions you want to change you can either the edit button beside the question or the delete button the question from the subject's question bank \n" \
        "5.If you click edit all the criteria is loaded into the inputs and you can just edit the question by either selecting the dropboxes or by changing the text of question \n" \
        "6.After editing the question you can click edit question which prompts the output text as editted Question if Successfull or will prompt with the approipate error \n" \
        "7.If you click delete button the question is then deleted from the question bank and will prompt deleted question \n" \
        "8.The Questions are loaded again after performing actions to indicate the changes has been done to questions in the subject \n"
        )

        add_section(scrollable_frame, "Create MCQs",
        "1.In the Create MCQs Page You can either select or create a subject to store to the MCQs by either typing the subject name or selecting it from the drop box \n" \
        "2.Then you can select what unit the MCQ belongs to by selecting the unit from the drop box named select unit \n" \
        "3.You can now type the question of the MCQ in the questions text box and the options of the questions in the options box \n" \
        "4.After that you can click the button Add Questions to add that MCQ into the question bank \n" \
        "5.If successfull it will give the output added question into the subject or give appropriate error if not saved \n"
        )

        add_section(scrollable_frame, "Generate MCQs",
        "1.In Generate MCQs page You select the file of which you want to generate questions from \n" \
        "2.After selecting the file you can click the generate MCQs Button to generate questions \n" \
        "3.20 MCQs are then genereated from the questions present in the file you selected \n" \
        "4.If you are want to make changes to the generated questions \n" \
        "5.You can edit the questions there itself but it will not save the changes to the data in the file \n" \
        "6.Click the save to word button if you are satisfied with the generated questions \n" \
        "7.Select the destination of where you want to save the file in \n" \
        "8.Check the saved file to see all the four sets of MCQs in the file \n" \
        "9.You can also create a question bank by adding some extra questions to the generated questions by clicking the create question bank button and save it into a word doucment in the specified path \n"
        )

        add_section(scrollable_frame, "Edit MCQs",
        "1.In the edit MCQs Page You select the file in which you want to change the Questions or Options of \n" \
        "2.You click the button load questions to load all the questions in the file \n" \
        "3.Select the question to which you want to make changes to and click on either edit or delete button \n" \
        "4.If you click the edit button the questions of and options of that question are loaded into the entry boxes where you can make changes to them \n" \
        "5.After making changes to the question you can select the save changes button to save the changes to the question that you have done that you have done \n" \
        "6.If the question change is saved successfully then it will output changes saved successfully and if not saved then it will propmt an appropriate error \n" \
        "7.The questions are then loaded again to show the changes done to the question \n" \
        "8.If you select the Delete Questions button the question is deleted from the file and the questions are loaded again to show the changed done to the file \n"
        )

        self.canvasFrame.pack(fill="both", expand=True, padx=10, pady=10)
