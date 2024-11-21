import argparse
from work_with_images import download_images
from work_with_images import create_annotation_csv
from iterator import ImageIterator


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
