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
