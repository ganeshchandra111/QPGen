from tkinter import *
import tkinter as tk

# from QPGen.pages.CreateQuestions import CreateQuestions
from pages.MainPage import MainPage
from pages.GanerateQuestions import GenerateQuestions
from pages.CreateQuestions import CreateQuestions
from pages.CreateMCQs import CreateMCQs
from pages.EditMCQs import EditMCQs
from pages.GenerateMCQs import GenerateMCQs
from pages.EditQuestions import EditQuestions


# root = Tk()
class QPGen:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x620")
        self.root.title("QPGen")
        self.root.resizable(False,False)

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

    def PageNavigationBtn(self,root,page,text):
        page1_btn = tk.Button(
            root, text=text, command=lambda: self.showPage(page)
        )
        page1_btn.pack(fill="x", pady=5,padx=10)

    def create_sidebar(self):
        # Sidebar for navigation
        self.sidebar = tk.Frame(self.root, bg="lightgray", width=100)
        self.sidebar.pack(side="left", fill="y")

        # Buttons for different counters
        self.PageNavigationBtn(self.sidebar,CreateQuestions,"Create Questions")
        self.PageNavigationBtn(self.sidebar,GenerateQuestions,"Generate Questions")
        self.PageNavigationBtn(self.sidebar,EditQuestions,"Edit Questions")
        self.PageNavigationBtn(self.sidebar,CreateMCQs,"CreateMCQs")
        self.PageNavigationBtn(self.sidebar,GenerateMCQs,"GenerateMCQs")
        self.PageNavigationBtn(self.sidebar,EditMCQs,"EditMCQs")


        back_btn = tk.Button(
            self.sidebar, text="Back", command=lambda: self.showPage(MainPage)
        )
        back_btn.pack(side="bottom",fill="x", pady=5,padx=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QPGen()
    app.run()
