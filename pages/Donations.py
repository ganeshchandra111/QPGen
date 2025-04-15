import tkinter as tk
import webbrowser  # To open Razorpay links in the browser


class Donations(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.configure(bg="#f9f9f9")  # Light grey background

        # Persuasive Text Label
        self.title_label = tk.Label(
            self,
            text=(
                "🌟 Be a Part of Something Bigger! 🌟\n\n"
                "Your donation is more than just financial support—it's an investment in a future brimming with "
                "possibilities. Together, we can create tools and solutions that impact lives and drive change.\n\n"
                "Every step forward is powered by your generosity. Whether it's a small gesture or a big contribution, "
                "you are helping us lay the foundation for innovation and growth.\n\n"
                "Click below to join our journey and leave your legacy. The future starts here!"
            ),
            font=("Arial", 14),
            bg="#f9f9f9",
            fg="#333333",  # Dark grey text
            wraplength=500,
            justify="center"
        )
        self.title_label.pack(pady=20)

        # Donate Now Button
        self.donate_button = tk.Button(
            self,
            text="Donate Now",
            font=("Arial", 14, "bold"),
            bg="#28a745",  # Green background
            fg="white",  # White text
            relief="raised",
            cursor="hand2",
            command=self.open_razorpay_link
        )
        self.donate_button.pack(pady=20, ipadx=20, ipady=10)

    def open_razorpay_link(self):
        """
        Opens the Razorpay payment page.
        """
        razorpay_base_url = "https://razorpay.me/@wowfour"  # Replace with your Razorpay payment link
        webbrowser.open(razorpay_base_url)
