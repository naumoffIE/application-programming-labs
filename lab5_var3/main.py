import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, \
    QFileDialog, QVBoxLayout, QWidget, QMessageBox

from iterator import ImageIterator


class MainWindow(QMainWindow):
    """
    Initializes a main application window.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("window application for viewing images")
        self.setFixedSize(1280, 920)
        self.setStyleSheet(
            """QMainWindow {
                background-color: #f2dcdf;
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

    def select_csv_file(self) -> None:
        """
        Opens a file dialog to select a CSV file containing image paths and initializes the image iterator.
        """
        filename, _ = QFileDialog.getOpenFileName(self, "Choose CSV file with paths to the images", "", "CSV Files ("
                                                                                                        "*.csv)")
        if filename:
            self.iterator = ImageIterator(filename)
            pixmap = QPixmap(self.iterator.current())
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def next_image(self) -> None:
        """
        Displays the next image in the iterator.
        """
        if self.iterator and self.iterator.image_paths:
            try:
                next_image_path = self.iterator.__next__()
                pixmap = QPixmap(next_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                QMessageBox.information(self, "DEnd of List", "You have reached the end of the image list.")

    def previous_image(self) -> None:
        """
        Displays the previous image in the iterator.
        """
        if self.iterator is not None:
            try:
                prev_image_path = self.iterator.previous()
                pixmap = QPixmap(prev_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                QMessageBox.information(self,  "Start of List", "You have reached the start of the image list.")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error acquired: {e}")


if __name__ == "__main__":
    main()
