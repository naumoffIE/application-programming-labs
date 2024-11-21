import csv
import cv2
from typing import Optional, Any


class ImageIterator:
    """
    Iterator class for loading images from an annotation CSV file.

    Iterates over image file paths recorded in the CSV and loads each image using OpenCV.
    """
    def __init__(self, annotation_file: str) -> None:
        """
        Initializes the iterator with paths from the annotation CSV file.

        :param: annotation_file: Path to the CSV file containing image paths.
        """
        with open(annotation_file, newline='', encoding='utf-8') as file:
            self.image_paths = [row[0] for row in csv.reader(file)][1:]
        self.index = 0

    def __iter__(self) -> 'ImageIterator':
        """
        Returns the iterator object itself.

        :return: The iterator object.
        """
        return self

    def __next__(self) -> Optional[Any]:
        """
        Returns the next image in the iteration or raises StopIteration if no more images.

        :return: The next image loaded with OpenCV, or None if loading fails.
        """
        if self.index >= len(self.image_paths):
            raise StopIteration
        image = cv2.imread(self.image_paths[self.index])
        self.index += 1
        return image
