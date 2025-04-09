from tkinter import *
import tkinter as tk

# Page imports
from pages.MainPage import MainPage
from pages.GanerateQuestions import GenerateQuestions
from pages.CreateQuestions import CreateQuestions
from pages.CreateMCQs import CreateMCQs
from pages.EditMCQs import EditMCQs
from pages.GenerateMCQs import GenerateMCQs
from pages.EditQuestions import EditQuestions
from pages.HelpPage import HelpPage


class QPGen:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x620")
        self.root.title("QPGen")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.currentPage = None

        # Initialize sidebar first so it's not hidden later
        self.create_sidebar()

        # Load default page
        self.showPage(MainPage)

    def showPage(self, page_class):
        if self.currentPage is not None:
            self.currentPage.destroy()

        self.currentPage = page_class(self.root)
        self.currentPage.pack(side="right", fill="both", expand=True)

    def PageNavigationBtn(self, root, page, text):
        btn = tk.Button(
            root,
            text=text,
            command=lambda: self.showPage(page),
            font=("Segoe UI", 10),
            bg="#ffffff",
            fg="#333333",
            activebackground="#dcdcdc",
            activeforeground="#000000",
            relief="flat",
            bd=0,
            padx=10,
            pady=10
        )
        btn.pack(fill="x", padx=10, pady=4)

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=180)
        self.sidebar.pack(side="left", fill="y")

        # Title/Logo (optional)
        title = tk.Label(
            self.sidebar,
            text="QPGen",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#2c3e50",
            pady=20
        )
        title.pack()

        # Navigation buttons
        self.PageNavigationBtn(self.sidebar, CreateQuestions, "📝 Create Questions")
        self.PageNavigationBtn(self.sidebar, GenerateQuestions, "⚙️ Generate Questions")
        self.PageNavigationBtn(self.sidebar, EditQuestions, "✏️ Edit Questions")
        self.PageNavigationBtn(self.sidebar, CreateMCQs, "🧠 Create MCQs")
        self.PageNavigationBtn(self.sidebar, GenerateMCQs, "⚡ Generate MCQs")
        self.PageNavigationBtn(self.sidebar, EditMCQs, "🔧 Edit MCQs")
        # self.PageNavigationBtn(self.sidebar, HelpPage, "🆘 Help")

        # Back to main
        back_btn = tk.Button(
            self.sidebar,
            text="⬅️ Back to Home",
            command=lambda: self.showPage(MainPage),
            font=("Segoe UI", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief="flat",
            bd=0
        )
        back_btn.pack(side="bottom", fill="x", padx=10, pady=20)

        back_btn = tk.Button(
            self.sidebar,
            text="\t🆘 Help\t",
            command=lambda: self.showPage(HelpPage),
            font=("Segoe UI", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief="flat",
            bd=0
        )
        back_btn.pack(side="bottom", fill="x", padx=10, pady=1)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QPGen()
    app.run()
