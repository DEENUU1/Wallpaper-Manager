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
        self.geometry("1350x690")
        self.image_size = (900, 500)
        self.sidebar_open = True
        self.resizable(False, False)
        self.create_ui()

    def create_ui(self) -> None:
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        self.sidebar_frame = ct.CTkFrame(self, fg_color="#202020")
        self.content_frame = ct.CTkFrame(self)

        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.label = ct.CTkLabel(self.sidebar_frame, text="Wallpapers")
        self.label.grid(pady=10)

        self.add_button = ct.CTkButton(self.sidebar_frame, text="Add Wallpaper")
        self.add_button.grid(pady=10, padx=10)
        self.remove_button = ct.CTkButton(self.sidebar_frame, text="Remove Wallpaper")
        self.remove_button.grid(padx=10)

        self.set_wallpaper = ct.CTkButton(self.sidebar_frame, text="Set as a Wallpaper")
        self.set_wallpaper.grid(padx=10)

        self.load_image(self.model.get_current_wallpaper())

        self.next = ct.CTkButton(self.content_frame, text="Next")
        self.next.grid(row=1, column=2, pady=0)
        self.previous = ct.CTkButton(self.content_frame, text="Previous")
        self.previous.grid(row=1, column=0, pady=0)

        self.scrollbar = tkinter.Scrollbar(self.sidebar_frame, orient="vertical", background="black")
        self.listbox = tkinter.Listbox(
            self.sidebar_frame,
            yscrollcommand=self.scrollbar.set,
            width=20, height=20,
            font={"Helvetica", 10},
            background="#202020",
            foreground="#ffffff"
        )
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky="ns")
        self.listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def update_listbox(self) -> None:
        self.listbox.delete(0, tkinter.END)
        image_dict = self.model.return_images_name()
        for name in image_dict.values():
            self.listbox.insert(tkinter.END, name)

    def on_select(self, event) -> None:
        widget = event.widget
        selection = widget.curselection()
        if selection:
            selected_item = widget.get(selection[0])
            image_dict = self.model.return_images_name()
            selected_index = [index for index,name in image_dict.items() if name == selected_item][0]
            image_path = self.model.get_wallpaper(selected_index)
            self.update_image(image_path)

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

    def bind_remove_wallpaper(self, handler):
        self.remove_button.bind("<Button-1>", handler)

    def bind_next(self, handler):
        self.next.bind("<Button-1>", handler)

    def bind_previous(self, handler):
        self.previous.bind("<Button-1>", handler)

    def bind_set_wallpaper(self, handler):
        self.set_wallpaper.bind("<Button-1>", handler)
