import tkinter.filedialog

from view import View
from model import Model
import ctypes


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.bind_add_wallpaper(self.add_wallpaper)
        self.view.bind_remove_wallpaper(self.remove_wallpaper)
        self.view.bind_next(self.next_wallpaper)
        self.view.bind_previous(self.previous_wallpaper)
        self.display_images_names()
        self.view.bind_set_wallpaper(self.set_wallpaper)

    def add_wallpaper(self, event=None) -> None:
        path = tkinter.filedialog.askopenfilename()
        if path:
            self.model.add_wallpaper(path)
            self.display_images_names()
            self.view.update_image(path)

    def remove_wallpaper(self, event=None) -> None:
        selected_index = self.view.listbox.curselection()
        if selected_index:
            self.model.delete_wallpaper(selected_index[0])
            self.view.update_listbox()

    def next_wallpaper(self, event=None) -> None:
        path = self.model.next_wallpaper()
        self.view.update_image(path)

    def previous_wallpaper(self, event=None) -> None:
        path = self.model.previous_wallpaper()
        self.view.update_image(path)

    def run(self) -> None:
        self.view.mainloop()

    def toggle_sidebar(self, handler) -> None:
        if self.view.sidebar_open:
            self.view.sidebar_frame.grid_remove()
        else:
            self.view.sidebar_frame.grid()
        self.view.sidebar_open = not self.view.sidebar_open

    def display_images_names(self) -> None:
        self.view.listbox.delete(0, tkinter.END)
        for image_name in self.model.return_images_name().values():
            self.view.listbox.insert(tkinter.END, image_name)

    def set_wallpaper(self, event=None) -> None:
        current_wallpaper = self.model.get_current_wallpaper()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, current_wallpaper, 0)

