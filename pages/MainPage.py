import shutil
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os
import json
from PIL import Image, ImageTk


class MainPage(tk.Frame):

    def show_name(self):
        name = self.collegeName.get()

        # Get the current script's folder path
        current_folder_path = os.path.dirname(os.path.abspath(__file__))

        # Define the relative path to the data folder
        data_folder_path = os.path.join(current_folder_path, '..', 'data')

        # Ensure the data folder exists; create it if it doesn't
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

        # Define the path for the JSON file
        file_path = os.path.join(data_folder_path, 'collegeName.json')

        # Save the data to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump({'CollegeName': name}, json_file, indent=4)

        print(f"Data saved to {file_path}")

    def __init__(self, parentRoot):
        super().__init__(parentRoot, bg="#f7f9fa")

        self.lable = Label(
            self,
            text="🏫 Welcome to the Main Page",
            font=("Segoe UI", 16, "bold"),
            fg="#2c3e50",
            bg="#f7f9fa"
        )
        self.lable.pack(padx=10, pady=20)

        self.MainPageFrame = Frame(self, bg="#f7f9fa")

        # College Name Entry Frame
        self.CollegeNameFrame = tk.Frame(self.MainPageFrame, bg="#f7f9fa")
        self.collegeName = tk.Entry(self.CollegeNameFrame, width=60, font=("Segoe UI", 10))
        self.collegeNameButton = tk.Button(
            self.CollegeNameFrame,
            text="Submit College Name",
            font=("Segoe UI", 9, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            relief="flat",
            command=self.show_name
        )

        self.collegeName.grid(row=0, column=0, padx=10, pady=10)
        self.collegeNameButton.grid(row=0, column=1, padx=10, pady=10)
        self.CollegeNameFrame.pack(padx=10, pady=10)

        # College Logo Frame
        self.CollegeLogoFrame = tk.Frame(self.MainPageFrame, bg="#f7f9fa")
        self.collegeLogoLable = Label(
            self.CollegeLogoFrame,
            text="🎓 Select Your College Logo",
            font=("Segoe UI", 10),
            bg="#f7f9fa",
            fg="#2c3e50"
        )
        self.collegeLogo = Button(
            self.CollegeLogoFrame,
            text="Browse",
            command=self.open_file,
            font=("Segoe UI", 9, "bold"),
            bg="#2ecc71",
            fg="white",
            activebackground="#27ae60",
            relief="flat"
        )
        self.image_label = Label(self.CollegeLogoFrame, bg="#f7f9fa")

        self.collegeLogoLable.grid(row=0, column=0, padx=5, pady=10)
        self.collegeLogo.grid(row=0, column=1, padx=10, pady=10)
        self.image_label.grid(row=1, column=0, columnspan=2, pady=10)
        self.CollegeLogoFrame.pack()

        # Show Questions
        self.QuestionsShowcaseFrame = Frame(self.MainPageFrame, bg="#f7f9fa")
        self.QuestionsShowcaseLable = Label(
            self.QuestionsShowcaseFrame,
            text="📚 View All Questions",
            font=("Segoe UI", 10, "bold"),
            bg="#f7f9fa",
            fg="#34495e"
        )
        self.QuestionsShowcaseLable.grid(row=0, column=0, pady=10)
        self.showAllUserCreatedQuestionPapers(self.getAllFilesFromFolder('Questions'), self.QuestionsShowcaseFrame)
        self.QuestionsShowcaseFrame.pack(pady=10)

        # Show MCQs
        self.MCQShowcaseFrame = Frame(self.MainPageFrame, bg="#f7f9fa")
        self.MCQShowcaseLable = Label(
            self.MCQShowcaseFrame,
            text="📝 All Created MCQs",
            font=("Segoe UI", 10, "bold"),
            bg="#f7f9fa",
            fg="#34495e"
        )
        self.MCQShowcaseLable.grid(row=0, column=0, pady=10)
        self.showAllUserCreatedQuestionPapers(self.getAllFilesFromFolder('MCQs'), self.MCQShowcaseFrame)
        self.MCQShowcaseFrame.pack(pady=10)

        self.MainPageFrame.pack()
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            initialdir="/",
            title="Select File",
            filetypes=(("Image Files", "*.jpg *.png"),)
        )

        if file_path:
            try:
                # Get the current script's folder path
                current_folder_path = os.path.dirname(os.path.abspath(__file__))

                # Define the relative path to the logos folder inside /data
                logos_folder_path = os.path.join(current_folder_path, '..', 'data', 'logos')

                # Ensure the logos folder exists; create it if it doesn't
                if not os.path.exists(logos_folder_path):
                    os.makedirs(logos_folder_path)

                # Extract the file name from the selected path
                file_name = os.path.basename(file_path)

                # Define the destination path
                destination_path = os.path.join(logos_folder_path, file_name)

                # Copy the selected image to the destination
                shutil.copy(file_path, destination_path)

                print(f"Logo saved to: {destination_path}")


                image = Image.open(destination_path)
                image = image.resize((200, 200))  # Resize for preview
                photo = ImageTk.PhotoImage(image)

                self.image_label.configure(image=photo)
                self.image_label.image = photo  

            except Exception as e:
                print(f"Error handling image file: {e}")

    def getAllFilesFromFolder(self,folder):

        try:
            current_folder_path = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_folder_path, '..', 'data', folder)
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
    

    def showAllUserCreatedQuestionPapers(self, array, frame):
        count = 0
        for i in array:
            displayText = i[0:4] + "..."

            button = tk.Button(
                frame,
                text=displayText,
                width=6,
                height=2,
                font=("Segoe UI", 12, "bold"),
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                activeforeground="white",
                relief="flat",
                cursor="hand2"
            )
            button.grid(row=1, column=count, padx=10, pady=10)
            count += 1






































































