import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, \
    QFileDialog, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from iterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window application for viewing images")
        self.setFixedSize(1280, 920)
        self.setStyleSheet("""QMainWindow {
                background-color: #f2dcdf; /* Цвет фона внутри окна */
            }
        """)
        self.image_label = QLabel(self)
        self.image_label.resize(1080, 700)
        self.image_label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.image_label)
        self.setCentralWidget(central_widget)

        self.button_previous = QPushButton("<< Previous", self)
        self.button_previous.setFixedSize(450, 80)
        self.button_previous.move(0, 840)
        self.button_previous.setStyleSheet('background-color: #de5d83;')
        self.button_previous.clicked.connect(self.previous_image)

        self.button_path = QPushButton("Select CSV File", self)
        self.button_path.setFixedSize(380, 80)
        self.button_path.move(450, 840)
        self.button_path.setStyleSheet('background-color: #de5d83;')
        self.button_path.clicked.connect(self.select_csv_file)

        self.button_next = QPushButton("Next >>", self)
        self.button_next.setFixedSize(450, 80)
        self.button_next.move(830, 840)
        self.button_next.setStyleSheet('background-color: #de5d83;')
        self.button_next.clicked.connect(self.next_image)

        self.iterator = None

    def select_csv_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите CSV файл с путями к изображениям", "", "CSV Files ("
                                                                                                         "*.csv)")
        if filename:
            self.iterator = ImageIterator(filename)
            pixmap = QPixmap(self.iterator.current())
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def next_image(self):
        if self.iterator and self.iterator.image_paths:
            try:
                next_image_path = self.iterator.__next__()
                pixmap = QPixmap(next_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                QMessageBox.information(self, "Конец списка", "Вы достигли конца списка изображений.")

    def previous_image(self):
        if self.iterator is not None:
            try:
                prev_image_path = self.iterator.previous()
                pixmap = QPixmap(prev_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                QMessageBox.information(self, "Начало списка", "Вы достигли начала списка изображений.")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
