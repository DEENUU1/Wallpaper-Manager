class Model:
    def __init__(self) -> None:
        self.path = [
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_1.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_2.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_3.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_4.jpg",
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
