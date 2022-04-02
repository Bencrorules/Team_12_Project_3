import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("B/W to RGB Image Converter")

canvas = Canvas(height="10000", width="10000")

#Adds titles to the top of the GUI
title = Label(root, text="Black & White to Colored Image Converter", font=('Helvetica', 30, 'bold'))
title.pack()
names = Label(root, anchor=CENTER, text="Project 3 by Team 12: Sam Aldeguer, Ben Crocker, Peter Lee, Jordan Cedeno", font=('Helvetica', 15))
names.pack()

#Method that uploads the image from the button and places the images.
def upload():
    global img
    global new_image
    global resized_image
    global imageHeight
    global imageWidth
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpg files", "*.jpg"),("png files", "*.png"),("jpeg files", "*.jpeg"),("all files", "*.*"))) #opens file browser
    img = Image.open(root.filename) #puts image path into variable
    imageWidth,imageHeight = img.size #gets width and height of image
    resized_image = img.resize((500, (int)((imageHeight/imageWidth)*500))) #scales the image to make it fit on interface
    new_image = ImageTk.PhotoImage(resized_image) #turns image path into image
    canvas.create_image(150,300,anchor=NW, image=new_image) #adds image to GUI

uploadButton = Button(root, text="Upload image", width=18, height=5, bd='10', command=upload) #creates upload button

uploadButton.place(relx=0.5, rely=0.15, anchor=CENTER) #places upload button at top center of screen

canvas.create_text(400, 250, text="Black & White Photo", font=('Helvetica', 25, 'bold')); #Black & White photo label
canvas.create_text(1050, 250, text="Colored", font=('Helvetica', 25, 'bold')); #Colored photo label

canvas.pack() #Puts everything onto the GUI

root.mainloop()
