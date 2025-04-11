import webbrowser
from tkinter import *
import tkinter as tk


class Donations(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.configure(bg="#f9f9f9")  # Light grey background

        # Title Label
        self.title_label = Label(
            self,
            text="Support Us - Donations Page",
            font=("Arial", 20, "bold"),
            bg="#f9f9f9",
            fg="#333333"  # Dark grey text
        )
        self.title_label.pack(pady=20)

        # Description Label
        self.desc_label = Label(
            self,
            text="Your support helps us keep going! Donate securely using Razorpay or share your details via Google Form.",
            font=("Arial", 12),
            bg="#f9f9f9",
            fg="#555555",  # Medium grey text
            wraplength=450,
            justify="center"
        )
        self.desc_label.pack(pady=10)

        # Razorpay Donate Button
        self.razorpay_button = Button(
            self,
            text="Donate with Razorpay",
            font=("Arial", 14, "bold"),
            bg="#2a9d8f",  # Teal green
            fg="white",
            relief="raised",
            cursor="hand2",
            command=self.open_razorpay_link
        )
        self.razorpay_button.pack(pady=15, ipadx=10, ipady=5)

        # Google Form Button
        self.google_form_button = Button(
            self,
            text="Fill Google Form",
            font=("Arial", 14, "bold"),
            bg="#264653",  # Deep greenish-blue
            fg="white",
            relief="raised",
            cursor="hand2",
            command=self.open_google_form
        )
        self.google_form_button.pack(pady=15, ipadx=10, ipady=5)

        # Suggested Donation Amounts Label
        self.donation_label = Label(
            self,
            text="Suggested Donation Amounts:",
            font=("Arial", 14, "bold"),
            bg="#f9f9f9",
            fg="#333333"
        )
        self.donation_label.pack(pady=20)

        # Donation Buttons Frame
        donation_frame = Frame(self, bg="#f9f9f9")
        donation_frame.pack(pady=10)

        # Suggested Donation Buttons
        prices = [50, 100, 250, 500, 1000]
        for price in prices:
            btn = Button(
                donation_frame,
                text=f"₹ {price}",
                font=("Arial", 12),
                bg="#457b9d",  # Muted blue
                fg="white",
                # relief="raised",
                cursor="hand2",
                command=lambda p=price: self.open_razorpay_link(p)
            )
            btn.pack(side=LEFT, padx=10, pady=5, ipadx=5, ipady=5)

    def open_razorpay_link(self, amount=None):
        """
        Opens the Razorpay payment link.
        Optionally appends the donation amount if provided.
        """
        base_url = "https://rzp.io/l/YOUR_RAZORPAY_LINK"  # Replace with your Razorpay link
        if amount:
            webbrowser.open(f"{base_url}?amount={amount*100}")  # Razorpay amount is in paise
        else:
            webbrowser.open(base_url)

    def open_google_form(self):
        """
        Opens the Google Form link in the browser.
        """
        google_form_url = "https://forms.gle/YOUR_GOOGLE_FORM_LINK"  # Replace with your Google Form link
        webbrowser.open(google_form_url)

