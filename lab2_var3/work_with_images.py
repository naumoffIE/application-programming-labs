import csv
import os

from icrawler.builtin import BingImageCrawler


def download_images(keyword: str, save_dir: str, num_images: int) -> None:
    """
    Downloads images from Google Images based on a specified keyword.

    :param: keyword: Keyword for the image search.
    :param: save_dir: Directory where images will be saved.
    :param: num_images: Maximum number of images to download.
    :return: None
    """
    crawler = BingImageCrawler(storage={"root_dir": save_dir})
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
                    rel_path = os.path.relpath(abs_path)
                    writer.writerow([abs_path, rel_path])
