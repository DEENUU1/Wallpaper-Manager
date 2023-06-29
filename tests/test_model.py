import pytest
from src.model import Model


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
