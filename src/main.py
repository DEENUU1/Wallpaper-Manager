from view import View
from model import Model
from controller import Controller


def main() -> None:
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
