import tkinter as tk
from PIL import Image, ImageTk
import time
from itertools import cycle

# Initialize the Tkinter root window
root = tk.Tk()  
root.title("Image Slide Show Viewer")

# List of image paths
image_path = [
    r"C:\Users\SS COMP\Pictures\WhatsApp Image 2024-08-08 at 20.17.18_220e9d2f.jpg",
    r"C:\Users\SS COMP\Pictures\WhatsApp Image 2024-08-08 at 20.17.18_21b4466c.jpg",
    r"C:\Users\SS COMP\Pictures\WhatsApp Image 2024-08-08 at 20.17.18_b126e815.jpg",
    r"C:\Users\SS COMP\Pictures\WhatsApp Image 2024-08-08 at 20.17.19_82f3a550_cleanup.jpg",
    r"C:\Users\SS COMP\Pictures\WhatsApp Image 2024-08-08 at 20.17.19_1dfae332_cleanup.jpg",
]

# Resize images
image_size = (1080, 1080)

# Load and resize images
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Create a label widget to display images
label = tk.Label(root)
label.pack()

# Function to update the image
def update_image():
    for photo_image in slide_show:
        label.config(image=photo_image)
        label.update()
        time.sleep(2)

# Create a cycle object for slideshow
slide_show = cycle(photo_images)

# Function to start the slideshow
def start_slide_show():
    update_image()

# Button to start the slideshow
play_button = tk.Button(root, text="Play Slide", command=start_slide_show)
play_button.pack()

# Run the Tkinter main event loop
root.mainloop()
