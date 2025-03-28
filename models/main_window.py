# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 529)
        MainWindow.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background-color: none;\n"
"	font: 700 11pt \"Arial\";\n"
"	height: 38px;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(859, 529))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minisidebar = QFrame(self.main_container)
        self.minisidebar.setObjectName(u"minisidebar")
        self.minisidebar.setMaximumSize(QSize(60, 16777215))
        self.minisidebar.setStyleSheet(u"QPushButton {\n"
"	height: 38px;\n"
"}	")
        self.minisidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.minisidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.minisidebar)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.minisidebar_active_orders_btn = QPushButton(self.minisidebar)
        self.minisidebar_active_orders_btn.setObjectName(u"minisidebar_active_orders_btn")
        icon = QIcon()
        icon.addFile(u":/resources/already_waiting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_active_orders_btn.setIcon(icon)
        self.minisidebar_active_orders_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_active_orders_btn)

        self.minisidebar_orders_history_btn = QPushButton(self.minisidebar)
        self.minisidebar_orders_history_btn.setObjectName(u"minisidebar_orders_history_btn")
        icon1 = QIcon()
        icon1.addFile(u":/resources/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_orders_history_btn.setIcon(icon1)
        self.minisidebar_orders_history_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_orders_history_btn)

        self.minisidebar_orders_screen_btn = QPushButton(self.minisidebar)
        self.minisidebar_orders_screen_btn.setObjectName(u"minisidebar_orders_screen_btn")
        icon2 = QIcon()
        icon2.addFile(u":/resources/orders.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_orders_screen_btn.setIcon(icon2)
        self.minisidebar_orders_screen_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_orders_screen_btn)

        self.minisidenar_endorsement_btn = QPushButton(self.minisidebar)
        self.minisidenar_endorsement_btn.setObjectName(u"minisidenar_endorsement_btn")
        icon3 = QIcon()
        icon3.addFile(u":/resources/endorsement_btn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidenar_endorsement_btn.setIcon(icon3)
        self.minisidenar_endorsement_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidenar_endorsement_btn)

        self.minisidebar_stock_management_btn = QPushButton(self.minisidebar)
        self.minisidebar_stock_management_btn.setObjectName(u"minisidebar_stock_management_btn")
        icon4 = QIcon()
        icon4.addFile(u":/resources/database_btn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_stock_management_btn.setIcon(icon4)
        self.minisidebar_stock_management_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_stock_management_btn)

        self.minisidebar_settings_btn = QPushButton(self.minisidebar)
        self.minisidebar_settings_btn.setObjectName(u"minisidebar_settings_btn")
        icon5 = QIcon()
        icon5.addFile(u":/resources/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_settings_btn.setIcon(icon5)
        self.minisidebar_settings_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_settings_btn)

        self.minisidebar_exit_btn = QPushButton(self.minisidebar)
        self.minisidebar_exit_btn.setObjectName(u"minisidebar_exit_btn")
        icon6 = QIcon()
        icon6.addFile(u":/resources/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_exit_btn.setIcon(icon6)
        self.minisidebar_exit_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_exit_btn)

        self.verticalSpacer = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.minisidebar)

        self.slide_sidebar = QFrame(self.main_container)
        self.slide_sidebar.setObjectName(u"slide_sidebar")
        self.slide_sidebar.setMaximumSize(QSize(200, 16777215))
        self.slide_sidebar.setStyleSheet(u"")
        self.slide_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_sidebar)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, -1, 0)
        self.active_orders_btn = QPushButton(self.slide_sidebar)
        self.active_orders_btn.setObjectName(u"active_orders_btn")

        self.verticalLayout_2.addWidget(self.active_orders_btn)

        self.orders_history_btn = QPushButton(self.slide_sidebar)
        self.orders_history_btn.setObjectName(u"orders_history_btn")

        self.verticalLayout_2.addWidget(self.orders_history_btn)

        self.orders_screen_btn = QPushButton(self.slide_sidebar)
        self.orders_screen_btn.setObjectName(u"orders_screen_btn")

        self.verticalLayout_2.addWidget(self.orders_screen_btn)

        self.endorsement_btn = QPushButton(self.slide_sidebar)
        self.endorsement_btn.setObjectName(u"endorsement_btn")

        self.verticalLayout_2.addWidget(self.endorsement_btn)

        self.stock_management_btn = QPushButton(self.slide_sidebar)
        self.stock_management_btn.setObjectName(u"stock_management_btn")

        self.verticalLayout_2.addWidget(self.stock_management_btn)

        self.settings_btn = QPushButton(self.slide_sidebar)
        self.settings_btn.setObjectName(u"settings_btn")

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.exit_btn = QPushButton(self.slide_sidebar)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout_2.addWidget(self.exit_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.slide_sidebar)

        self.inside_container = QFrame(self.main_container)
        self.inside_container.setObjectName(u"inside_container")
        sizePolicy.setHeightForWidth(self.inside_container.sizePolicy().hasHeightForWidth())
        self.inside_container.setSizePolicy(sizePolicy)
        self.inside_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.inside_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.inside_container)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.inside_container)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 50))
        self.header_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, 0, 0)
        self.sidebar_toggle_btn_frame = QFrame(self.header_frame)
        self.sidebar_toggle_btn_frame.setObjectName(u"sidebar_toggle_btn_frame")
        self.sidebar_toggle_btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar_toggle_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_toggle_btn_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 3, 0, 0)
        self.sidebar_toggle_btn = QPushButton(self.sidebar_toggle_btn_frame)
        self.sidebar_toggle_btn.setObjectName(u"sidebar_toggle_btn")
        icon7 = QIcon()
        icon7.addFile(u":/resources/sidebar_toggle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sidebar_toggle_btn.setIcon(icon7)
        self.sidebar_toggle_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.sidebar_toggle_btn, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_3.addWidget(self.sidebar_toggle_btn_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.main_label_frame = QFrame(self.header_frame)
        self.main_label_frame.setObjectName(u"main_label_frame")
        self.main_label_frame.setMaximumSize(QSize(196, 44))
        self.main_label_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_label_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_label_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.app_name_label = QLabel(self.main_label_frame)
        self.app_name_label.setObjectName(u"app_name_label")

        self.horizontalLayout_5.addWidget(self.app_name_label)

        self.app_icon_label = QLabel(self.main_label_frame)
        self.app_icon_label.setObjectName(u"app_icon_label")
        self.app_icon_label.setPixmap(QPixmap(u":/resources/asena_main.ico"))

        self.horizontalLayout_5.addWidget(self.app_icon_label)


        self.horizontalLayout_3.addWidget(self.main_label_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.corner_button_frame = QFrame(self.header_frame)
        self.corner_button_frame.setObjectName(u"corner_button_frame")
        self.corner_button_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.corner_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.corner_button_frame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 6, 0)
        self.minimize_btn = QPushButton(self.corner_button_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(16, 16))
        self.minimize_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/resources/minimize_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon8)
        self.minimize_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.corner_button_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(16, 16))
        icon9 = QIcon()
        icon9.addFile(u":/resources/fullscreen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_btn.setIcon(icon9)
        self.maximize_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.corner_button_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(16, 16))
        icon10 = QIcon()
        icon10.addFile(u":/resources/close_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon10)
        self.close_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.corner_button_frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_page = QFrame(self.inside_container)
        self.main_page.setObjectName(u"main_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_page.sizePolicy().hasHeightForWidth())
        self.main_page.setSizePolicy(sizePolicy1)
        self.main_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_page.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.embed_frame = QFrame(self.main_page)
        self.embed_frame.setObjectName(u"embed_frame")
        self.embed_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.embed_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.embed_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.horizontalLayout_7.addWidget(self.embed_frame)


        self.verticalLayout.addWidget(self.main_page)


        self.horizontalLayout_2.addWidget(self.inside_container)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minisidebar_active_orders_btn.setText("")
        self.minisidebar_orders_history_btn.setText("")
        self.minisidebar_orders_screen_btn.setText("")
        self.minisidenar_endorsement_btn.setText("")
        self.minisidebar_stock_management_btn.setText("")
        self.minisidebar_settings_btn.setText("")
        self.minisidebar_exit_btn.setText("")
        self.active_orders_btn.setText(QCoreApplication.translate("MainWindow", u"AKTIF SIPARI\u015eLER", None))
        self.orders_history_btn.setText(QCoreApplication.translate("MainWindow", u"SIPARI\u015e GE\u00c7MI\u015eI", None))
        self.orders_screen_btn.setText(QCoreApplication.translate("MainWindow", u"SIPARI\u015e EKRANI", None))
        self.endorsement_btn.setText(QCoreApplication.translate("MainWindow", u"CIRO TAK\u0130B\u0130", None))
        self.stock_management_btn.setText(QCoreApplication.translate("MainWindow", u"STOK YONETIMI", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"AYARLAR", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u00c7IKI\u015e", None))
        self.sidebar_toggle_btn.setText("")
        self.app_name_label.setText(QCoreApplication.translate("MainWindow", u"ASENA", None))
        self.app_icon_label.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi

