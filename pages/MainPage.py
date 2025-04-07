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
        super().__init__(parentRoot)

        self.lable = Label(self, text=''' This is the main page ''')
        self.lable.pack(padx=10,pady=10)

        self.MainPageFrame = Frame(self)


        self.CollegeNameFrame = tk.Frame(self.MainPageFrame) #THsi is a Frame for collge name entry 
        self.collegeName = tk.Entry(self.CollegeNameFrame,width=100)
        self.collegeNameButton = tk.Button(self.CollegeNameFrame, text="Submit College Name",command=self.show_name)

        # Packing the widgets
        self.collegeName.grid(row=0,column=0,padx=10,pady=10)
        self.collegeNameButton.grid(row=0, column=1,padx=10, pady=10)
        self.CollegeNameFrame.pack(padx=10,pady=10)

        self.CollegeLogoFrame = tk.Frame(self.MainPageFrame)
    
        self.collegeLogoLable = Label(self.CollegeLogoFrame, text="Selcet your college Logo")
        self.collegeLogo = Button(self.CollegeLogoFrame, text="Select Logo", command=self.open_file )
        self.image_label = Label(self.CollegeLogoFrame)
        self.collegeLogoLable.grid(row=0,column=0)
        self.collegeLogo.grid(row=0, column=1)
        self.image_label.grid(row=1,column=0,pady=10)
        self.CollegeLogoFrame.pack()
        
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






