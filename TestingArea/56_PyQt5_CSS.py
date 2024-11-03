import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI!")
        self.setWindowIcon(QIcon("logo.png"))

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            font-family: Verdana;
            padding: 20px 50px;
            margin: 10px;
            border: 5px solid;
            border-radius: 10px;
        }
        
        QPushButton#button1{
            background-color: red;
        }
        
        QPushButton#button2{
            background-color: green;
        }
        
        QPushButton#button3{
            background-color: yellow;
        }
        
        QPushButton#button1:hover, QPushButton#button2:hover, QPushButton#button3:hover{
            background-color: black;
            color: white;
        }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
