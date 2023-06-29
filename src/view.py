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

        self.load_image(self.model.get_current_wallpaper())

        self.add_button = ct.CTkButton(self.frame, text="Add Wallpaper")
        self.add_button.pack(side="left")
        self.remove_button = ct.CTkButton(self.frame, text="Remove Wallpaper")
        self.remove_button.pack(side="left")

        self.next = ct.CTkButton(self.frame, text="Next")
        self.next.pack(side="top")
        self.previous = ct.CTkButton(self.frame, text="Previous")
        self.previous.pack(side="top")

    def load_image(self, image_path: str) -> None:
        image = Image.open(image_path)
        image = image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ct.CTkImage(light_image=image, dark_image=image, size=(450, 450))
        self.image = ct.CTkLabel(self.frame, image=self.photo, text="")
        self.image.pack()

    def update_image(self, image_path: str) -> None:
        image = Image.open(image_path)
        image = image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ct.CTkImage(light_image=image, dark_image=image, size=(450, 450))
        self.image.configure(image=self.photo)

    def bind_add_wallpaper(self, handler):
        self.add_button.bind("<Button-1>", handler)

    def bind_remove_wallpaper(self, handler):
        self.remove_button.bind("<Button-1>", handler)

    def bind_next(self, handler):
        self.next.bind("<Button-1>", handler)

    def bind_previous(self, handler):
        self.previous.bind("<Button-1>", handler)
