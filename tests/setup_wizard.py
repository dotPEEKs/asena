import os,sys

from PySide6.QtCore import QTimer,QRect,Qt
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QWizard,QWizardPage,QTextEdit,QProgressBar,QSizePolicy

eula = "Bu kod ticari amaç taşımamakla beraber ticari amaçla dağıtılması kopyalanması satılması kesinlikle yasaktır\nve oluşacak herhangi kullanıcı taraflı veri kaybından kesinlikle yapımcı sorumlu değildir !"
class Wizard(QWizard):
    def __init__(self):
        super().__init__()
        self.eula_page()
    def eula_page(self):
        setup_wizard_eula_page = QWizardPage(self)
        setup_wizard_eula_page_vertical_layout = QVBoxLayout(setup_wizard_eula_page)
        text_edit = QTextEdit()
        text_edit.setText(eula)
        text_edit.setReadOnly(True)
        text_edit.setStyleSheet("font: Arial 700 11pt;")
        setup_wizard_eula_page_vertical_layout.addWidget(text_edit)
        self.addPage(setup_wizard_eula_page)
        self.set_setup_path()
    def set_setup_path(self):
        qtimer = QTimer()
        qtimer.setInterval(50)
        setup_wizard_setup_page = QWizardPage(self)
        setup_wizard_setup_page_vertical_layout = QVBoxLayout(setup_wizard_setup_page)
        setup_wizard_setup_page.setLayout(setup_wizard_setup_page_vertical_layout)
        setup_wizard_setup_page_progress_bar = QProgressBar()
        setup_wizard_setup_page_progress_bar.setStyleSheet("\nborder-radius: 5px;\nbackground-color: 'blue';")
        setup_wizard_setup_page_progress_bar.setStyleSheet("QProgressBar::chunk {\n\tborder-radius: 6px\n\twidth: 7px;\nbackground-color: 'red';\n;}")
        setup_wizard_setup_page_progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        setup_wizard_setup_page_progress_bar.setMaximum(100)
        setup_wizard_setup_page_progress_bar.setMinimum(0)
        push_button = QPushButton("Tıkla")
        qtimer.timeout.connect(lambda:setup_wizard_setup_page_progress_bar.setValue(setup_wizard_setup_page_progress_bar.value() + 1))
        push_button.clicked.connect(lambda:qtimer.start())
        setup_wizard_setup_page_vertical_layout.addWidget(setup_wizard_setup_page_progress_bar)
        setup_wizard_setup_page_vertical_layout.addWidget(push_button)
        self.addPage(setup_wizard_setup_page)

app = QApplication([])
setup_wizard = Wizard()
setup_wizard.show()
app.exec()