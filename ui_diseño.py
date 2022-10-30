# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui_v3QGXdTL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from rc_images import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 818)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius:30px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tieude = QFrame(self.frame)
        self.tieude.setObjectName(u"tieude")
        self.tieude.setStyleSheet(u"")
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

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 10)

        self.verticalLayout_6.addWidget(self.tieude)

        self.main = QFrame(self.frame)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_1 = QFrame(self.main)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"background: none;")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grafica_uno = QVBoxLayout()
        self.grafica_uno.setObjectName(u"grafica_uno")

        self.verticalLayout_4.addLayout(self.grafica_uno)

        self.name_chart_1 = QLabel(self.frame_1)
        self.name_chart_1.setObjectName(u"name_chart_1")
        self.name_chart_1.setStyleSheet(u"background: none;")

        self.verticalLayout_4.addWidget(self.name_chart_1)

        self.verticalLayout_4.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_1, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.grafica_dos = QVBoxLayout()
        self.grafica_dos.setObjectName(u"grafica_dos")

        self.verticalLayout_5.addLayout(self.grafica_dos)

        self.name_chart_2 = QLabel(self.frame_2)
        self.name_chart_2.setObjectName(u"name_chart_2")
        self.name_chart_2.setStyleSheet(u"background: none;")

        self.verticalLayout_5.addWidget(self.name_chart_2)

        self.verticalLayout_5.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.grafica_tres = QVBoxLayout()
        self.grafica_tres.setObjectName(u"grafica_tres")

        self.verticalLayout_7.addLayout(self.grafica_tres)

        self.name_chart_3 = QLabel(self.frame_3)
        self.name_chart_3.setObjectName(u"name_chart_3")
        self.name_chart_3.setStyleSheet(u"background: none;")

        self.verticalLayout_7.addWidget(self.name_chart_3)

        self.verticalLayout_7.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.grafica_cuatro = QVBoxLayout()
        self.grafica_cuatro.setObjectName(u"grafica_cuatro")

        self.verticalLayout_8.addLayout(self.grafica_cuatro)

        self.name_chart_4 = QLabel(self.frame_4)
        self.name_chart_4.setObjectName(u"name_chart_4")
        self.name_chart_4.setStyleSheet(u"background: none;")

        self.verticalLayout_8.addWidget(self.name_chart_4)

        self.verticalLayout_8.setStretch(0, 5)

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.main)

        self.button = QFrame(self.frame)
        self.button.setObjectName(u"button")
        self.button.setStyleSheet(u"")
        self.button.setFrameShape(QFrame.StyledPanel)
        self.button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.load_button = QPushButton(self.button)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.load_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lineEdit = QLineEdit(self.button)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.start_button = QPushButton(self.button)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.start_button)

        self.horizontalSpacer = QSpacerItem(216, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exit_button = QPushButton(self.button)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout.addWidget(self.exit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 3)
        self.horizontalLayout.setStretch(7, 1)

        self.verticalLayout_6.addWidget(self.button)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 8)
        self.verticalLayout_6.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 22))
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
        self.name_chart_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean \u0111\u1ed3 th\u1ecb 1</span></p></body></html>", None))
        self.name_chart_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean \u0111\u1ed3 th\u1ecb 2</span></p></body></html>", None))
        self.name_chart_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean \u0111\u1ed3 th\u1ecb 3</span></p></body></html>", None))
        self.name_chart_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean \u0111\u1ed3 th\u1ecb 4</span></p></body></html>", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
'''
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dise�odnqowz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 497)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"border: none;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.grafica_uno = QVBoxLayout()
        self.grafica_uno.setObjectName(u"grafica_uno")

        self.verticalLayout_3.addLayout(self.grafica_uno)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"border: none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.grafica_dos = QVBoxLayout()
        self.grafica_dos.setObjectName(u"grafica_dos")

        self.verticalLayout_4.addLayout(self.grafica_dos)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"border: none;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.grafica_tres = QVBoxLayout()
        self.grafica_tres.setObjectName(u"grafica_tres")

        self.verticalLayout_6.addLayout(self.grafica_tres)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"border: none;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.grafica_cuatro = QVBoxLayout()
        self.grafica_cuatro.setObjectName(u"grafica_cuatro")

        self.verticalLayout_8.addLayout(self.grafica_cuatro)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)

        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Graficas Matplotlib", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Grafica N\u00b0 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Grafica N\u00b0 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Grafica N\u00b0 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Grafica N\u00b0 4", None))
    # retranslateUi

'''