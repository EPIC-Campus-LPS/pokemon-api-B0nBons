import tkinter as tk
from PIL import ImageTk
# Import needed libraries

class PokemonView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.name_label = tk.Label(text="", font=("Helvetica", 20), master=master)
        self.name_label.grid(row=0, column=0)

        # Image label
        self.image_label = tk.Label(master=master)
        self.image_label.grid(row=1, column=0)

        # Make a frame where the buttons will sit
        self.frame = tk.Frame(master=master)
        self.frame.grid(row=2, column=0, pady=10)

        # Finally figured out how to add buttons
        self.prev_button = tk.Button(text="Previous", master=self.frame)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(text="Next", master=self.frame)
        self.next_button.grid(row=0, column=1, padx=5)


    def set_label(self, text):
        self.name_label.config(text=str(text))

    def set_image(self, pil_image):
        # set image so that its compatible with ImageTK
        self._photo_image = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=self._photo_image)

    def set_next_callback(self, callback):
        # Callbacks are essentially functions that take other functions as arguments then runs it
        # This was the only way I could figure out how to make the GUI refresh with the new pokemon
        self.next_button.config(command=callback)

    def set_prev_callback(self, callback):
        self.prev_button.config(command=callback)
