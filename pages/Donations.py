import tkinter as tk
from PIL import Image, ImageTk  # Ensure you have Pillow installed: pip install pillow

class Donations(tk.Frame):
    def __init__(self, parentRoot):
        super().__init__(parentRoot)

        self.configure(bg="#f9f9f9")  # Light grey background

        # Title Label
        self.title_label = tk.Label(
            self,
            text="Support Us - Scan to Donate",
            font=("Arial", 20, "bold"),
            bg="#f9f9f9",
            fg="#333333"  # Dark grey text
        )
        self.title_label.pack(pady=20)

        # QR Code Image
        self.qr_image = Image.open("D:/_PROJECTS/QPGen/QPGen/utils/QR.jpg")
        self.qr_image = self.qr_image.resize((300, 300))  # Resize to fit the frame
        self.qr_photo = ImageTk.PhotoImage(self.qr_image)

        self.qr_label = tk.Label(self, image=self.qr_photo, bg="#f9f9f9")
        self.qr_label.pack(pady=20)

        # Instruction Label
        self.instruction_label = tk.Label(
            self,
            text="Scan the QR code with your PhonePe app to donate.",
            font=("Arial", 12),
            bg="#f9f9f9",
            fg="#555555"  # Medium grey text
        )
        self.instruction_label.pack(pady=10)
