import re
import argparse


def parsing() -> str:
    """
      Parse command line arguments and returns the file name      :return: file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='The name of the file to analyze')
    args = parser.parse_args()
    return args.file


def open_file(namefile: str) -> str:
    """
    Reading the contents of a file
    :param namefile: The file name       :return: A string containing data from a file
    """
    with open(namefile, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def separation_text(text: str) -> list[str]:
    """
    Searches for parser values in the text
    :param text: A line with the words
    :return: A row with birthdates
    """
    pattern = r'\d{2}.\d{2}.\d{4}'
    people = re.findall(pattern, text)
    return people


def separation_birth(year: int, month: int, day: int) -> int:
    """
    Check the condition of occurrence of birthdays
    :param year:
    :param month:
    :param day:
    :return:  1 if it fits
    """
    current_year = 2024
    return (1983 <= year <= 1993) or \
           (1984 <= year < current_year and month >= 9 and day >= 25) or \
           (year == current_year and month <= 9 and day <= 25)


def counting_birth(people: list[str]) -> int:
    """
    Divides the date of the birthday into components and goes through all
    :return: the number of suitable dates
    """
    count = 0
    for date_str in people:
        year, month, day = map(int, date_str.split('.'))
        count += separation_birth(year, month, day)
    return count


def main():
    filename = parsing()
    text = open_file(filename)
    separation = separation_text(text)
    quantity = counting_birth(separation)
    print('Количество людей возрастом от 30 до 40 лет:', quantity)


if __name__ == "__main__":
    main()
