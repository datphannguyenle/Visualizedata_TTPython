from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from rc_images import *
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

##############################################################################
# -*- coding: utf-8 -*-

################################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 818)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 0px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tieude = QFrame(self.frame)
        self.tieude.setObjectName(u"tieude")
        self.tieude.setStyleSheet(u"border-radius:30px;\n"
"")
        self.tieude.setFrameShape(QFrame.StyledPanel)
        self.tieude.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.tieude)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo = QFrame(self.tieude)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"background: none;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo_img = QLabel(self.logo)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setStyleSheet(u"background-color: none;\n"
"\n"
"image: url(:/images/images/logos/ute_logo.png);")

        self.verticalLayout_3.addWidget(self.logo_img)


        self.horizontalLayout_2.addWidget(self.logo)

        self.text = QFrame(self.tieude)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"background: none;")
        self.text.setFrameShape(QFrame.StyledPanel)
        self.text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tendetai = QLabel(self.text)
        self.tendetai.setObjectName(u"tendetai")
        self.tendetai.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 italic 19pt \"League Spartan\";\n"
"background-color: none;\n"
"")

        self.verticalLayout_2.addWidget(self.tendetai)

        self.tacgia = QLabel(self.text)
        self.tacgia.setObjectName(u"tacgia")
        self.tacgia.setStyleSheet(u"background-color: none;\n"
"")

        self.verticalLayout_2.addWidget(self.tacgia)


        self.horizontalLayout_2.addWidget(self.text)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 20)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout_6.addWidget(self.tieude)

        self.main = QFrame(self.frame)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"border-radius:30px;\n"
"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_1 = QFrame(self.main)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grafica_uno = QVBoxLayout()
        self.grafica_uno.setObjectName(u"grafica_uno")

        self.verticalLayout_4.addLayout(self.grafica_uno)

        self.verticalLayout_4.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_1, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.grafica_dos = QVBoxLayout()
        self.grafica_dos.setObjectName(u"grafica_dos")

        self.verticalLayout_5.addLayout(self.grafica_dos)

        self.verticalLayout_5.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.grafica_tres = QVBoxLayout()
        self.grafica_tres.setObjectName(u"grafica_tres")

        self.verticalLayout_7.addLayout(self.grafica_tres)

        self.verticalLayout_7.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.grafica_cuatro = QVBoxLayout()
        self.grafica_cuatro.setObjectName(u"grafica_cuatro")

        self.verticalLayout_8.addLayout(self.grafica_cuatro)

        self.verticalLayout_8.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.main)

        self.button = QFrame(self.frame)
        self.button.setObjectName(u"button")
        self.button.setStyleSheet(u"border-radius:30px;\n"
"")
        self.button.setFrameShape(QFrame.StyledPanel)
        self.button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.button)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background: none;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.load_button = QPushButton(self.frame_6)
        self.load_button.setObjectName(u"load_button")
        font = QFont()
        font.setPointSize(10)
        self.load_button.setFont(font)
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_3.addWidget(self.load_button)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.start_button = QPushButton(self.frame_6)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setFont(font)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_3.addWidget(self.start_button)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.button)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(328, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.exit_button = QPushButton(self.frame_5)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(237, 51, 59);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_4.addWidget(self.exit_button)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.button)

        self.verticalLayout_6.setStretch(1, 9)
        self.verticalLayout_6.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
#if QT_CONFIG(tooltip)
        self.tendetai.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tendetai.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tendetai.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-style:normal;\">Visualize Data Software</span></p></body></html>", None))
        self.tacgia.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">BY: LE PHAN NGUYEN DAT 20139037 - NGUYEN HOAI TAM 20139012</span></p></body></html>", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

