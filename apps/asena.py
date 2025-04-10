import os
import sys
import time

from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QScrollArea
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHeaderView,QTabWidget
from PySide6.QtWidgets import QStackedWidget,QWidget
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QFrame
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
from models.custom_widgets import QCardWidget

class AsenaMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() # initialize all class
        self.setupUi(self)
        self.main_container.setStyleSheet("border-radius: 10px;")
        self.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        self._drag_position = QPoint()
        self.set_all_signals()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.inside_container_animation_handler = self.create_animation_object(self.inside_container)
        self.slide_sidebar_animation_handler = self.create_animation_object(self.slide_sidebar)
        self.stretch_all_table_widgets()
        self.orders_history_btn.setCheckable(False)
        self.append_item_to_grid_layout()
    def handle_sidebar(self):
        sidebar_width = 153
        collapsed_width = 0
        # <>
        main_width = self.width()
        print(self.slide_sidebar.width())
        if self.slide_sidebar.width() == 0:
            # sidebar is opening

            self.slide_sidebar_animation_handler.setStartValue(QRect(61, 1, collapsed_width, self.height()))
            self.slide_sidebar_animation_handler.setEndValue(QRect(61, 1, sidebar_width, self.height()))

            self.inside_container_animation_handler.setStartValue(
                QRect(61, 1, self.inside_container.width(), self.height()))
            self.inside_container_animation_handler.setEndValue(
                QRect(61 + sidebar_width, 1, main_width - (61 + sidebar_width), self.height()))
        else:

            # sidebar is closing
            self.slide_sidebar_animation_handler.setStartValue(QRect(61, 1, sidebar_width, self.height()))
            self.slide_sidebar_animation_handler.setEndValue(QRect(61, 1, collapsed_width, self.height()))

            self.inside_container_animation_handler.setStartValue(
                QRect(61 + sidebar_width, 1, self.inside_container.width(), self.height()))
            self.inside_container_animation_handler.setEndValue(QRect(61, 1, main_width - 61, self.height()))

        self.slide_sidebar_animation_handler.start()
        self.inside_container_animation_handler.start()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self._drag_position)
            self.move(self.pos() + delta)
            self._drag_position = event.globalPosition().toPoint()
    def mouseReleaseEvent(self, event):
        self._drag_position = QPoint()
    def create_animation_object(self,input_frame: QFrame,duration = 300,animation_type = b"geometry") -> QPropertyAnimation:
        qproperty_animation_object = QPropertyAnimation(
            input_frame,
            animation_type
        )
        qproperty_animation_object.setDuration(duration)
        return qproperty_animation_object
    def set_all_signals(self):
       self.active_orders_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
       self.orders_history_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
       self.orders_screen_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
       self.endorsement_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(3))
       self.close_btn.clicked.connect(self.close)
       self.minimize_btn.clicked.connect(self.showMinimized)
       self.maximize_btn.clicked.connect(self.showMaximized)
       self.sidebar_toggle_btn.clicked.connect(self.handle_sidebar)
    def stretch_all_table_widgets(self):
        #NOTE -> FindChildren returns many objects
        #NOTE -> FindChild return just one objects
        table_widgets = self.stackedWidget.findChildren(QTableWidget)
        for table_widget in table_widgets:
            print(table_widget)
            table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def append_item_to_grid_layout(self):
        grid_layout = QGridLayout()
        embed_stacked_widget = self.stackedWidget.findChild(QStackedWidget)
        scroll_area = embed_stacked_widget.findChild(QScrollArea)

        for index in range(0,18):
            row = index // 3
            col = index % 3
            card_widget = QCardWidget(label_text=f"Masa {row}",image = os.path.join(os.path.dirname(__file__),"..","assets","table32px.png"))
            card_widget.mouse_long_press.connect(lambda:print("Omygod"))

            grid_layout.addWidget(card_widget,col,row)
        scroll_area.setLayout(grid_layout)
    def kill_timer(self):
        f = QMessageBox()
        f.setText("Uzun basma aktif")
        f.exec()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AsenaMainWindow()
    window.show()
    app.exec()