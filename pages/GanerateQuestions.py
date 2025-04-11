from tkinter import *
import tkinter as tk
import json
import os
import random
from tkinter import ttk
from docx import Document
from tkinter import filedialog
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
        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_folder_path, "..", "data", "Questions")

            if not os.path.exists(folder_path):
                return []

            return [f[:-5] for f in os.listdir(folder_path) if f.endswith(".json")]  
        except Exception:
            return []
    
    def generate_questions(self):
        self.generated_display.delete(1.0, tk.END)

        selected_file = self.fileNameEntry.get()
        if not selected_file:
            self.generated_display.insert(tk.END, "No file selected. Please choose a file.\n")
            return

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

        mode = self.ModeOFExamCombobox.get()
        units = list(questions_data.keys())

        if mode == "SEM":
            if len(units) != 5:
                self.generated_display.insert(tk.END, "SEM Mode requires exactly 5 units.\n")
                return

            # ----------- Part A (2 Marks) ------------
            self.generated_display.insert(tk.END, f"Part - A\n")
            self.generated_display.insert(tk.END, "1. Answer all the following questions (2 Marks Each)\n")

            combined_two_mark_questions = []

            for unit_data in questions_data.values():
                unit_questions = unit_data.get("2", [])
                if not unit_questions:
                    continue
                count = 2 if len(unit_questions) >= 2 else 1
                selected = random.sample(unit_questions, count)
                combined_two_mark_questions.extend([q['question'] for q in selected])

            if len(combined_two_mark_questions) < 5:
                self.generated_display.insert(tk.END, "Not enough 2-mark questions across units.\n")
                return

            random.shuffle(combined_two_mark_questions)
            sub_labels = ['a)', 'b)', 'c)', 'd)', 'e)']
            for idx in range(5):
                self.generated_display.insert(tk.END, f"{sub_labels[idx]} {combined_two_mark_questions[idx]}\n")

            # ---------- Part B ------------
            question_number = 2
            or_after = [1, 3, 5, 7, 9]

            for unit_index, (unit, unit_data) in enumerate(questions_data.items()):
                self.generated_display.insert(tk.END, f"\nUnit: {unit}\n", 'header')
                self.generated_display.insert(tk.END, "-" * 50 + "\n")

                five_pool = unit_data.get("5", [])
                ten_pool = unit_data.get("10", [])
                unit_questions = []

                # Randomly choose between paired 5-mark or 10-mark question for the first question
                if five_pool and ten_pool:
                    first_question_type = random.choice([5, 10])
                    if first_question_type == 5:
                        # Select a paired 5-mark question (a + b)
                        pair = random.sample(five_pool, 2)
                        combined = f"a) {pair[0]['question']}\n   b) {pair[1]['question']}"
                        unit_questions.append(combined)
                    else:
                        # Select a 10-mark question
                        unit_questions.append(random.choice(ten_pool)['question'])
                elif five_pool:
                    # Only 5-mark questions available
                    pair = random.sample(five_pool, 2)
                    combined = f"a) {pair[0]['question']}\n   b) {pair[1]['question']}"
                    unit_questions.append(combined)
                elif ten_pool:
                    # Only 10-mark questions available
                    unit_questions.append(random.choice(ten_pool)['question'])

                # Randomly select the second question (either 5-mark or 10-mark)
                if len(unit_questions) < 1:
                    continue  # Skip if we can't select the first question

                if len(unit_questions) < 2:
                    if five_pool:
                        pair = random.sample(five_pool, 2)
                        combined = f"a) {pair[0]['question']}\n   b) {pair[1]['question']}"
                        unit_questions.append(combined)
                    elif ten_pool:
                        unit_questions.append(random.choice(ten_pool)['question'])

                if len(unit_questions) < 2:
                    self.generated_display.insert(tk.END, "Not enough questions in this unit.\n")
                    continue

                selected = random.sample(unit_questions, 2)
                for q in selected:
                    self.generated_display.insert(tk.END, f"{question_number}. {q}\n\n")
                    if question_number in or_after:
                        self.generated_display.insert(tk.END, "                               or           \n\n")
                    question_number += 1

        elif mode in ["Mid-I", "Mid-II"]:
            if len(units) not in [2, 3]:
                self.generated_display.insert(tk.END, "Mid exam requires 2 or 3 units.\n")
                return
            
            check_units = questions_data.items()
            # Make sure there are at least 2 or 3 units
            num_units = len(check_units)
 
            unit_names = list(questions_data.keys())
            question_number = 1
            unit_distribution = []

            if num_units == 2:
                unit_distribution = [unit_names[0]] * 2 + [unit_names[1]] * 2 + random.choices(unit_names, k=2)
            elif num_units == 3:
                unit_distribution = [unit_names[0]] * 2 + [unit_names[1]] * 2 + [unit_names[2]] * 2

            self.generated_display.insert(tk.END, f"Part - B\n")

            for idx, unit in enumerate(unit_distribution):
                unit_data = questions_data.get(unit, {})
                five_mark_pool = unit_data.get("5", [])
                ten_mark_pool = unit_data.get("10", [])

                unit_questions = []

                # Create paired 5-mark question
                if len(five_mark_pool) >= 2:
                    pair = random.sample(five_mark_pool, 2)
                    combined_5marks = f"a) {pair[0]['question']}\n   b) {pair[1]['question']}"
                    unit_questions.append(combined_5marks)
                elif len(five_mark_pool) == 1:
                    unit_questions.append(f"Only one 5-mark question available: {five_mark_pool[0]['question']}")

                # Pick one 10-mark question
                if len(ten_mark_pool) >= 1:
                    ten_q = random.choice(ten_mark_pool)
                    unit_questions.append(ten_q["question"])

                if len(unit_questions) < 1:
                    self.generated_display.insert(tk.END, f"Unit {unit}: Not enough questions available.\n")
                    continue

                selected = random.choice(unit_questions)
                self.generated_display.insert(tk.END, f"{question_number}. {selected}\n\n")

                # Add "or" after 1st, 3rd, and 4th questions
                if question_number in [1, 3, 5]:
                    self.generated_display.insert(tk.END, f"{' ' * 40}or\n\n")

                question_number += 1

   
    def save_to_word(self):
        text_content = self.generated_display.get(1.0, tk.END)

        if text_content.strip() == "":
            messagebox.showwarning("No Content", "There are no generated questions to save.")
            return

        # Exam metadata
        current_folder = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_folder, "..", "data", "collegeName.json")
        college_name = "Default College"
        if os.path.exists(json_file_path):
            try:
                with open(json_file_path, "r") as file:
                    data = json.load(file)
                    college_name = data.get("CollegeName", "Default College")
            except json.JSONDecodeError:
                print("Invalid JSON. Using default college name.")

        year = self.year.get()
        semester = self.semester.get()
        branch = self.branch.get()
        subject = self.subject.get()
        date = self.date.get()
        marks = self.marks.get()
        mode = self.ModeOFExamCombobox.get()

        if not all([year, semester, branch, subject, date, marks, mode]):
            messagebox.showwarning("Missing Information", "Please fill in all the details before saving.")
            return

        save_file_path = filedialog.asksaveasfilename(
            title="Save Question Paper",
            defaultextension=".docx",
            filetypes=[("Word Documents", "*.docx")]
        )

        if not save_file_path:
            return

        try:
            doc = Document()

            # Add logo
            logo_path = os.path.join(current_folder, "..", "utils", "Gpcet_logo.png")
            if os.path.exists(logo_path):
                doc.add_picture(logo_path, width=Inches(1))

            # Header
            title = doc.add_paragraph()
            title.alignment = 1
            title.add_run(college_name + "\n").bold = True
            title.add_run("(Autonomous)\n").bold = True
            title.add_run(f"Year: {year} | Semester: {semester} | {mode}\n")

            details = doc.add_paragraph()
            details.add_run(f"Branch: {branch}                                                                       Date: {date}\n")
            details.add_run(f"Subject: {subject}                                                                     Max Marks: {marks}\n")

            doc.add_paragraph('-' * 100)

            # Process content
            lines = text_content.strip().split("\n")
            in_part_b = False
            in_part_a_sub = False
            table = None
            part_a_text = []
            question_number = 1

            for i, line in enumerate(lines):
                stripped = line.strip()

                if "Part - A" in stripped:
                    doc.add_paragraph("\nPart - A", style="Heading 2")
                    in_part_b = False
                    in_part_a_sub = False
                    continue

                elif "Part - B" in stripped:
                    # Output Part A grouped under Q1
                    if part_a_text:
                        doc.add_paragraph(part_a_text[0], style="List Number")
                        for sub in part_a_text[1:]:
                            doc.add_paragraph(sub, style="List Bullet")
                    part_a_text = []

                    doc.add_paragraph("\nPart - B", style="Heading 2")
                    in_part_b = True
                    table = doc.add_table(rows=1, cols=4)
                    table.style = 'Table Grid'
                    hdr_cells = table.rows[0].cells
                    hdr_cells[0].text = "Question"
                    hdr_cells[1].text = "Marks"
                    hdr_cells[2].text = "BT"
                    hdr_cells[3].text = "CO"
                    continue

                elif stripped.startswith("1. Answer all the following"):
                    # Collect Part A intro line
                    part_a_text.append(stripped)
                    in_part_a_sub = True
                    continue

                elif in_part_a_sub and stripped[:2] in ['a)', 'b)', 'c)', 'd)', 'e)']:
                    part_a_text.append(stripped)
                    continue

                elif stripped.startswith("Unit:"):
                    doc.add_paragraph(stripped, style="Heading 3")

                elif in_part_b and stripped and stripped[0].isdigit() and "." in stripped:
                    # It's a question in Part B
                    q_num, q_text = stripped.split(".", 1)

                    # Detect marks type
                    if "a)" in q_text and "b)" in q_text:
                        marks = "5 + 5"
                    elif "Only one" in q_text:
                        marks = "5"
                    else:
                        marks = "10"

                    # Extract BT level if present
                    bt_value = ""
                    if "Understand" in q_text:
                        bt_value = "Understand"
                    elif "Analyze" in q_text:
                        bt_value = "Analyze"
                    elif "Create" in q_text:
                        bt_value = "Create"
                    elif "Remember" in q_text:
                        bt_value = "Remember"

                    row = table.add_row().cells
                    row[0].text = q_text.strip()
                    row[1].text = marks
                    row[2].text = bt_value
                    row[3].text = ""  # CO left empty

                elif "or" in stripped.lower() and in_part_b:
                    # Add "or" as a merged and centered row in the table
                    or_row = table.add_row().cells
                    merged_cell = or_row[0].merge(or_row[1]).merge(or_row[2]).merge(or_row[3])
                    merged_cell.text = "or"
                    merged_cell.paragraphs[0].alignment = 1

                elif not in_part_b and not in_part_a_sub:
                    # General line outside parts
                    doc.add_paragraph(stripped)

            # Output Part A if not already written
            # if part_a_text:
            #     doc.add_paragraph(part_a_text[0], style="List Number")
            #     for sub in part_a_text[1:]:
            #         doc.add_paragraph(sub, style="List Bullet")

            doc.save(save_file_path)
            messagebox.showinfo("Saved", f"Document saved at:\n{save_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
