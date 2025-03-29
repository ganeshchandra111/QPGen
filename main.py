from tkinter import *
import tkinter as tk

from pages.CreatePage import CreatePage
from pages.MainPage import MainPage
from pages.GanerateQuestions import GenerateQuestions


# root = Tk()
class QPGen:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1020x720")
        self.root.title("QPGen")

        self.currentPage = None
        self.showPage(MainPage)

        self.create_sidebar()

    def showPage(self, page_class):
        # Clear the current frame
        if self.currentPage is not None:
            self.currentPage.destroy()

        # Create a new page
        self.currentPage = page_class(self.root)
        self.currentPage.pack(side="right", fill="both", expand=True)

    def create_sidebar(self):
        # Sidebar for navigation
        self.sidebar = tk.Frame(self.root, bg="lightgray", width=100)
        self.sidebar.pack(side="left", fill="y")

        # Buttons for different counters
        page1_btn = tk.Button(
            self.sidebar, text="Page 1", command=lambda: self.showPage(CreatePage)
        )
        page1_btn.pack(fill="x", pady=5)

        page2_btn = tk.Button(
            self.sidebar, text="Page 2", command=lambda: self.showPage(GenerateQuestions)
        )
        page2_btn.pack(fill="x", pady=5)

        back_btn = tk.Button(
            self.sidebar, text="Back", command=lambda: self.showPage(MainPage)
        )
        back_btn.pack(side="bottom",fill="x", pady=5)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QPGen()
    app.run()
