import os
import sys
import winreg

from PySide6.QtCore import QSize

sys.path.append(os.path.join(os.path.dirname(__file__),".."))


from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog
from models.setup_model import Ui_Form
from utils.reg_utils import Registry,HKEY
from utils.fs import WriteOk,ReadOk
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
        self.registry = Registry(HKEY.HKEY_CURRENT_USER,r"Software\Asena")
    def open_file_dialog(self,*args,**kwargs):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Kurulum patikası seçiniz !")
        file_dialog.setFileMode(QFileDialog.Directory)
        file_dialog.exec()
        directory = file_dialog.selectedFiles()
        if len(directory) > 0:
            directory = directory[0].replace("/","\\")
            if WriteOk(directory) and ReadOk(directory):
                self.setup_path.setText(directory)
            else:
                message_box = QMessageBox()
                message_box.setWindowTitle("Hata")
                message_box.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
                message_box.setText("Verilen klasör kurulum için uygunsuz (Gerekli izinlere sahip değil (read/write))")
                message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                message_box.exec()
    def set_all_signals(self):
        self.exit_btn.clicked.connect(lambda:self.close())
        self.setup_btn.clicked.connect(self.handle_setup_progress)
    def append_text(self,text: str):
        self.action_list.append(text)
    def create_required_registry_keys(self):
        setup_path = "\"%s\"" % (os.path.join(self.setup_path.text(),"asena.exe"))
        if self.persistance_btn.isChecked():
            self.registry.sub_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            reg_handler.write_key("Asena","\"%s\"" % (setup_path))
        self.registry.sub_path = r"Software\Asena"
        self.registry.write_key("SetupPath",setup_path)
        self.registry.write_key("DividedSalt",os.urandom(100),data_type = winreg.REG_BINARY)

    def handle_setup_progress(self):
        # disable line edit events
        self.setup_path.mousePressEvent = lambda *args:None # Void lambda function
        self.setup_path.setReadOnly(True)
        self.create_required_registry_keys()

if __name__ == "__main__":
    app = QApplication([])
    window = SetupUI()
    window.show()
    app.exec()