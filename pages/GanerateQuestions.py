from tkinter import *
import tkinter as tk
import json
import os
import random
from tkinter import ttk
from docx import Document
from tkinter import filedialog
from docx import Document
from docx.shared import Inches
from tkinter import filedialog, messagebox

class GenerateQuestions(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)
        self.create_form()
        self.create_file_selection_ui()

        # Text widget to display generated questions
        self.generated_display = Text(self, width=80, height=10)
        self.generated_display.grid(row=6, column=0, columnspan=8, pady=10)

        # Define text formatting for headers
        self.generated_display.tag_configure('header', font=('Arial', 12, 'bold'))

        # Buttons
        generate_button = Button(self, text="Generate Questions", width=20, command=self.generate_questions)
        generate_button.grid(row=7, column=5, columnspan=4, pady=10)

        save_button = Button(self, text="Save to Word", width=20, command=self.save_to_word)
        save_button.grid(row=7, column=1, columnspan=4, pady=10)

    def create_form(self):
        Label(self, text="Fill The Details").grid(row=0, column=1, columnspan=4, pady=10)

        Label(self, text="College Name:").grid(row=1, column=0, sticky="w")

        # Define JSON file path
        current_folder = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_folder, "..", "data")

        if not os.path.exists(json_file_path):
            os.makedirs(json_file_path)

        file_path = os.path.join(json_file_path, 'collegeName.json')

        # Load College Name from JSON safely
        college_name = "Default College"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    college_name = data.get("CollegeName", "Default College")
            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Using default college name.")

        # Display College Name
        Label(self, text=f"{college_name}").grid(row=1, column=1, sticky="w", pady=2)

        Label(self, text="Year:").grid(row=2, column=0, sticky="w")
        self.year = Entry(self, width=10)
        self.year.grid(row=2, column=0, pady=5)

        Label(self, text="Semester:").grid(row=2, column=2, sticky="w")
        self.semester = Entry(self, width=10)
        self.semester.grid(row=2, column=3, pady=5)

        Label(self, text="Branch:").grid(row=3, column=0, sticky="w")
        self.branch = Entry(self, width=10)
        self.branch.grid(row=3, column=0, )
        
        Label(self, text="Date:").grid(row=4, column=0, sticky="w")
        self.date = Entry(self, width=10)
        self.date.grid(row=4, column=0, )

        Label(self, text="Subject:").grid(row=3, column=2, sticky="w")
        self.subject = Entry(self, width=10)
        self.subject.grid(row=3, column=3, pady=5)
        Label(self, text="Max Marks:").grid(row=4, column=2, sticky="w")
        self.marks = Entry(self, width=10)
        self.marks.grid(row=4, column=3, pady=5)

    def create_file_selection_ui(self):
    # Frame for selecting the Mode of Examination
        self.selectionFrame = Frame(self)
        self.selectionFrame.grid(row=5, column=0, padx=10, pady=20)

        # Frame for Mode of Examination (Left side)
        self.ModeOFExamFrame = Frame(self.selectionFrame, borderwidth=1, relief="groove", padx=10, pady=10)
        self.ModeOFExamFrame.grid(row=5, column=0, padx=10, pady=10)

        Label(
            self.ModeOFExamFrame,
            text="Select Mode of Examination:",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

        mode_of_exam = ["Mid-I", "Mid-II", "SEM"]
        self.ModeOFExamCombobox = ttk.Combobox(
            self.ModeOFExamFrame,
            width=20,
            values=mode_of_exam,
            state="readonly"
        )
        self.ModeOFExamCombobox.grid(row=1, column=0, padx=5, pady=5)

        # Frame for File Selection (Right side)
        self.fileNameFrame = Frame(self.selectionFrame, borderwidth=1, relief="groove", padx=10, pady=10)
        self.fileNameFrame.grid(row=5, column=1, padx=10, pady=10)

        Label(
            self.fileNameFrame,
            text="Select a File:",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.AllFiles = self.get_all_files_from_questions_folder()

        self.fileNameEntry = ttk.Combobox(
            self.fileNameFrame,
            width=20,
            values=self.AllFiles,
            state="readonly"
        )
        self.fileNameEntry.grid(row=5, column=0, padx=5, pady=5)

    def get_all_files_from_questions_folder(self):
        """Get all JSON files from the data/questions folder."""
        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

            if not os.path.exists(folder_path):
                return []

            return [f[:-5] for f in os.listdir(folder_path) if f.endswith(".json")]  # Remove .json extension
        except Exception:
            return []

    
    
    def generate_questions(self):
        """Retrieve and display only '5' and '10' marks questions."""
        self.generated_display.delete(1.0, tk.END)  

        selected_file = self.fileNameEntry.get()

        if not selected_file:
            self.generated_display.insert(tk.END, "No file selected. Please choose a file.\n")
            return

        # Get file path
        current_folder_path = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_folder_path, "..", "data", "Questions")
        file_path = os.path.join(folder_path, f"{selected_file}.json")

        if not os.path.exists(file_path):
            self.generated_display.insert(tk.END, "Selected file does not exist.\n")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                questions_data = json.load(f)
        except json.JSONDecodeError:
            self.generated_display.insert(tk.END, "Error: Invalid JSON format in the selected file.\n")
            return

        # Display questions (Only 5 and 10 Marks)
        for unit, unit_data in questions_data.items():
            self.generated_display.insert(tk.END, f"Unit: {unit}\n", 'header')
            self.generated_display.insert(tk.END, "-" * 50 + "\n")

            # Get only "5 Marks" and "10 Marks" questions
            five_marks_questions = unit_data.get("5", [])
            ten_marks_questions = unit_data.get("10", [])

            # Select two "5 Marks" questions
            if len(five_marks_questions) >= 2:
                selected_five = random.sample(five_marks_questions, 2)
                # self.generated_display.insert(tk.END, "5 Marks Question:\n")
                self.generated_display.insert(tk.END, f"  a) {selected_five[0]['question']}\n")
                self.generated_display.insert(tk.END, f"  b) {selected_five[1]['question']}\n\n")
            elif len(five_marks_questions) == 1:
                # self.generated_display.insert(tk.END, "5 Marks Question:\n")
                self.generated_display.insert(tk.END, f"  a) {five_marks_questions[0]['question']}\n")
                self.generated_display.insert(tk.END, f"  b) (Not enough questions available)\n\n")

            # Select one "10 Marks" question
            if ten_marks_questions:
                selected_ten = random.choice(ten_marks_questions)
                self.generated_display.insert(tk.END, f"{selected_ten['question']}\n\n")

        self.generated_display.insert(tk.END, "-" * 50 + "\n")
        

    def save_to_word(self):
        """Save the displayed questions to a Word document as a table."""
        text_content = self.generated_display.get(1.0, tk.END)

        if text_content.strip() == "":
            messagebox.showwarning("No Content", "There are no generated questions to save.")
            return

        current_folder = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_folder, "..", "data")

        if not os.path.exists(json_file_path):
                os.makedirs(json_file_path)

        file_path = os.path.join(json_file_path, 'collegeName.json')

            # Load College Name from JSON safely
        get_college_name = "Default College"
        if os.path.exists(file_path):
            try:
                    with open(file_path, "r") as file:
                        data = json.load(file)
                        get_college_name = data.get("CollegeName", "Default College")
            except json.JSONDecodeError:
                    print("Error: Invalid JSON format. Using default college name.")
            
        college_name = get_college_name  
        year = self.year.get()
        semester = self.semester.get()
        branch = self.branch.get()
        subject = self.subject.get()
        date = self.date.get()
        marks = self.marks.get()
        ModeOFExamCombobox = self.ModeOFExamCombobox.get()
        if not all([college_name, year, semester, branch, subject , marks , date , ModeOFExamCombobox]):
            messagebox.showwarning("Missing Information", "Please fill in all the details before saving.")
            return

        # Ask for save location
        save_file_path = filedialog.asksaveasfilename(
            title="Save Generated Question Paper",
            defaultextension=".docx",
            filetypes=(("Word Documents", "*.docx"), ("All Files", "*.*")))

        if not save_file_path:
            # print("Save file path is None, operation canceled.")
            return

        try:
            doc = Document()

            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(current_folder_path, "..", "utils", "Gpcet_logo.png")

            # Check if the image exists at the specified location
            if os.path.exists(logo_path):
                
                doc.add_picture(logo_path, width=Inches(1))
            else:
                messagebox.showerror("Error", f"Logo image not found at: {logo_path}")
                return

            # Add the college name and exam details as header
            title_paragraph = doc.add_paragraph()
            title_paragraph.alignment = 1  # Center align the paragraph
            title_paragraph.add_run(college_name + "\n").bold = True
            title_paragraph.add_run("(Autonomous)"+ "\n").bold = True
            title_paragraph.add_run(f"Year: {year} | Semester: {semester} | {ModeOFExamCombobox}\n")
            sub_title = doc.add_paragraph()
            sub_title.add_run(f"Branch: {branch}                                                                           Date : {date}\n")
            sub_title.add_run(f"Subject: {subject}                                                               \t\t           Max Marks: {marks}")

            doc.add_paragraph('-' * 100)  # Add a separator

            # Add a table with headers
            table = doc.add_table(rows=1, cols=4)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = "Question"
            hdr_cells[1].text = "Marks"
            hdr_cells[2].text = "CO"
            hdr_cells[3].text = "Cognitive Level"
            
            table.columns[0].width = Inches(4)
            # table.columns[1].width = Inches(1)
            hdr_cells[1].width = Inches(1)
            table.columns[2].width = Inches(1)
            table.columns[3].width = Inches(1)
            # for i in range(1, 4): 
            #     for cell in table.columns[i].cells:
            #         cell.width = Inches(1) 

            selected_file = self.fileNameEntry.get()
            if not selected_file:
                messagebox.showwarning("No File Selected", "Please select a file to save.")
                return

            folder_path = os.path.join(current_folder_path, "..", "data", "Questions")
            file_path = os.path.join(folder_path, f"{selected_file}.json")
            
            # print(f"Attempting to open file: {file_path}")

            if not os.path.exists(file_path):
                self.generated_display.insert(tk.END, "Selected file does not exist.\n")
                return

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    questions_data = json.load(f)
            except json.JSONDecodeError:
                self.generated_display.insert(tk.END, "Error: Invalid JSON format in the selected file.\n")
                return

            for unit, unit_data in questions_data.items():
                # Process 5 marks questions
                five_marks_questions = unit_data.get("5", [])
                for q in five_marks_questions:
                    row_cells = table.add_row().cells
                    row_cells[0].text = q.get('question', '')
                    row_cells[1].text = "5 Marks"
                    row_cells[3].text = q.get('bt' , '')

                # Process 10 marks questions
                ten_marks_questions = unit_data.get("10", [])
                for q in ten_marks_questions:
                    row_cells = table.add_row().cells
                    row_cells[0].text = q.get('question', '')
                    row_cells[1].text = "10 Marks"
                    row_cells[3].text = q.get('bt' , '')
                    

            # Save the document
            # print(f"Saving document to: {save_file_path}")
            doc.save(save_file_path)
            messagebox.showinfo("Saved", f"Questions saved to Word document at {save_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
