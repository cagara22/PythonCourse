import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI!")
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(20, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Verdana;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_change)

    def checkbox_change(self, state):
        if state == Qt.Checked:
            print("You like food!")
        else:
            print("You don't like food!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()