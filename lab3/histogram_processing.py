from typing import Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np


def calculate_histogram(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Вычисляет гистограмму изображения для каждого цветового канала.

    Args:
        image (np.ndarray): Изображение в формате OpenCV.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: Гистограммы для каналов R, G, B.
    """
    r_hist = cv2.calcHist([image], [2], None, [256], [0, 256])
    g_hist = cv2.calcHist([image], [1], None, [256], [0, 256])
    b_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return r_hist, g_hist, b_hist


def plot_histogram(hist_data: Tuple[np.ndarray, np.ndarray, np.ndarray], output_path: str) -> None:
    """
    Строит и сохраняет гистограмму изображения.

    Args:
        hist_data (Tuple[np.ndarray, np.ndarray, np.ndarray]): Гистограммы для каналов R, G, B.
        output_path (str): Путь для сохранения гистограммы.
    """
    plt.figure(figsize=(10, 6))
    colors = ("r", "g", "b")
    for hist, color in zip(hist_data, colors):
        plt.plot(hist, color=color)
    plt.title("Histogram")
    plt.xlabel("Intensity Value")
    plt.ylabel("Pixel Count")
    plt.legend(("Red Channel", "Green Channel", "Blue Channel"))
    plt.grid()
    plt.savefig(output_path.replace(".jpg", "_histogram.png"))
    plt.close()
