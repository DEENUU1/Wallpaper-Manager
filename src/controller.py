import tkinter.filedialog

from view import View
from model import Model


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.bind_add_wallpaper(self.add_wallpaper)
        self.view.bind_remove_wallpaper(self.remove_wallpaper)
        self.view.bind_next(self.next_wallpaper)
        self.view.bind_previous(self.previous_wallpaper)
        self.view.bind_side_bar(self.toggle_sidebar)
        self.display_images_names()

    def add_wallpaper(self, event=None) -> None:
        path = tkinter.filedialog.askopenfilename()
        if path:
            self.model.add_wallpaper(path)

    def remove_wallpaper(self, event=None) -> None:
        path = tkinter.filedialog.askopenfilename()
        if path:
            self.model.delete_wallpaper(path)

    def next_wallpaper(self, event=None) -> None:
        path = self.model.next_wallpaper()
        self.view.update_image(path)

    def previous_wallpaper(self, event=None) -> None:
        path = self.model.previous_wallpaper()
        self.view.update_image(path)

    def run(self) -> None:
        self.view.mainloop()

    def toggle_sidebar(self, handler):
        if self.view.sidebar_open:
            self.view.sidebar_frame.grid_remove()
        else:
            self.view.sidebar_frame.grid()
        self.view.sidebar_open = not self.view.sidebar_open

    def display_images_names(self):
        for image_name in self.model.return_images_name():
            self.view.listbox.insert(tkinter.END, image_name)
