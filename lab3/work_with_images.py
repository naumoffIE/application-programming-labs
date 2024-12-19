import numpy as np
import cv2


def read_image(path: str) -> np.ndarray:
    """
    Читает изображение из файла.

    Args:
        path (str): Путь к изображению.

    Returns:
        np.ndarray: Изображение в формате OpenCV.
    """
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Не удалось загрузить изображение: {path}")
    return image


def concatenate_images(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """
    Соединяет два изображения по горизонтали.

    Args:
        image1 (np.ndarray): Первое изображение.
        image2 (np.ndarray): Второе изображение.

    Returns:
        np.ndarray: Соединенное изображение.
    """
    height = max(image1.shape[0], image2.shape[0])
    image1_resized = cv2.resize(image1, (image2.shape[1], height))
    image2_resized = cv2.resize(image2, (image2.shape[1], height))
    return np.hstack((image1_resized, image2_resized))


def save_image(image: np.ndarray, path: str) -> None:
    """
    Сохраняет изображение в файл.

    Args:
        image (np.ndarray): Изображение.
        path (str): Путь для сохранения.
    """
    cv2.imwrite(path, image)
