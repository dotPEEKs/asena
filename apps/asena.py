import os
import sys
import time

from PyQt5.QtWidgets import QFrame
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import QPoint
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRect
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt,QEasingCurve
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPropertyAnimation
path = os.path.join(
    os.path.dirname(__file__),
    ".."
)
sys.path.append(path)
from models.main_window import Ui_MainWindow
from models.history import Ui_Frame
class AsenaMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() # initialize all class
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        self.toggle = False
        self._drag_position = QPoint()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.label.setText("Coded By dotPEEK")
        self.sidebar_toggle_btn.clicked.connect(self.handle_sidebar)
        self.animation_slidebar = QPropertyAnimation(self.slide_sidebar,b"geometry")
        self.animation_slidebar.setDuration(300)
        self.animation_inside_container = QPropertyAnimation(self.inside_container,b"geometry")

        self.animation_inside_container.setDuration(300)
        self.active_orders_btn.clicked.connect(lambda :self.label.setText("Aktif Siparişler :)"))
        self.orders_history_btn.clicked.connect(self.handle_orders_history_btn)
        self.orders_screen_btn.clicked.connect(lambda :self.label.setText("Sipariş ekranı :)"))
        self.settings_btn.clicked.connect(lambda :self.label.setText("Ayarlar :)"))
        self.minisidebar_active_orders_btn.clicked.connect(lambda :self.label.setText("Aktif Siparişler :)"))
        self.minisidebar_orders_history_btn.clicked.connect(lambda :self.label.setText("Sipariş Geçmişi :)"))
        self.minisidebar_orders_screen_btn.clicked.connect(lambda :self.label.setText("Sipariş ekranı :)"))
        self.minisidebar_settings_btn.clicked.connect(lambda :self.label.setText("Ayarlar :)"))
        self.minisidebar_exit_btn.clicked.connect(lambda :self.label.setText("Hadi byy"))
        self.exit_btn.clicked.connect(self.close)
        self.maximize_btn.clicked.connect(lambda :self.showMaximized())
        self.minimize_btn.clicked.connect(lambda :self.showMinimized())
        self.close_btn.clicked.connect(lambda :self.close())
        self.ui = None

    def handle_sidebar(self):
        if not self.toggle:
            self.animation_slidebar.setStartValue(
                QRect(
                    61,1,
                    self.slide_sidebar.width(),
                    self.height()
                )
            )
            self.animation_slidebar.setEndValue(
                QRect(
                    61,1,
                    0,527
                )
            )
            self.animation_inside_container.setStartValue(
                QRect(
                    261,
                    1,
                    self.inside_container.width(),
                    self.height()
                )
            )
            self.animation_inside_container.setEndValue(
                QRect(
                    61,1,
                    self.inside_container.width() + 200,
                    self.inside_container.height()
                )
            )
        else:
            self.animation_inside_container.setStartValue(
                QRect(
                    61, 1,
                    self.inside_container.width(),
                    self.height()
                )
            )
            self.animation_inside_container.setEndValue(QRect(
                    261,
                    1,
                    self.inside_container.width() - 200,
                    self.height()
                )
            )
            self.animation_slidebar.setStartValue(
                QRect(
                    61,1,0,self.height()
                )
            )
            self.animation_slidebar.setEndValue(
                QRect(
                    61,1,
                    200,self.height()
                )
            )
        self.animation_slidebar.start()
        self.animation_inside_container.start()
        print("Konum",self.inside_container.geometry(),self.sidebar_toggle_btn.geometry())
        self.toggle = not self.toggle
    def handle_orders_history_btn(self):
        ui_loader = QFile(os.path.join(os.path.dirname(__file__),"..","ui","orders_history.ui"))
        ui_loader.open(QFile.ReadOnly)

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
    def resizeEvent(self, event):
        if not self.ui is None:
            self.ui.setGeometry(0,0,self.main_page.width(),self.main_page.height())
    def mouseReleaseEvent(self, event):
        # Fareyi serbest bırakınca hareketi durdur
        self._drag_position = QPoint()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AsenaMainWindow()
    window.show()
    app.exec()