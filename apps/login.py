import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QPoint
from models.login_model import Ui_Form
from assets import assets
class Login(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ASENA - LOGIN")
        self.setWindowIcon(QIcon(u":/resources/asena_main.png"))
        self.minimize_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.login_btn.clicked.connect(lambda :print("You god damn right :)"))

        self._drag_position = QPoint()

    def mousePressEvent(self, event):
        # Fare tıklama ile pencereyi hareket ettirmek için başlat
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        # Fare hareket ettiğinde pencereyi taşı
        if event.buttons() & Qt.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self._drag_position)
            self.move(self.pos() + delta)
            self._drag_position = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        # Fareyi serbest bırakınca hareketi durdur
        self._drag_position = QPoint()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
