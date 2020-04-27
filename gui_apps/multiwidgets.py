import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        self.label = QLabel('Calculator')
        self.x = 12
        self.y = 32
        self.result = self.x+self.y
        self.current_value = str(self.x)
        self.y_value = str(self.y)
        self.z = self.y+self.x
        self.total_value = str(self.z)

        self.label_current = QLabel(self.current_value)
        self.plus_label = QLabel('+')
        self.label_y_value = QLabel(self.y_value)
        self.equal_label = QLabel('=')
        self.label_total = QLabel(self.total_value)

        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.label_current)
        self.h_layout.addWidget(self.plus_label)
        self.h_layout.addWidget(self.label_y_value)
        self.h_layout.addWidget(self.equal_label)
        self.h_layout.addWidget(self.label_total)
        
    def add(self, a, b):
        return a+b
    
    def div(self, x,y):
        return x/y


if __name__=="__main__":
    app = QApplication(sys.argv)
    mainwindow = Widget()
    mainwindow.resize(800, 400)
    mainwindow.show()
    sys.exit(app.exec_())