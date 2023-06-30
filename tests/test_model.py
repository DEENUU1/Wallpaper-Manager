import pytest
from src.wallpaper_manager.model import Model


@pytest.fixture
def model():
    path = [
        "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_1.jpg",
        "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_2.jpg",
        "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_3.jpg",
        "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_4.jpg",
    ]
    model = Model(path)
    return model


def test_current_index(model):
    assert model.current_index == 0


def test_add_wallpaper(model):
    model.add_wallpaper("C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_5.jpg")
    assert len(model.path) == 5


def test_delete_wallpaper(model):
    model.delete_wallpaper(1)
    assert len(model.path) == 3


def test_get_wallpaper(model):
    assert model.get_wallpaper(1) == "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_2.jpg"


def test_current_wallpaper(model):
    current = model.get_current_wallpaper()
    assert current == "C:\\Users\\Test\\Pulpit\\Projects\\Wallpaper-Manager\\wallpapers\\wallpaper_1.jpg"


def test_next_wallpaper(model):
    model.next_wallpaper()
    current = model.get_current_wallpaper()
    assert current == "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_2.jpg"


def test_previous_wallpaper(model):
    model.previous_wallpaper()
    current = model.get_current_wallpaper()
    assert current == "C:\\Users\Test\Pulpit\Projects\Wallpaper-Manager\wallpapers\wallpaper_4.jpg"


def test_images_name(model):
    assert model.return_images_name() == {0: "wallpaper_1.jpg", 1: "wallpaper_2.jpg", 2: "wallpaper_3.jpg", 3: "wallpaper_4.jpg"}
    assert len(model.return_images_name()) == 4
