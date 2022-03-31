import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title("B/W to RGB Image Converter")
root.attributes('-fullscreen', True)


canvas = Canvas(height="10000", width="10000")

canvas.create_text(715, 30, text="Black & White to Colored Image Converter", font=('Helvetica', 30, 'bold'))
canvas.create_text(715, 60, text="Project 3 by Team 12: Sam Aldeguer, Ben Crocker, Peter Lee, Jordan Cedeno", font=('Helvetica', 15))
def upload():
    global img
    global new_image
    global imageHeight
    global imageWidth
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpg files", "*.jpg"),("png files", "*.png"),("jpeg files", "*.jpeg"),("all files", "*.*")))
    img = Image.open(root.filename)
    new_image = ImageTk.PhotoImage(img)
    imageHeight = new_image.height()
    imageWidth = new_image.width()
    canvas.create_image(150,300,anchor=NW, image=new_image)

uploadButton = Button(root, text="Upload image", width=18, height=5, bd='10', command=upload)
uploadButton.place(x=610, y=75)

canvas.create_text(400, 250, text="Black & White Photo", font=('Helvetica', 25, 'bold'));
canvas.create_text(1050, 250, text="Colored", font=('Helvetica', 25, 'bold'));

canvas.pack()

root.mainloop()
