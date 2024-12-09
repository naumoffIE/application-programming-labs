import argparse

from data_frame_functions import add_image_parameters
from data_frame_functions import add_area_column
from data_frame_functions import create_dataframe
from data_frame_functions import filter_images_by_size
from data_frame_functions import image_statistics
from data_frame_functions import sort_by_area
from histogram_processing import plot_column_distribution


def parsing() -> argparse.Namespace:
    """
    Parse command-line arguments for the script.

    :return: Namespace containing parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--annotation_file',
        default="C:/Users/Mi/PycharmProjects/lab2/lab2_var3/images/annotation.csv",
        type=str,
        help='Path to the annotation CSV file.'
    )
    parser.add_argument('-mw', '--max_width', type=int, default=1920, help='Maximum width of images.')
    parser.add_argument('-mh', '--max_height', type=int, default=1080, help='Maximum height of images.')
    return parser.parse_args()


def main():
    args = parsing()
    try:
        df = create_dataframe(args.annotation_file)
        print("DataFrame:")
        print(df)
        add_image_parameters(df)
        print("Images measurements:")
        dk = df.take([2, 3, 4], axis=1)
        print(dk)
        print("Image statistics:")
        print(image_statistics(df))
        print("Images after size-filtering:")
        print(filter_images_by_size(df, args.max_width, args.max_height))
        df = add_area_column(df)
        print("DataFrame with Area column:")
        print(df)
        df = sort_by_area(df)
        print("Sorted by Area DataFrame:")
        print(df)
        plot_column_distribution(df["Area"], 'Area')
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    main()

