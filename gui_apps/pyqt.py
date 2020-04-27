import sys
from PyQt5.QtWidgets import QApplication, QDialogButtonBox, QLabel, QMainWindow, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from ctypes import dll

# Subclass QMainWindow to customise your application's main window
class GUIWin(QWidget):

    def __init__(self, *args, **kwargs):
        super(GUIWin, self).__init__(*args, **kwargs)
        self.setWindowTitle("Simple GUI")
        box_layout = QHBoxLayout()
        
        self.setLayout(box_layout)
        self.label = QLabel("\t\t\t Simple GUI example \n\n\n\n\n")
        self.x = 2
        self.y = 3
        self.z =self.x/self.y
        self.x_value = QLabel(str(self.x))
        self.division_label = QLabel('/')
        self.y_value = QLabel(str(self.y))
        self.equal_label = QLabel('= ')
        self.z_value = QLabel(str(self.z))

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        box_layout.addWidget(self.label)
        box_layout.addWidget(self.x_value)
        box_layout.addWidget(self.division_label)
        box_layout.addWidget(self.y_value)
        box_layout.addWidget(self.equal_label)
        box_layout.addWidget(self.z_value)
        
        # QBtn = QDialogButtonBox.Ok  # No cancel
        # self.buttonBox = QDialogButtonBox(QBtn)
        # layout = QVBoxLayout()
        # title = QLabel("MooseAche")
        # font = title.font()
        # font.setPointSize(20)
        # title.setFont(font)

        # layout.addWidget(title)

        # layout.addWidget(QLabel("Version 23.35.211.233232"))
        # layout.addWidget(QLabel("Copyright 2015 MooseAche Inc."))

        # for i in range(0, layout.count()):
        #     layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        # layout.addWidget(self.buttonBox)

        # self.setLayout(layout)


app = QApplication(sys.argv)
mainwindow = GUIWin()
mainwindow.resize(800,600)
mainwindow.show()
sys.exit(app.exec_())