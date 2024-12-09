import cv2
import pandas as pd


def create_dataframe(file_csv: str) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a CSV file containing image paths.

    :param: file_csv: Path to the CSV file.
    :return: DataFrame with columns ['Absolute_path', 'Relative_path'].
    :raises FileNotFoundError: If the CSV file cannot be loaded.
    """
    try:
        df = pd.read_csv(file_csv)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_csv}")

    if df.empty:
        raise ValueError(f"The file {file_csv} is empty or improperly formatted.")

    df.columns = ['Absolute_path', 'Relative_path']
    return df


def add_image_parameters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add image dimensions (height, width, depth) to the DataFrame.

    :param: df: DataFrame with a column 'Absolute_path' containing image file paths.
    :return: DataFrame with additional columns: 'Height', 'Width', 'Depth'
    """
    heights, widths, depths = [], [], []
    for abs_path in df['Absolute_path']:
        img = cv2.imread(abs_path)
        heights.append(img.shape[0])
        widths.append(img.shape[1])
        depths.append(img.shape[2])

    df['Height'] = heights
    df['Width'] = widths
    df['Depth'] = depths
    return df


def image_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute descriptive statistics for image dimensions.

    :param: df: DataFrame with columns 'Width', 'Height', and 'Depth'.
    :return: DataFrame with descriptive statistics for the specified columns.
    """
    return df[['Width', 'Height', 'Depth']].describe()


def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Filter images based on maximum width and height.

    :param: df: DataFrame with columns 'Width' and 'Height'.
    :param: max_width: Maximum allowable width.
    :param: max_height: Maximum allowable height.
    :return: Filtered DataFrame containing images within the specified size.
    """
    return df[(df['Width'] <= max_width) & (df['Height'] <= max_height)]


def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a new column 'Area' to the DataFrame, calculated as width * height.

    :param df: DataFrame with columns 'Width' and 'Height'.
    :return: DataFrame with an additional column 'Area'.
    """
    df['Area'] = df['Width'] * df['Height']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort the DataFrame by the 'Area' column in ascending order.

    :param: df: DataFrame with an 'Area' column.
    :return: Sorted DataFrame.
    """
    return df.sort_values(by='Area', ascending=True)
