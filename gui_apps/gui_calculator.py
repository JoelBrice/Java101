import sys
from PyQt5 import QtWidgets
from  PyQt5.QtWidgets import QApplication, QMainWindow, QBoxLayout, QLabel, QListWidget, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.result = QLabel(self)
        self.initUI()
              
    def button_clicked(self):
        self.result.setText(" Button clicked!")
        self.result.baseSize()
        self.result.move(50,100)
        
    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle("Tech With Tim")
        
        self.label = QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50 ,50)
        
        self.b1 = QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.resize(800, 400)
    win.show()
    sys.exit(app.exec_())

window()