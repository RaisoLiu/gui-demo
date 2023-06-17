import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk
from video_processing.video_loader import load_video
from video_processing.frame_selector import select_frames
from video_processing.color_replacer import replace_color

class ApplicationWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Video Color Replacer")
        
        self.frames = []
        self.selected_frames = []
        self.current_frame_index = 0
        self.color = None

        self.label = tk.Label(self)
        self.label.pack()

        self.select_video_button = tk.Button(self, text="Select Video", command=self.select_video)
        self.select_video_button.pack()

        self.select_color_button = tk.Button(self, text="Select Color", command=self.select_color)
        self.select_color_button.pack()

        self.next_frame_button = tk.Button(self, text="Next Frame", command=self.next_frame)
        self.next_frame_button.pack()

        self.modified_label = tk.Label(self)
        self.modified_label.pack()


    def select_video(self):
        filepath = filedialog.askopenfilename()
        self.frames = load_video(filepath)
        self.selected_frames = select_frames(self.frames, 5)
        self.current_frame_index = 0  # Reset the frame index

        self.update_image()

    def select_color(self):
        color = colorchooser.askcolor()
        self.color = color[0]  # askcolor returns the color in two formats, we only need the first one
        self.update_image()

    def next_frame(self):
        # print(len(self.selected_frames))
        self.current_frame_index = (self.current_frame_index + 1) % len(self.selected_frames)
        self.update_image()

    # def update_image(self):
    #     if self.selected_frames and self.color:
    #         # Convert the color from RGB to BGR
    #         bgr_color = [int(c) for c in self.color[::-1]]
    #         frame = replace_color(self.selected_frames[self.current_frame_index], [0, 0, 255], bgr_color)
    #         image = Image.fromarray(frame)
    #         image = ImageTk.PhotoImage(image)

    #         self.label.config(image=image)
    #         self.label.image = image  # we need to keep a reference to the image or it will be garbage collected
    def update_image(self):
        if self.selected_frames:
            frame = self.selected_frames[self.current_frame_index]
            original_image = Image.fromarray(frame)
            original_image = ImageTk.PhotoImage(original_image)

            self.label.config(image=original_image)
            self.label.image = original_image  # we need to keep a reference to the image or it will be garbage collected

            if self.color:
                # Convert the color from RGB to BGR
                # print(self.color)
                bgr_color = [int(c) for c in self.color]
                modified_frame = replace_color(frame, bgr_color, [255, 0, 0], threshold=40)
                modified_image = Image.fromarray(modified_frame)
                modified_image = ImageTk.PhotoImage(modified_image)

                self.modified_label.config(image=modified_image)
                self.modified_label.image = modified_image  # we need to keep a reference to the image or it will be garbage collected