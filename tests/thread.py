# Mantık nasıl işliyor ?

# İlk önce işçi bir sınıf hazırlıyoruz (Worker)


# ardından sinyalleri işleyen bir sınıf hazırlıyoruz (Signals)

# worker sınıfındaki sinyali işleyebilmek için ilgili sinyalin connect fonksiyonunu kullanıyoruz yani

# emit edildiğinde önceden connect ile belirlenen fonksiyon çalıştırılıyor

# Ardından qthreadpool ile işçi sınıfı run ediyoruz

# run fonksiyonu her bi işlem değişikliğinde Signals class'nın içersindeki label_signal'i emit ediyor



import time
from PySide6.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QVBoxLayout,QWidget
from PySide6.QtCore import Qt,QObject,Signal,QRunnable,QThreadPool
from typing import override
class Signals(QObject):
    label_signal = Signal(str)

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
    @override
    def run(self):
        for text in ["Uploading","Downloading","Dümendening","Cart","Curt"]:
            self.signals.label_signal.emit(text)
            time.sleep(5)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.threadpool = QThreadPool.globalInstance()
        self.setCentralWidget(self.widget)
        self.hlayout = QVBoxLayout(self.widget)
        self.label = QLabel("Not Yet")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hlayout.addWidget(self.label)
        self.push_button = QPushButton("Hello")
        self.push_button.clicked.connect(self.start_thread)
        self.hlayout.addWidget(self.push_button)
    def start_thread(self):
        worker = Worker()
        worker.signals.label_signal.connect(lambda param:self.label.setText(param))
        self.threadpool.start(worker)
app = QApplication([])
window = Window()
window.show()
app.exec()