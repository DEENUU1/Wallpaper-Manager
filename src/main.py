from view import View
from model import Model
from controller import Controller

PATH = [
    "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_1.jpg",
    "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_2.jpg",
    "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_3.jpg",
    "C:\\Users\Kacper\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_4.jpg",
]


def main() -> None:
    model = Model(PATH)
    view = View(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
