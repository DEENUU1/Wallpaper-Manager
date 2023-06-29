

class Model:
    def __init__(self) -> None:
        self.path = []

    def add_wallpaper(self, path: str):
        return self.path.append(path)

    def delete_wallpaper(self, path: str):
        return self.path.remove(path)

    # def get_wallpaper(self, path):
    #     return self.path[path]
