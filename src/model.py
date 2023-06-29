class Model:
    def __init__(self) -> None:
        self.path = [
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper1.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper2.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper3.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper4.jpg",
        ]
        self.current_index = 0

    def add_wallpaper(self, path: str):
        print(path)
        return self.path.append(path)

    def delete_wallpaper(self, path: str):
        print(path)
        return self.path.remove(path)

    def get_current_wallpaper(self):
        return self.path[self.current_index]

    def next_wallpapepaper(self):
        self.current_index += 1
        if self.current_index >= len(self.path):
            self.current_index = 0
        return self.path[self.current_index]
