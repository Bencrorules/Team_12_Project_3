import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("B/W to RGB Image Converter")

canvas = Canvas(height="700", width="1000")

canvas.create_text(500, 30, text="Black and White to Colored Image Converter", font=('Helvetica', 30, 'bold'))
canvas.create_text(500, 60, text="Project 3 by Team 12: Sam Aldeguer, Ben Crocker, Peter Lee, Jordan Cedeno", font=('Helvetica', 15))
uploadButton = Button(root, text="Upload image", width=18, height=5, bd='10')
uploadButton.place(x=415, y=75)

canvas.pack()

root.mainloop()
