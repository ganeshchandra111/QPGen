import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot, bg="#f7f9fa")

        # Title
        title = tk.Label(
            self,
            text="📄 Question Paper Generator",
            font=("Segoe UI", 20, "bold"),
            fg="#2c3e50",
            bg="#f7f9fa"
        )
        title.pack(pady=(40, 10))

        # Tagline
        tagline = tk.Label(
            self,
            text="Easily create, manage, and generate exam papers",
            font=("Segoe UI", 12, "italic"),
            fg="#7f8c8d",
            bg="#f7f9fa"
        )
        tagline.pack(pady=(0, 30))

        # Features
        features_text = (
            "✨ What this software does:\n\n"
            "• Create and edit your own subject-wise question banks\n"
            "• Generate Mid-I, Mid-II, and Semester papers automatically\n"
            "• Supports 2-mark, 5-mark, and 10-mark questions\n"
            "• Export generated papers to Word for printing"
        )
        features = tk.Label(
            self,
            text=features_text,
            font=("Segoe UI", 11),
            fg="#34495e",
            bg="#f7f9fa",
            justify="left"
        )
        features.pack(padx=40, anchor="w")

        # Footer
        footer = tk.Label(
            self,
            text="Use the menu to navigate (Create, Generate, Edit, Help).",
            font=("Segoe UI", 10),
            fg="#95a5a6",
            bg="#f7f9fa"
        )
        footer.pack(side="bottom", pady=20)
