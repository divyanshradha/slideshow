import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageSlideshowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Slideshow")
        self.root.geometry("800x600")

        # Initialize variables
        self.images = []
        self.current_image_index = 0
        self.slideshow_running = False

        # Create widgets
        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True, fill='both')

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(side='bottom', fill='x')

        self.prev_button = tk.Button(self.control_frame, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side='left')

        self.next_button = tk.Button(self.control_frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side='left')

        self.start_button = tk.Button(self.control_frame, text="Start Slideshow", command=self.start_slideshow)
        self.start_button.pack(side='left')

        self.stop_button = tk.Button(self.control_frame, text="Stop Slideshow", command=self.stop_slideshow)
        self.stop_button.pack(side='left')

        self.load_button = tk.Button(self.control_frame, text="Load Images", command=self.load_images)
        self.load_button.pack(side='left')

        # Initialize slideshow timer
        self.slideshow_interval = 2000  # 2 seconds
        self.timer = None

    def load_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif")])
        self.images = [Image.open(fp) for fp in file_paths]
        if self.images:
            self.current_image_index = 0
            self.show_image()

    def show_image(self):
        if self.images:
            image = self.images[self.current_image_index]
            # Resize the image to fit the window
            image.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def show_previous_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

    def start_slideshow(self):
        if not self.slideshow_running and self.images:
            self.slideshow_running = True
            self._run_slideshow()

    def stop_slideshow(self):
        if self.slideshow_running:
            self.slideshow_running = False
            if self.timer:
                self.root.after_cancel(self.timer)

    def _run_slideshow(self):
        if self.slideshow_running and self.images:
            self.show_next_image()
            self.timer = self.root.after(self.slideshow_interval, self._run_slideshow)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSlideshowApp(root)
    root.mainloop()