import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title("B/W to RGB Image Converter")

canvas = Canvas(height="700", width="1000")

canvas.create_text(500, 30, text="Black and White to Colored Image Converter", font=('Helvetica', 30, 'bold'))
canvas.create_text(500, 60, text="Project 3 by Team 12: Sam Aldeguer, Ben Crocker, Peter Lee, Jordan Cedeno", font=('Helvetica', 15))

def upload():
    global img
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    file_label = Label(root, text=root.filename).pack()
    img = Image.open(root.filename)
    img = img.resize((200,200))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img).pack()

uploadButton = Button(root, text="Upload image", width=18, height=5, bd='10', command=upload)
uploadButton.place(x=415, y=75)


canvas.pack()

root.mainloop()
