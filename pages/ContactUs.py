from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

class ContactUs(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        # Set background color and style
        self.configure(bg="#f0f0f0")
        
        # Title Label
        title_label = Label(
            self,
            text="Contact Us",
            font=("Arial", 20, "bold"),
            fg="#333333",
            bg="#f0f0f0"
        )
        title_label.pack(pady=20)

        # Team Details
        team_members = [
            {"name": "Ganesh chandra", "role": "Project Manager", "email": "ganeshchandracodes@gmail.com"},
            {"name": "Kategar Ganesh", "role": "Developer", "email": "ganeshkategar23@gmail.com"},
            {"name": "Prasad", "role": "Developer", "email": "venkatdurgaprasad4@gmail.com"},
            {"name": "Jaya Deep", "role": "UI/UX Designer", "email": "karanamjayadeep@gmail.com"},
        ]

        # Developer cards
        for member in team_members:
            self.create_developer_card(member)
        
        # Footer label
        footer_label = Label(
            self,
            text="We'd love to hear from you! Reach out with any questions.",
            font=("Arial", 12),
            fg="#666666",
            bg="#f0f0f0",
            wraplength=400
        )
        footer_label.pack(pady=20)

    def create_developer_card(self, member):
        # Card Frame
        card_frame = Frame(self, bg="white", relief=RAISED, borderwidth=1)
        card_frame.pack(pady=10, padx=20, fill=X)

        # Name Label
        name_label = Label(
            card_frame,
            text=member["name"],
            font=("Arial", 14, "bold"),
            fg="#333333",
            bg="white"
        )
        name_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)

        # Role Label
        role_label = Label(
            card_frame,
            text=member["role"],
            font=("Arial", 12),
            fg="#666666",
            bg="white"
        )
        role_label.grid(row=1, column=0, sticky=W, padx=10)

        # Email Label
        email_label = Label(
            card_frame,
            text=f"Email: {member['email']}",
            font=("Arial", 12),
            fg="#007acc",
            bg="white",
            cursor="hand2"
        )
        email_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

        # Bind email click
        email_label.bind("<Button-1>", lambda e: self.open_email(member["email"]))

    def open_email(self, email):
        # This function opens the email client when an email is clicked
        os.system(f'start mailto:{email}')
