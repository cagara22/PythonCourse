import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI!")
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("SUBMIT", self)
        self.label = QLabel("[Greet]", self)
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 300, 40)
        self.line_edit.setStyleSheet("font-size: 30px;"
                                     "font-family: Verdana;")
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.setGeometry(310, 10, 100, 40)
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: Verdana;")
        self.button.clicked.connect(self.submit)

        self.label.setGeometry(10, 50, 200, 40)
        self.label.setStyleSheet("font-size: 20px;"
                                  "font-family: Verdana;")

    def submit(self):
        text = self.line_edit.text()
        self.label.setText(f"Hi {text}!")
        # print(f"Hello {text}!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
