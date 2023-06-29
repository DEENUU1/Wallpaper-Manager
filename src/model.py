class Model:
    def __init__(self) -> None:
        self.path = [
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper1.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper2.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper3.jpg",
            "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper4.jpg",
        ]

    def add_wallpaper(self, path: str):
        print(path)
        return self.path.append(path)

    def delete_wallpaper(self, path: str):
        print(path)
        return self.path.remove(path)

    # def get_wallpaper(self, path):
    #     return self.path[path]
