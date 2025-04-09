import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from PySide6.QtWidgets import QWidget,QApplication
from test_ui import Ui_Form
from source.backend.setup_backend import SetupBackend
from source.Qthread import QThreadWorker

class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.module = SetupBackend()
        self.thread_worker = QThreadWorker(self.module)
        self.module.register_slot(self.set_label_test)
        self.pushButton.clicked.connect(self.thread_worker.start)
    def set_label_test(self,msg):
        self.label.setText(msg.value)
app = QApplication([])
window = Main()
window.show()
app.exec()