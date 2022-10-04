# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_alterar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 450)
        Form.setMinimumSize(QSize(450, 450))
        Form.setMaximumSize(QSize(450, 450))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(Form)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pagina_login = QStackedWidget(self.frame_10)
        self.pagina_login.setObjectName(u"pagina_login")
        self.alterar_senha = QWidget()
        self.alterar_senha.setObjectName(u"alterar_senha")
        self.verticalLayout_4 = QVBoxLayout(self.alterar_senha)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 77, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.frame_14 = QFrame(self.alterar_senha)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(200, 50))
        self.frame_14.setMaximumSize(QSize(200, 50))
        self.frame_14.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_14)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")
        font = QFont()
        font.setFamily(u"Bell MT")
        font.setPointSize(18)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_31, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.label_33 = QLabel(self.alterar_senha)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(200, 0))
        self.label_33.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamily(u"Bell MT")
        font1.setPointSize(11)
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.entry_alterarsenha = QLineEdit(self.alterar_senha)
        self.entry_alterarsenha.setObjectName(u"entry_alterarsenha")
        self.entry_alterarsenha.setMinimumSize(QSize(200, 40))
        self.entry_alterarsenha.setMaximumSize(QSize(200, 40))
        self.entry_alterarsenha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_alterarsenha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.entry_alterarsenha, 0, Qt.AlignHCenter)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_pesquisar_6 = QPushButton(self.alterar_senha)
        self.btn_pesquisar_6.setObjectName(u"btn_pesquisar_6")
        self.btn_pesquisar_6.setMinimumSize(QSize(110, 40))
        self.btn_pesquisar_6.setMaximumSize(QSize(110, 40))
        self.btn_pesquisar_6.setFont(font1)
        self.btn_pesquisar_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_6.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_pesquisar_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_6 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.pagina_login.addWidget(self.alterar_senha)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_3 = QVBoxLayout(self.login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 77, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_13 = QFrame(self.login)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 50))
        self.frame_13.setMaximumSize(QSize(200, 50))
        self.frame_13.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_13)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_29, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_13, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_32 = QLabel(self.login)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(200, 0))
        self.label_32.setMaximumSize(QSize(200, 16777215))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_32, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.entry_senhalogin = QLineEdit(self.login)
        self.entry_senhalogin.setObjectName(u"entry_senhalogin")
        self.entry_senhalogin.setMinimumSize(QSize(200, 40))
        self.entry_senhalogin.setMaximumSize(QSize(200, 40))
        self.entry_senhalogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_senhalogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_senhalogin, 0, Qt.AlignHCenter)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_pesquisar_4 = QPushButton(self.login)
        self.btn_pesquisar_4.setObjectName(u"btn_pesquisar_4")
        self.btn_pesquisar_4.setMinimumSize(QSize(110, 40))
        self.btn_pesquisar_4.setMaximumSize(QSize(110, 40))
        self.btn_pesquisar_4.setFont(font1)
        self.btn_pesquisar_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_4.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_pesquisar_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pagina_login.addWidget(self.login)

        self.verticalLayout.addWidget(self.pagina_login)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.retranslateUi(Form)

        self.pagina_login.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Mudar senha", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Digite sua nova senha:", None))
        self.entry_alterarsenha.setPlaceholderText("")
        self.btn_pesquisar_6.setText(QCoreApplication.translate("Form", u"Alterar", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Digite sua senha:", None))
        self.entry_senhalogin.setPlaceholderText("")
        self.btn_pesquisar_4.setText(QCoreApplication.translate("Form", u"Entrar", None))
    # retranslateUi

