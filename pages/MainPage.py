import tkinter as tk
from tkinter import Label, Frame

class MainPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot, bg="#f7f9fa")

        # Title Label
        self.label = Label(
            self,
            text="QPGen",
            font=("Segoe UI", 16, "bold"),
            fg="#2c3e50",
            bg="#f7f9fa"
        )
        self.label.pack(padx=10, pady=20)

        # Info Frame
        self.infoFrame = Frame(self, bg="#f7f9fa")

        overview_heading = ("Overview\n")
        overview_text = (
            "QPGen is a desktop-based application developed to facilitate the creation, editing,\n"
            "and management of question papers and multiple-choice questions. It provides a structured\n"
            "environment for educators to generate assessments efficiently and with greater accuracy.\n"
        )

        purpose_heading = ("Purpose\n")
        purpose_text = (
            "The application is designed to simplify the question paper preparation process. It reduces\n"
            "the need for manual formatting, supports question organization, and promotes consistency across exams.\n"
            "QPGen is suitable for use in schools, colleges, and training institutions.\n"
        )

        features_heading = ("Features\n")
        features_text = (
            "- Create and edit descriptive questions\n"
            "- Create and manage multiple-choice questions (MCQs)\n"
            "- Automatically generate question sets from a database\n"
            "- Organize questions by subject, topic, and difficulty level\n"
            "- Export question papers for printing or digital use\n"
        )

        # OVERVIEW SECTION
        self.overview = Label(
            self.infoFrame,
            text=overview_heading,
            font=("Segoe UI", 12, "bold"),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )
        self.overview_text = Label(
            self.infoFrame,
            text=overview_text,
            font=("Segoe UI", 12),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )

        self.overview.pack(padx=20, anchor="w")
        self.overview_text.pack(padx=40, pady=(0, 20), anchor="w")

        # PURPOSE SECTION
        self.purpose = Label(
            self.infoFrame,
            text=purpose_heading,
            font=("Segoe UI", 12, "bold"),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )
        self.purpose_text = Label(
            self.infoFrame,
            text=purpose_text,
            font=("Segoe UI", 12),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )

        self.purpose.pack(padx=20, anchor="w")
        self.purpose_text.pack(padx=40, pady=(0, 20), anchor="w")

        # FEATURES SECTION
        self.features = Label(
            self.infoFrame,
            text=features_heading,
            font=("Segoe UI", 12, "bold"),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )
        self.features_text = Label(
            self.infoFrame,
            text=features_text,
            font=("Segoe UI", 12),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left",
            anchor="w"
        )

        self.features.pack(padx=20, anchor="w")
        self.features_text.pack(padx=40, pady=(0, 20), anchor="w")

        self.infoFrame.pack(fill="both", expand=True, padx=20, pady=10)
