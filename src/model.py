from typing import List


class Model:
    def __init__(self, path: List[str] = None) -> None:
        self.path = path
        self.current_index = 0

    def get_wallpaper(self, index):
        return self.path[index]

    def add_wallpaper(self, path: str):
        return self.path.append(path)

    def delete_wallpaper(self, index: int):
        path = self.get_wallpaper(index)
        return self.path.remove(path)

    def get_current_wallpaper(self):
        return self.path[self.current_index]

    def next_wallpaper(self):
        self.current_index += 1
        if self.current_index >= len(self.path):
            self.current_index = 0
        return self.path[self.current_index]

    def previous_wallpaper(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.path) - 1
        return self.path[self.current_index]

    def return_images_name(self):
        names = []
        for i in range(len(self.path)):
            names.append(self.path[i].split("\\")[-1])
        return names
