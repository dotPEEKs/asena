import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from PySide6.QtWidgets import *

from ui.sidebar import Ui_MainWindow

class Sidebar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame_3.setStyleSheet("background-color: 'red';")
        self.pushButton_6.clicked.connect(self.toggle_side_bar)
        self.toggle = True
    def toggle_side_bar(self):
        if self.toggle:
            self.frame_2.hide()
        else:
            self.frame_2.show()
        self.toggle = not self.toggle
app = QApplication([])
window = Sidebar()
window.show()
app.exec()