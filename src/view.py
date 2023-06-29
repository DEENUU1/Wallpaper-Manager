import tkinter
import customtkinter as ct
from model import Model


ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")


class View(ct.CTk):
    def __init__(self, model: Model):
        super().__init__()
        self.model = model
        self.title("Wallpaper Manager")
        self.geometry("500x500")

    def bind_add_wallpaper(self, handler):
        pass

    def bind_remove_wallpaper(self, handler):
        pass
