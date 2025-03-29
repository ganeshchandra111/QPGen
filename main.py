import tkinter as tk
from tkinter import *


root = Tk()
root.geometry("1020x720")  # Set the size of the window

# Configure the root grid layout
root.grid_rowconfigure(0, weight=1)  # Allow resizing vertically
root.grid_columnconfigure(0, weight=1)  # Allow resizing horizontally
root.grid_columnconfigure(1, weight=4)  # Allocate more weight to the main frame

# Create the side menu frame
sideMenuFrame = tk.Frame(root, bg="lightblue", width=100)
sideFrameLable = tk.Label(sideMenuFrame, text="This is the side menu bar", bg="blue", fg="white")
sideFrameLable.pack(padx=10, pady=10,fill="both")
sideMenuFrame.grid(row=0, column=0, sticky="ns")  # Sticky 'ns' makes it stretch vertically

mainFrame = tk.Frame(root, bg="white")
mainLabel = tk.Label(mainFrame, text="This is the main Frame and Main Page", bg="white")
mainLabel.pack(padx=10, pady=10)
mainFrame.grid(row=0, column=1, sticky="nsew")  

root.mainloop()

