import argparse
import csv
import cv2
from icrawler.builtin import GoogleImageCrawler
from typing import Optional, Any
import os


def parsing() -> argparse.Namespace:
    """
    Parses command-line arguments for the script.

    :return: Parsed command-line arguments as a Namespace object, containing:
             - keyword: Keyword for image search
             - save_dir: Directory to save downloaded images
             - annotation_file: Path to the annotation CSV file
             - num_images: Number of images to download
    """
    parser = argparse.ArgumentParser(description="Download images and create an iterator for a specified class.")
    parser.add_argument("--keyword", type=str, default="bird", help="Keyword for image search")
    parser.add_argument("--save_dir", type=str, default="images", help="Directory to save downloaded images")
    parser.add_argument("--annotation_file", type=str, default="images/annotation.csv", help="Path to the annotation "
                                                                                             "CSV file")
    parser.add_argument("--num_images", type=int, default=50, help="Number of images to download (default: 50)")
    args = parser.parse_args()
    return args


def download_images(keyword: str, save_dir: str, num_images: int) -> None:
    """
    Downloads images from Google Images based on a specified keyword.

    :param: keyword: Keyword for the image search.
    :param: save_dir: Directory where images will be saved.
    :param: num_images: Maximum number of images to download.
    :return: None
    """
    crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
    crawler.crawl(keyword=keyword, max_num=num_images)


def create_annotation_csv(annotation_file: str, save_dir: str) -> None:
    """
    Creates a CSV file that annotates downloaded images with their absolute and relative paths.

    :param: annotation_file: Path to the output CSV file for annotations.
    :param: save_dir: Directory containing the downloaded images.
    :return: None
    """
    with open(annotation_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["absolute_path", "relative_path"])

        for root, _, files in os.walk(save_dir):
            for name in files:
                if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    abs_path = os.path.abspath(os.path.join(root, name))
                    rel_path = os.path.relpath(abs_path, start=save_dir)
                    writer.writerow([abs_path, rel_path])


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


def main():
    args = parsing()

    download_images(args.keyword, args.save_dir, args.num_images)
    create_annotation_csv(args.annotation_file, args.save_dir)
    iterator = ImageIterator(args.annotation_file)

    for image in iterator:
        if image is not None:
            print("Image downloaded!")
        else:
            print("Failed to download an image.")


if __name__ == "__main__":
    main()
