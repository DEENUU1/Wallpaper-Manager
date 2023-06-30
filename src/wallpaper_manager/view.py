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
        self.geometry("1000x700")
        self.image_size = (550, 500)
        self.sidebar_open = True
        self.create_ui()

    def create_ui(self) -> None:
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ct.CTkFrame(self, fg_color="#202020")
        self.content_frame = ct.CTkFrame(self)

        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.add_button = ct.CTkButton(self.sidebar_frame, text="Add Wallpaper")
        self.add_button.grid(pady=10, padx=10)
        self.remove_button = ct.CTkButton(self.sidebar_frame, text="Remove Wallpaper")
        self.remove_button.grid(padx=10)

        self.set_wallpaper = ct.CTkButton(self.sidebar_frame, text="Set as a Wallpaper")
        self.set_wallpaper.grid(padx=10)

        self.load_image(self.model.get_current_wallpaper())

        self.next = ct.CTkButton(self.content_frame, text="Next")
        self.next.grid(row=1, column=1, pady=0)
        self.previous = ct.CTkButton(self.content_frame, text="Previous")
        self.previous.grid(row=1, column=0, pady=0)

        self.toggle_button = ct.CTkButton(self.content_frame, text="Toggle Sidebar")
        self.toggle_button.grid(row=1, column=3, pady=0)

        self.scrollbar = tkinter.Scrollbar(self.sidebar_frame, orient="vertical", background="black")
        self.listbox = tkinter.Listbox(
            self.sidebar_frame,
            yscrollcommand=self.scrollbar.set,
            width=20, height=20,
            font={"Helvetica", 10},
            background="#202020",
            foreground="#ffffff"
        )
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.grid(row=3, column=2, sticky="ns")
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

    def load_image(self, image_path: str) -> None:
        image = Image.open(image_path)
        image = image.resize(self.image_size, Image.ANTIALIAS)
        self.photo = ct.CTkImage(light_image=image, dark_image=image, size=self.image_size)
        self.image = ct.CTkLabel(self.content_frame, image=self.photo, text="")
        self.image.grid(row=0, column=1, pady=80)

    def update_image(self, image_path: str) -> None:
        image = Image.open(image_path)
        image = image.resize(self.image_size, Image.ANTIALIAS)
        self.photo = ct.CTkImage(light_image=image, dark_image=image, size=self.image_size)
        self.image.configure(image=self.photo)

    def bind_add_wallpaper(self, handler):
        self.add_button.bind("<Button-1>", handler)

    def bind_side_bar(self, handler):
        self.toggle_button.bind("<Button-1>", handler)

    def bind_remove_wallpaper(self, handler):
        self.remove_button.bind("<Button-1>", handler)

    def bind_next(self, handler):
        self.next.bind("<Button-1>", handler)

    def bind_previous(self, handler):
        self.previous.bind("<Button-1>", handler)

    def bind_set_wallpaper(self, handler):
        self.set_wallpaper.bind("<Button-1>", handler)