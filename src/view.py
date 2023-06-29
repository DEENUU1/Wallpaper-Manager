import tkinter
import customtkinter as ct
from model import Model
from PIL import Image


ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")


class View(ct.CTk):
    def __init__(self, model: Model):
        super().__init__()
        self.model = model
        self.title("Wallpaper Manager")
        self.geometry("500x500")
        self.create_ui()

    def create_ui(self) -> None:
        self.frame = ct.CTkFrame(self, width=500, height=500)
        self.frame.pack()

        self.add_button = ct.CTkButton(self.frame, text="Add Wallpaper")
        self.add_button.pack(side="left")
        self.remove_button = ct.CTkButton(self.frame, text="Remove Wallpaper")
        self.remove_button.pack(side="left")

        self.next = ct.CTkButton(self.frame, text="Next")
        self.next.pack(side="left")
        self.previous = ct.CTkButton(self.frame, text="Previous")
        self.previous.pack(side="left")

    def bind_add_wallpaper(self, handler):
        self.add_button.bind("<Button-1>", handler)

    def bind_remove_wallpaper(self, handler):
        self.remove_button.bind("<Button-1>", handler)

    def bind_next(self, handler):
        self.next.bind("<Button-1>", handler)

    def bind_previous(self, handler):
        self.previous.bind("<Button-1>", handler)
