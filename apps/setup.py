import os
import sys

from pandas.core.dtypes.base import Registry

sys.path.append(os.path.join(os.path.dirname(__file__),".."))


from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog
from models.setup_model import Ui_Form

from enums.defaults import Defaults
from utils.fs import WriteOk,ReadOk,copyfile2dst
from source.setup import SetupModule
from source.setup import Signals
from source.setup import ThreadWorker
from utils.log_utils import create_new_logger_instance
from utils.log_utils import pack_log_files
logger = create_new_logger_instance(Defaults.DEFAULT_LOG_FILE_PATH)

class SetupUI(QWidget,Ui_Form):
    """
    kod düzenlemesi yapılacak
    text_edit min'den max'e çekilecek
    """
    def __init__(self):
        super(SetupUI,self).__init__()
        self.setupUi(self)
        self.set_line_edit_path()
        self.set_all_signals()

    def launch_file_dialog(self):
        file_dialog_window = QFileDialog()
        file_dialog_window.setWindowTitle("Patika seçin ")
        file_dialog_window.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        file_dialog_window.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog_window.exec()
        directory = file_dialog_window.selectedFiles()[0].replace("/","\\")
        if not WriteOk(directory) and not ReadOk(directory): # path has no write/read permission
            message_box = QMessageBox()
            message_box.setText("Uygun olmayan patika :/ seçilen patika uygun özellikleri taşımıyor :/ (R/W)")
            message_box.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.setWindowTitle("Hata")
            message_box.exec()
        else:
            self.path_line_edit.setText(directory)
    def setup(self):
        self.status_line.setMaximumHeight(Defaults.DEFAULT_MAX_WINDOW_SIZE)
        self.qmain_thread = QThreadPool().globalInstance()
        self.signals = Signals()
        setup_handler = SetupModule(__file__,self.persistance_btn.isChecked(),self.path_line_edit.text())
        setup_handler.signal_function = self.signals.progress.emit
        self.signals.progress.connect(self.setup_progress)
        self.worker = ThreadWorker(setup_handler)
        self.qmain_thread.start(self.worker)

    def set_all_signals(self):
        self.file_dialog_btn.clicked.connect(self.launch_file_dialog)
        self.setup_btn.clicked.connect(self.setup)
    def set_line_edit_path(self):
        self.path_line_edit.mousePressEvent = self.reset_line_edit
        self.path_line_edit.setText(Defaults.DEFAULT_SETUP_PATH)
    def reset_line_edit(self,*args,**kwargs):
        self.path_line_edit.setText(Defaults.DEFAULT_SETUP_PATH)
    def setup_progress(self,intuple: tuple):
        crash_text = intuple[0]
        progress_status = intuple[1] #
        if not progress_status:
            msgbox = QMessageBox()
            msgbox.setText(crash_text)
            msgbox.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
            msgbox.setWindowTitle("Hata")
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            self.copy_crash_logs()
            pack_log_files()
            self.close()
        else:
            self.status_line.append(crash_text)
    def copy_crash_logs(self):
        copyfile2dst(Defaults.DEFAULT_LOG_FILE_PATH,r"C:\Users\alper\OneDrive\Desktop\setup.log")
if __name__ == "__main__":
    app = QApplication([])
    window = SetupUI()
    window.show()
    app.exec()