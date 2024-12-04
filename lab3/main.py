import argparse

import cv2

from histogram_processing import calculate_histogram
from histogram_processing import plot_histogram
from work_with_images import concatenate_images
from work_with_images import read_image
from work_with_images import save_image


def parsing() -> argparse.Namespace:
    """
    Парсит аргументы командной строки.

    Returns:
        argparse.Namespace: Объект с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Обработка изображения: построение гистограммы, преобразования и соединение изображений."
    )
    parser.add_argument("input_path", type=str, help="Путь к входному изображению.")
    parser.add_argument("output_path", type=str, help="Путь для сохранения результата.")
    parser.add_argument(
        "concat_path", type=str, help="Путь к изображению для соединения."
    )
    return parser.parse_args()


def main() -> None:
    """
    Основная функция программы.
    """
    args = parsing()
    try:
        image = read_image(args.input_path)
        print("Изображение успешно загружено!")
    except FileNotFoundError as error:
        print(f"Ошибка: {error}")
        image = None

    if image is not None:
        pass
    try:
        concat_image = read_image(args.concat_path)
        print("Изображение успешно загружено!")
    except FileNotFoundError as error:
        print(f"Ошибка: {error}")
        concat_image = None

    if concat_image is not None:
        pass

    print(f"Размер первого изображения: {image.shape[:2]}")
    print(f"Размер второго изображения: {concat_image.shape[:2]}")

    histogram = calculate_histogram(image)
    plot_histogram(histogram, args.output_path)
    hist_image = cv2.imread("output_path_histogram.png")

    combined_image = concatenate_images(image, concat_image)

    cv2.imshow("Исходное изображение", image)
    cv2.imshow("Соединенное изображение", combined_image)
    cv2.imshow("Гистограмма исходного изображения", hist_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_image(combined_image, args.output_path)
    print(f"Результат сохранен: {args.output_path}")


if __name__ == "__main__":
    main()
