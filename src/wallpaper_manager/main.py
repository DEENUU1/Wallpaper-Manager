from view import View
from model import Model
from controller import Controller
import os


WORK_DIR = os.path.dirname(__file__)
WALLPAPERS_DIR = os.path.join(WORK_DIR, "wallpapers")
PATH = [
    os.path.join(WALLPAPERS_DIR, wallpaper) for wallpaper in os.listdir(WALLPAPERS_DIR) if wallpaper.endswith(".jpg")
]


def main() -> None:

    model = Model(PATH)
    view = View(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
