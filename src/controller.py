import tkinter.filedialog

from view import View
from model import Model


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.bind_add_wallpaper(self.add_wallpaper)
        self.view.bind_remove_wallpaper(self.remove_wallpaper)
        # self.view.bind_next()
        # self.view.bind_previous()

    def add_wallpaper(self, event=None) -> None:
        path = tkinter.filedialog.askopenfilename()
        if path:
            self.model.add_wallpaper(path)

    def remove_wallpaper(self, event=None) -> None:
        path = tkinter.filedialog.askopenfilename()
        if path:
            self.model.delete_wallpaper(path)

    def run(self) -> None:
        self.view.mainloop()
