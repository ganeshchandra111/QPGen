# QPGen - Question Paper Generator

A desktop-based application built with Python and Tkinter for creating, editing, and managing question papers and multiple-choice questions (MCQs). QPGen provides educators with a structured environment to generate assessments efficiently and with greater accuracy.

## 🎯 Overview

QPGen is designed to simplify the question paper preparation process for educators. It reduces the need for manual formatting, supports question organization, and promotes consistency across exams. The application is suitable for use in schools, colleges, and training institutions.

## ✨ Features

- **Create Questions**: Add descriptive questions with units, marks, and Bloom's taxonomy classification
- **Generate Questions**: Automatically generate question papers for mid-semester and semester exams
- **Edit Questions**: Modify existing questions in your question bank
- **Create MCQs**: Add multiple-choice questions with multiple options
- **Generate MCQs**: Automatically generate MCQ sets from your question bank
- **Edit MCQs**: Modify existing MCQs and their options
- **Export Functionality**: Save question papers to Word documents
- **Question Organization**: Organize questions by subject, unit, and difficulty level
- **User-Friendly Interface**: Clean and intuitive GUI with sidebar navigation

## 📋 Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- Additional dependencies (if any) should be listed in requirements.txt

## 📖 How to Use

### Creating Questions

1. Navigate to the "Create Questions" page
2. Select or create a subject file to store questions
3. Choose the unit from the dropdown menu
4. Select marks and Bloom's taxonomy level
5. Type your question in the text box
6. Click "Save Question"

### Generating Questions

1. Go to the "Generate Questions" page
2. Enter exam details (Year, Semester, Branch, Subject, Date, Max Marks)
3. Select exam mode (Mid/Semester) from dropdown
4. Choose the subject file from the dropdown
5. Click "Generate Questions"
6. Edit questions if needed (changes won't be saved to the original file)
7. Click "Save to Word" to export the question paper

### Editing Questions

1. Open the "Edit Questions" page
2. Select the subject you want to edit
3. Click "Open File" to load all questions
4. Browse through questions and choose to edit or delete
5. Use the edit button to modify questions
6. Changes are automatically saved to the question bank

### Creating MCQs

1. Navigate to "Create MCQs" page
2. Select or create a subject for storing MCQs
3. Choose the unit from the dropdown
4. Type the question and options
5. Click "Add Question" to save the MCQ

### Generating MCQs

1. Go to "Generate MCQs" page
2. Select the file to generate questions from
3. Click "Generate MCQs" to create 20 MCQs
4. Edit questions if needed
5. Save to Word document or create a question bank

### Editing MCQs

1. Open "Edit MCQs" page
2. Select the file containing MCQs to edit
3. Click "Load Questions" to view all MCQs
4. Select a question to edit or delete
5. Make changes and save or delete as needed

## 🎨 Interface Features

- **Sidebar Navigation**: Easy access to all features
- **Responsive Design**: Clean and modern interface
- **Scrollable Content**: Handle large amounts of content efficiently
- **Color-Coded Interface**: Visual consistency throughout the application


## 🙏 Acknowledgments

- Built with Python and Tkinter
- Designed for educational institutions
- Created to simplify the question paper generation process

---

**Note**: Make sure to have all required dependencies installed before running the application. The application creates and manages question banks locally on your system.
