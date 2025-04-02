import os
import sys
import time

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from PySide6.QtCore import QTimer,Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog
from models.setup_model import Ui_Form
class SetupUI(QWidget,Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setup_path.mousePressEvent = self.open_file_dialog # its calls a function when press on linedit
        self.setWindowTitle("Asena - Setup")
        self.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        self.default_path = r"C:\Users\alper\Desktop"
        self.setup_path.setText(self.default_path)
        self.set_all_signals()
    def open_file_dialog(self,*args,**kwargs):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)
        file_dialog.exec()
        directory = file_dialog.selectedFiles()
        if len(directory) > 0:
            directory = directory[0]
            self.setup_path.setText(directory.replace("/","\\"))
    def set_all_signals(self):
        self.exit_btn.clicked.connect(lambda:self.close())
        self.setup_btn.clicked.connect(self.write_random)
    def write_random(self):
        self.setup_path.mousePressEvent = lambda *args:None
        self.setup_path.setReadOnly(True)
        actions = [
            "Dosyalar kopyalanıyor...",
            "Kayıt defterine güncellemeler yapılıyor...",
            "Kısayollar oluşturuluyor....",

        ]
        files = [file for file in self.walk_path(os.path.join(os.path.dirname(__file__),".."))]
        files_len = len(files)
        print(files_len)
        files = iter(files)
        for counter in range(files_len):
            QTimer.singleShot(counter * 200,lambda:self.textEdit.append("Dosya kopyalanıyor: %s" % next(files)))


    def walk_path(self,path: str):
        for root,_,files in os.walk(path):
            for file in files:
                path = os.path.join(root,file)
                if os.path.splitext(path)[1] == ".py":
                    yield path
    def append_text(self,text: str):
        self.action_list.append(text)
if __name__ == "__main__":
    app = QApplication([])
    window = SetupUI()
    window.show()
    app.exec()