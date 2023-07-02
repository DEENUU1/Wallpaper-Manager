from typing import List, Dict


class Model:
    """
    Data model with methods to manipulate the data.
    """
    def __init__(self, path: List[str] = None) -> None:
        self.path = path if path is not None else []
        self.current_index = 0

    def get_wallpaper(self, index) -> str:
        """
        Returns the path for an image of a given index
        """
        return self.path[index]

    def add_wallpaper(self, path: str) -> None:
        """
        Adds a new image to the list of images
        """
        return self.path.append(path)

    def delete_wallpaper(self, index: str) -> None:
        """
        Deletes an image from the list of images
        """
        path = self.get_wallpaper(index)
        return self.path.remove(path)

    def get_current_wallpaper(self) -> str:
        """
        Returns the current image
        """
        return self.path[self.current_index]

    def next_wallpaper(self) -> str:
        """
        Returns the next image in the list
        """
        self.current_index += 1
        if self.current_index >= len(self.path):
            self.current_index = 0
        return self.path[self.current_index]

    def previous_wallpaper(self) -> str:
        """
        Returns the previous image in the list
        """
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.path) - 1
        return self.path[self.current_index]

    def return_images_name(self) -> Dict[int, str]:
        """
        Returns a dictionary with the index as key and the name of the image as value
        """
        names = {}
        for i, path in enumerate(self.path):
            names[i] = path.split("\\")[-1]
        return names
