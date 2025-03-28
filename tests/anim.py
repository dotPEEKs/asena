from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QPropertyAnimation, QRect

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)  # Pencere boyutu
        self.sidebar_width = 60  # Kapalı sidebar genişliği
        self.expanded_width = 200  # Açık sidebar genişliği

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setStyleSheet("background-color: #333;")
        self.sidebar.setGeometry(0, 0, self.sidebar_width, 400)

        # Yanındaki Frame
        self.frame = QWidget(self)
        self.frame.setStyleSheet("background-color: #555;")
        self.frame.setGeometry(self.sidebar_width, 0, 540, 400)

        # Aç/Kapat Butonu
        self.button = QPushButton("☰", self.sidebar)
        self.button.setGeometry(10, 10, 40, 30)
        self.button.clicked.connect(self.toggle_sidebar)

        # Animasyonlar
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"geometry")
        self.frame_animation = QPropertyAnimation(self.frame, b"geometry")

    def toggle_sidebar(self):
        if self.sidebar.width() == self.sidebar_width:
            # Aç: Sidebar genişlet, frame'i sağa kaydır
            self.sidebar_animation.setStartValue(QRect(0, 0, self.sidebar_width, self.height()))
            self.sidebar_animation.setEndValue(QRect(0, 0, self.expanded_width, self.height()))

            self.frame_animation.setStartValue(QRect(self.sidebar_width, 0, 540, self.height()))
            self.frame_animation.setEndValue(QRect(self.expanded_width, 0, 400, self.height()))
        else:
            # Kapat: Sidebar küçült, frame'i eski yerine getir
            self.sidebar_animation.setStartValue(QRect(0, 0, self.expanded_width, self.height()))
            self.sidebar_animation.setEndValue(QRect(0, 0, self.sidebar_width, self.height()))

            self.frame_animation.setStartValue(QRect(self.expanded_width, 0, 400, self.height()))
            self.frame_animation.setEndValue(QRect(self.sidebar_width, 0, 540, self.height()))

        # Animasyon süresi (milisaniye)
        self.sidebar_animation.setDuration(300)
        self.frame_animation.setDuration(300)

        # Animasyonları başlat
        self.sidebar_animation.start()
        self.frame_animation.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()