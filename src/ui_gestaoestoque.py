# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestaoestoque.ui'
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
        MainWindow.resize(898, 532)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer)

        self.btn_realizarvenda = QPushButton(self.frame)
        self.btn_realizarvenda.setObjectName(u"btn_realizarvenda")
        self.btn_realizarvenda.setMinimumSize(QSize(0, 30))
        self.btn_realizarvenda.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Bell MT")
        font.setPointSize(12)
        self.btn_realizarvenda.setFont(font)
        self.btn_realizarvenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_realizarvenda.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_35.addWidget(self.btn_realizarvenda)

        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_35.addWidget(self.btn_cadastrar)

        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(0, 30))
        self.btn_estoque.setMaximumSize(QSize(16777215, 30))
        self.btn_estoque.setFont(font)
        self.btn_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_35.addWidget(self.btn_estoque)

        self.btn_entradaesaida = QPushButton(self.frame)
        self.btn_entradaesaida.setObjectName(u"btn_entradaesaida")
        self.btn_entradaesaida.setMinimumSize(QSize(0, 30))
        self.btn_entradaesaida.setMaximumSize(QSize(16777215, 30))
        self.btn_entradaesaida.setFont(font)
        self.btn_entradaesaida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entradaesaida.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_35.addWidget(self.btn_entradaesaida)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.inicial = QWidget()
        self.inicial.setObjectName(u"inicial")
        self.verticalLayout_7 = QVBoxLayout(self.inicial)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.entry_pesquisar = QLineEdit(self.inicial)
        self.entry_pesquisar.setObjectName(u"entry_pesquisar")
        self.entry_pesquisar.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.entry_pesquisar)

        self.btn_pesquisar = QPushButton(self.inicial)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamily(u"Bell MT")
        font1.setPointSize(11)
        self.btn_pesquisar.setFont(font1)
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_pesquisar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_pesquisa = QTableWidget(self.inicial)
        if (self.tb_pesquisa.columnCount() < 6):
            self.tb_pesquisa.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_pesquisa.setObjectName(u"tb_pesquisa")
        self.tb_pesquisa.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_pesquisa.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_pesquisa.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_pesquisa.setShowGrid(True)

        self.horizontalLayout_4.addWidget(self.tb_pesquisa)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.entry_quantidade_2 = QLineEdit(self.inicial)
        self.entry_quantidade_2.setObjectName(u"entry_quantidade_2")
        self.entry_quantidade_2.setMinimumSize(QSize(100, 30))
        self.entry_quantidade_2.setMaximumSize(QSize(100, 30))
        self.entry_quantidade_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.entry_quantidade_2)

        self.btn_inserirnocarrinho = QPushButton(self.inicial)
        self.btn_inserirnocarrinho.setObjectName(u"btn_inserirnocarrinho")
        self.btn_inserirnocarrinho.setMinimumSize(QSize(110, 30))
        self.btn_inserirnocarrinho.setMaximumSize(QSize(110, 30))
        font2 = QFont()
        font2.setFamily(u"Bell MT")
        font2.setPointSize(10)
        font2.setUnderline(False)
        self.btn_inserirnocarrinho.setFont(font2)
        self.btn_inserirnocarrinho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inserirnocarrinho.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.btn_inserirnocarrinho)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.inicial)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setFamily(u"Bell MT")
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.frame_2 = QFrame(self.inicial)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(700, 200))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tb_carrinho = QTableWidget(self.frame_2)
        if (self.tb_carrinho.columnCount() < 6):
            self.tb_carrinho.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_carrinho.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tb_carrinho.setObjectName(u"tb_carrinho")
        self.tb_carrinho.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_carrinho.setDragEnabled(False)
        self.tb_carrinho.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tb_carrinho.setAlternatingRowColors(True)
        self.tb_carrinho.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_carrinho.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_6.addWidget(self.tb_carrinho)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.cb_pagamento = QComboBox(self.frame_2)
        self.cb_pagamento.addItem("")
        self.cb_pagamento.addItem("")
        self.cb_pagamento.addItem("")
        self.cb_pagamento.addItem("")
        self.cb_pagamento.addItem("")
        self.cb_pagamento.setObjectName(u"cb_pagamento")
        self.cb_pagamento.setMinimumSize(QSize(110, 30))
        self.cb_pagamento.setMaximumSize(QSize(110, 30))
        self.cb_pagamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_pagamento.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-radius: 5px;")

        self.verticalLayout_6.addWidget(self.cb_pagamento)

        self.btn_finalizarvenda = QPushButton(self.frame_2)
        self.btn_finalizarvenda.setObjectName(u"btn_finalizarvenda")
        self.btn_finalizarvenda.setMinimumSize(QSize(110, 30))
        self.btn_finalizarvenda.setMaximumSize(QSize(110, 30))
        self.btn_finalizarvenda.setFont(font1)
        self.btn_finalizarvenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizarvenda.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
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

        self.verticalLayout_6.addWidget(self.btn_finalizarvenda)

        self.btn_apagaritens = QPushButton(self.frame_2)
        self.btn_apagaritens.setObjectName(u"btn_apagaritens")
        self.btn_apagaritens.setMinimumSize(QSize(110, 30))
        self.btn_apagaritens.setMaximumSize(QSize(110, 30))
        self.btn_apagaritens.setFont(font1)
        self.btn_apagaritens.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_apagaritens.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(220, 0, 0);\n"
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

        self.verticalLayout_6.addWidget(self.btn_apagaritens)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_9 = QFrame(self.inicial)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 35))
        self.frame_9.setMaximumSize(QSize(16777215, 35))
        self.frame_9.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 0))
        self.label_16.setMaximumSize(QSize(60, 16777215))
        self.label_16.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(100, 0))
        self.label_26.setMaximumSize(QSize(60, 16777215))
        self.label_26.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_7.addWidget(self.label_26)

        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 30))
        self.label_39.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_7.addWidget(self.label_39)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(60, 0))
        self.label_17.setMaximumSize(QSize(60, 16777215))
        self.label_17.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_7.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(70, 30))
        self.label_18.setMaximumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.label_18)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.inicial)
        self.cadastrarprodutos = QWidget()
        self.cadastrarprodutos.setObjectName(u"cadastrarprodutos")
        self.verticalLayout_16 = QVBoxLayout(self.cadastrarprodutos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.cadastrarprodutos)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Bell MT")
        font4.setPointSize(18)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_2)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetMinimumSize)
        self.stackedWidget_2 = QStackedWidget(self.cadastrarprodutos)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.produto = QWidget()
        self.produto.setObjectName(u"produto")
        self.gridLayout_2 = QGridLayout(self.produto)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_a = QVBoxLayout()
        self.verticalLayout_a.setObjectName(u"verticalLayout_a")
        self.label_13 = QLabel(self.produto)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_a.addWidget(self.label_13)

        self.entry_codigo = QLineEdit(self.produto)
        self.entry_codigo.setObjectName(u"entry_codigo")
        self.entry_codigo.setMinimumSize(QSize(0, 30))
        self.entry_codigo.setMaximumSize(QSize(16777215, 30))
        self.entry_codigo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_codigo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_a.addWidget(self.entry_codigo)


        self.gridLayout_2.addLayout(self.verticalLayout_a, 2, 0, 1, 1)

        self.verticalLayout_b = QVBoxLayout()
        self.verticalLayout_b.setObjectName(u"verticalLayout_b")
        self.label_4 = QLabel(self.produto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_b.addWidget(self.label_4)

        self.entry_venda = QLineEdit(self.produto)
        self.entry_venda.setObjectName(u"entry_venda")
        self.entry_venda.setMinimumSize(QSize(0, 30))
        self.entry_venda.setMaximumSize(QSize(16777215, 30))
        self.entry_venda.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout_b.addWidget(self.entry_venda)


        self.gridLayout_2.addLayout(self.verticalLayout_b, 2, 1, 1, 1)

        self.verticalLayout_c = QVBoxLayout()
        self.verticalLayout_c.setObjectName(u"verticalLayout_c")
        self.label_9 = QLabel(self.produto)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_c.addWidget(self.label_9)

        self.entry_peso = QLineEdit(self.produto)
        self.entry_peso.setObjectName(u"entry_peso")
        self.entry_peso.setMinimumSize(QSize(0, 30))
        self.entry_peso.setMaximumSize(QSize(16777215, 30))
        self.entry_peso.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_peso.setAlignment(Qt.AlignCenter)

        self.verticalLayout_c.addWidget(self.entry_peso)


        self.gridLayout_2.addLayout(self.verticalLayout_c, 3, 0, 1, 1)

        self.verticalLayout_f = QVBoxLayout()
        self.verticalLayout_f.setObjectName(u"verticalLayout_f")
        self.label_5 = QLabel(self.produto)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_f.addWidget(self.label_5)

        self.entry_custo = QLineEdit(self.produto)
        self.entry_custo.setObjectName(u"entry_custo")
        self.entry_custo.setMinimumSize(QSize(0, 30))
        self.entry_custo.setMaximumSize(QSize(16777215, 30))
        self.entry_custo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_custo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_f.addWidget(self.entry_custo)


        self.gridLayout_2.addLayout(self.verticalLayout_f, 3, 1, 1, 1)

        self.verticalLayout_d = QVBoxLayout()
        self.verticalLayout_d.setObjectName(u"verticalLayout_d")
        self.label_10 = QLabel(self.produto)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_d.addWidget(self.label_10)

        self.entry_quantidade = QLineEdit(self.produto)
        self.entry_quantidade.setObjectName(u"entry_quantidade")
        self.entry_quantidade.setMinimumSize(QSize(0, 30))
        self.entry_quantidade.setMaximumSize(QSize(16777215, 30))
        self.entry_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_d.addWidget(self.entry_quantidade)


        self.gridLayout_2.addLayout(self.verticalLayout_d, 4, 0, 1, 1)

        self.verticalLayout_e = QVBoxLayout()
        self.verticalLayout_e.setObjectName(u"verticalLayout_e")
        self.label_8 = QLabel(self.produto)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_e.addWidget(self.label_8)

        self.entry_dimensoes = QLineEdit(self.produto)
        self.entry_dimensoes.setObjectName(u"entry_dimensoes")
        self.entry_dimensoes.setMinimumSize(QSize(0, 30))
        self.entry_dimensoes.setMaximumSize(QSize(16777215, 30))
        self.entry_dimensoes.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_dimensoes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_e.addWidget(self.entry_dimensoes)


        self.gridLayout_2.addLayout(self.verticalLayout_e, 4, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.produto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.entry_nome = QLineEdit(self.produto)
        self.entry_nome.setObjectName(u"entry_nome")
        self.entry_nome.setMinimumSize(QSize(0, 30))
        self.entry_nome.setMaximumSize(QSize(16777215, 30))
        self.entry_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_nome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.entry_nome)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 0, 1, 2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.produto)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.entry_dimensoes_2 = QLineEdit(self.produto)
        self.entry_dimensoes_2.setObjectName(u"entry_dimensoes_2")
        self.entry_dimensoes_2.setMinimumSize(QSize(0, 30))
        self.entry_dimensoes_2.setMaximumSize(QSize(16777215, 30))
        self.entry_dimensoes_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_dimensoes_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.entry_dimensoes_2)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 1, 0, 1, 2)

        self.horizontalLayout_h = QHBoxLayout()
        self.horizontalLayout_h.setObjectName(u"horizontalLayout_h")
        self.btn_salvar = QPushButton(self.produto)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy1)
        self.btn_salvar.setMinimumSize(QSize(150, 40))
        self.btn_salvar.setMaximumSize(QSize(150, 40))
        self.btn_salvar.setFont(font3)
        self.btn_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
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

        self.horizontalLayout_h.addWidget(self.btn_salvar)

        self.btn_irfornecedor = QPushButton(self.produto)
        self.btn_irfornecedor.setObjectName(u"btn_irfornecedor")
        sizePolicy1.setHeightForWidth(self.btn_irfornecedor.sizePolicy().hasHeightForWidth())
        self.btn_irfornecedor.setSizePolicy(sizePolicy1)
        self.btn_irfornecedor.setMinimumSize(QSize(150, 40))
        self.btn_irfornecedor.setMaximumSize(QSize(150, 40))
        self.btn_irfornecedor.setFont(font1)
        self.btn_irfornecedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_irfornecedor.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_h.addWidget(self.btn_irfornecedor)


        self.gridLayout_2.addLayout(self.horizontalLayout_h, 5, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.produto)
        self.fornecedor = QWidget()
        self.fornecedor.setObjectName(u"fornecedor")
        self.verticalLayout_34 = QVBoxLayout(self.fornecedor)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_i = QVBoxLayout()
        self.verticalLayout_i.setObjectName(u"verticalLayout_i")
        self.label_15 = QLabel(self.fornecedor)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_i.addWidget(self.label_15)

        self.entry_nfornecedor = QLineEdit(self.fornecedor)
        self.entry_nfornecedor.setObjectName(u"entry_nfornecedor")
        self.entry_nfornecedor.setMinimumSize(QSize(0, 30))
        self.entry_nfornecedor.setMaximumSize(QSize(16777215, 30))
        self.entry_nfornecedor.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_nfornecedor.setInputMethodHints(Qt.ImhDigitsOnly)
        self.entry_nfornecedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_i.addWidget(self.entry_nfornecedor)


        self.verticalLayout_34.addLayout(self.verticalLayout_i)

        self.verticalLayout_j = QVBoxLayout()
        self.verticalLayout_j.setObjectName(u"verticalLayout_j")
        self.label_7 = QLabel(self.fornecedor)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_j.addWidget(self.label_7)

        self.entry_tfornecedor = QLineEdit(self.fornecedor)
        self.entry_tfornecedor.setObjectName(u"entry_tfornecedor")
        self.entry_tfornecedor.setMinimumSize(QSize(0, 30))
        self.entry_tfornecedor.setMaximumSize(QSize(16777215, 30))
        self.entry_tfornecedor.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_tfornecedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_j.addWidget(self.entry_tfornecedor)


        self.verticalLayout_34.addLayout(self.verticalLayout_j)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.btn_salvar_2 = QPushButton(self.fornecedor)
        self.btn_salvar_2.setObjectName(u"btn_salvar_2")
        sizePolicy1.setHeightForWidth(self.btn_salvar_2.sizePolicy().hasHeightForWidth())
        self.btn_salvar_2.setSizePolicy(sizePolicy1)
        self.btn_salvar_2.setMinimumSize(QSize(150, 40))
        self.btn_salvar_2.setMaximumSize(QSize(150, 40))
        self.btn_salvar_2.setFont(font3)
        self.btn_salvar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_2.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
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

        self.horizontalLayout_10.addWidget(self.btn_salvar_2)

        self.btn_irproduto = QPushButton(self.fornecedor)
        self.btn_irproduto.setObjectName(u"btn_irproduto")
        sizePolicy1.setHeightForWidth(self.btn_irproduto.sizePolicy().hasHeightForWidth())
        self.btn_irproduto.setSizePolicy(sizePolicy1)
        self.btn_irproduto.setMinimumSize(QSize(150, 40))
        self.btn_irproduto.setMaximumSize(QSize(150, 40))
        self.btn_irproduto.setFont(font1)
        self.btn_irproduto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_irproduto.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_10.addWidget(self.btn_irproduto)


        self.verticalLayout_34.addLayout(self.horizontalLayout_10)

        self.stackedWidget_2.addWidget(self.fornecedor)

        self.verticalLayout_21.addWidget(self.stackedWidget_2)


        self.verticalLayout_16.addLayout(self.verticalLayout_21)

        self.stackedWidget.addWidget(self.cadastrarprodutos)
        self.estoque = QWidget()
        self.estoque.setObjectName(u"estoque")
        self.verticalLayout_3 = QVBoxLayout(self.estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.estoque)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.entry_pesquisar_2 = QLineEdit(self.estoque)
        self.entry_pesquisar_2.setObjectName(u"entry_pesquisar_2")
        self.entry_pesquisar_2.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.entry_pesquisar_2)

        self.btn_pesquisar_2 = QPushButton(self.estoque)
        self.btn_pesquisar_2.setObjectName(u"btn_pesquisar_2")
        self.btn_pesquisar_2.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_2.setMaximumSize(QSize(100, 30))
        self.btn_pesquisar_2.setFont(font1)
        self.btn_pesquisar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_2.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_11.addWidget(self.btn_pesquisar_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.frame_5 = QFrame(self.estoque)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stackedWidget_3 = QStackedWidget(self.frame_5)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.estoque_2 = QWidget()
        self.estoque_2.setObjectName(u"estoque_2")
        self.verticalLayout_33 = QVBoxLayout(self.estoque_2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.tb_estoque = QTableWidget(self.estoque_2)
        if (self.tb_estoque.columnCount() < 11):
            self.tb_estoque.setColumnCount(11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        self.tb_estoque.setObjectName(u"tb_estoque")
        self.tb_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"border-radius: 0px;")
        self.tb_estoque.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_estoque.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_estoque.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_estoque.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_33.addWidget(self.tb_estoque)

        self.frame_7 = QFrame(self.estoque_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: none;\n"
"border-radius: 0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_excluir = QPushButton(self.frame_7)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(80, 30))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(220, 0, 0);\n"
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

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_editar = QPushButton(self.frame_7)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setMinimumSize(QSize(80, 30))
        self.btn_editar.setFont(font)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_editar)


        self.verticalLayout_33.addWidget(self.frame_7)

        self.stackedWidget_3.addWidget(self.estoque_2)
        self.editar = QWidget()
        self.editar.setObjectName(u"editar")
        self.gridLayout_3 = QGridLayout(self.editar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.editar)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_19)

        self.entry_dimensoes_3 = QLineEdit(self.editar)
        self.entry_dimensoes_3.setObjectName(u"entry_dimensoes_3")
        self.entry_dimensoes_3.setMinimumSize(QSize(0, 30))
        self.entry_dimensoes_3.setMaximumSize(QSize(16777215, 30))
        self.entry_dimensoes_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_dimensoes_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.entry_dimensoes_3)


        self.gridLayout_3.addLayout(self.verticalLayout_19, 3, 2, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_23 = QLabel(self.editar)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 30))
        self.label_23.setMaximumSize(QSize(16777215, 30))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.label_23)

        self.entry_custo_2 = QLineEdit(self.editar)
        self.entry_custo_2.setObjectName(u"entry_custo_2")
        self.entry_custo_2.setMinimumSize(QSize(0, 30))
        self.entry_custo_2.setMaximumSize(QSize(16777215, 30))
        self.entry_custo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_custo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.entry_custo_2)


        self.gridLayout_3.addLayout(self.verticalLayout_23, 3, 1, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_22 = QLabel(self.editar)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_31.addWidget(self.label_22)

        self.entry_codigo_2 = QLineEdit(self.editar)
        self.entry_codigo_2.setObjectName(u"entry_codigo_2")
        self.entry_codigo_2.setMinimumSize(QSize(0, 30))
        self.entry_codigo_2.setMaximumSize(QSize(16777215, 30))
        self.entry_codigo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_codigo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.entry_codigo_2)


        self.gridLayout_3.addLayout(self.verticalLayout_31, 3, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_21 = QLabel(self.editar)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 30))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_21)

        self.entry_peso_2 = QLineEdit(self.editar)
        self.entry_peso_2.setObjectName(u"entry_peso_2")
        self.entry_peso_2.setMinimumSize(QSize(0, 30))
        self.entry_peso_2.setMaximumSize(QSize(16777215, 30))
        self.entry_peso_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_peso_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.entry_peso_2)


        self.gridLayout_3.addLayout(self.verticalLayout_22, 2, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_25 = QLabel(self.editar)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 30))
        self.label_25.setMaximumSize(QSize(16777215, 30))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_25)

        self.entry_venda_2 = QLineEdit(self.editar)
        self.entry_venda_2.setObjectName(u"entry_venda_2")
        self.entry_venda_2.setMinimumSize(QSize(0, 30))
        self.entry_venda_2.setMaximumSize(QSize(16777215, 30))
        self.entry_venda_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_venda_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.entry_venda_2)


        self.gridLayout_3.addLayout(self.verticalLayout_24, 2, 1, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.editar)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.label_20)

        self.entry_quantidade_3 = QLineEdit(self.editar)
        self.entry_quantidade_3.setObjectName(u"entry_quantidade_3")
        self.entry_quantidade_3.setMinimumSize(QSize(0, 30))
        self.entry_quantidade_3.setMaximumSize(QSize(16777215, 30))
        self.entry_quantidade_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_quantidade_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.entry_quantidade_3)


        self.gridLayout_3.addLayout(self.verticalLayout_20, 2, 2, 1, 1)

        self.btn_editar_2 = QPushButton(self.editar)
        self.btn_editar_2.setObjectName(u"btn_editar_2")
        self.btn_editar_2.setMinimumSize(QSize(80, 40))
        self.btn_editar_2.setFont(font)
        self.btn_editar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_2.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
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

        self.gridLayout_3.addWidget(self.btn_editar_2, 4, 2, 1, 1)

        self.btn_voltar_estoque = QPushButton(self.editar)
        self.btn_voltar_estoque.setObjectName(u"btn_voltar_estoque")
        self.btn_voltar_estoque.setMinimumSize(QSize(80, 40))
        self.btn_voltar_estoque.setMaximumSize(QSize(16777215, 16777215))
        self.btn_voltar_estoque.setFont(font1)
        self.btn_voltar_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_estoque.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_voltar_estoque, 4, 0, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_24 = QLabel(self.editar)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 30))
        self.label_24.setMaximumSize(QSize(16777215, 30))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_32.addWidget(self.label_24)

        self.entry_dimensoes_4 = QLineEdit(self.editar)
        self.entry_dimensoes_4.setObjectName(u"entry_dimensoes_4")
        self.entry_dimensoes_4.setMinimumSize(QSize(0, 30))
        self.entry_dimensoes_4.setMaximumSize(QSize(16777215, 30))
        self.entry_dimensoes_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_dimensoes_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.entry_dimensoes_4)


        self.gridLayout_3.addLayout(self.verticalLayout_32, 1, 0, 1, 3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.editar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.entry_nome_2 = QLineEdit(self.editar)
        self.entry_nome_2.setObjectName(u"entry_nome_2")
        self.entry_nome_2.setMinimumSize(QSize(0, 30))
        self.entry_nome_2.setMaximumSize(QSize(16777215, 30))
        self.entry_nome_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_nome_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.entry_nome_2)


        self.gridLayout_3.addLayout(self.verticalLayout_11, 0, 0, 1, 3)

        self.stackedWidget_3.addWidget(self.editar)

        self.verticalLayout_17.addWidget(self.stackedWidget_3)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.estoque)
        self.entradaesaida = QWidget()
        self.entradaesaida.setObjectName(u"entradaesaida")
        self.verticalLayout_27 = QVBoxLayout(self.entradaesaida)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_8 = QFrame(self.entradaesaida)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_12)


        self.verticalLayout_27.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.entradaesaida)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.stackedWidget_4 = QStackedWidget(self.frame_10)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_27)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_saida = QPushButton(self.page)
        self.btn_saida.setObjectName(u"btn_saida")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.btn_saida.sizePolicy().hasHeightForWidth())
        self.btn_saida.setSizePolicy(sizePolicy2)
        self.btn_saida.setMinimumSize(QSize(100, 30))
        self.btn_saida.setMaximumSize(QSize(100, 30))
        self.btn_saida.setFont(font)
        self.btn_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saida.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_17.addWidget(self.btn_saida)

        self.entry_pesquisar_5 = QLineEdit(self.page)
        self.entry_pesquisar_5.setObjectName(u"entry_pesquisar_5")
        self.entry_pesquisar_5.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_pesquisar_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.entry_pesquisar_5)

        self.btn_pesquisar_6 = QPushButton(self.page)
        self.btn_pesquisar_6.setObjectName(u"btn_pesquisar_6")
        self.btn_pesquisar_6.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_6.setMaximumSize(QSize(100, 30))
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

        self.horizontalLayout_17.addWidget(self.btn_pesquisar_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.tb_entrada = QTableWidget(self.page)
        if (self.tb_entrada.columnCount() < 11):
            self.tb_entrada.setColumnCount(11)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(9, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tb_entrada.setHorizontalHeaderItem(10, __qtablewidgetitem33)
        self.tb_entrada.setObjectName(u"tb_entrada")
        self.tb_entrada.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_entrada.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_entrada.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_entrada.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.tb_entrada)

        self.stackedWidget_4.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_37 = QVBoxLayout(self.page_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_12 = QFrame(self.page_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_28)


        self.verticalLayout_37.addWidget(self.frame_12)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_entrada = QPushButton(self.page_2)
        self.btn_entrada.setObjectName(u"btn_entrada")
        sizePolicy2.setHeightForWidth(self.btn_entrada.sizePolicy().hasHeightForWidth())
        self.btn_entrada.setSizePolicy(sizePolicy2)
        self.btn_entrada.setMinimumSize(QSize(100, 30))
        self.btn_entrada.setMaximumSize(QSize(100, 30))
        self.btn_entrada.setFont(font)
        self.btn_entrada.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrada.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_12.addWidget(self.btn_entrada)

        self.entry_pesquisar_3 = QLineEdit(self.page_2)
        self.entry_pesquisar_3.setObjectName(u"entry_pesquisar_3")
        self.entry_pesquisar_3.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_pesquisar_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.entry_pesquisar_3)

        self.btn_pesquisar_3 = QPushButton(self.page_2)
        self.btn_pesquisar_3.setObjectName(u"btn_pesquisar_3")
        self.btn_pesquisar_3.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_3.setMaximumSize(QSize(100, 30))
        self.btn_pesquisar_3.setFont(font1)
        self.btn_pesquisar_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_3.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_12.addWidget(self.btn_pesquisar_3)


        self.verticalLayout_37.addLayout(self.horizontalLayout_12)

        self.tb_saida = QTableWidget(self.page_2)
        if (self.tb_saida.columnCount() < 6):
            self.tb_saida.setColumnCount(6)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tb_saida.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        self.tb_saida.setObjectName(u"tb_saida")
        self.tb_saida.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_saida.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_saida.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_saida.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_saida.horizontalHeader().setDefaultSectionSize(140)

        self.verticalLayout_37.addWidget(self.tb_saida)

        self.btn_detalharvenda_2 = QPushButton(self.page_2)
        self.btn_detalharvenda_2.setObjectName(u"btn_detalharvenda_2")
        self.btn_detalharvenda_2.setMinimumSize(QSize(80, 30))
        self.btn_detalharvenda_2.setFont(font)
        self.btn_detalharvenda_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detalharvenda_2.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_37.addWidget(self.btn_detalharvenda_2)

        self.stackedWidget_4.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_38 = QVBoxLayout(self.page_3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setMaximumSize(QSize(16777215, 50))
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
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_29)


        self.verticalLayout_38.addWidget(self.frame_13)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.entry_pesquisar_4 = QLineEdit(self.page_3)
        self.entry_pesquisar_4.setObjectName(u"entry_pesquisar_4")
        self.entry_pesquisar_4.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.entry_pesquisar_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.entry_pesquisar_4)

        self.btn_pesquisar_4 = QPushButton(self.page_3)
        self.btn_pesquisar_4.setObjectName(u"btn_pesquisar_4")
        self.btn_pesquisar_4.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_4.setMaximumSize(QSize(100, 30))
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


        self.verticalLayout_38.addLayout(self.horizontalLayout_13)

        self.tb_vendadetalhada = QTableWidget(self.page_3)
        if (self.tb_vendadetalhada.columnCount() < 6):
            self.tb_vendadetalhada.setColumnCount(6)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tb_vendadetalhada.setHorizontalHeaderItem(5, __qtablewidgetitem45)
        self.tb_vendadetalhada.setObjectName(u"tb_vendadetalhada")
        self.tb_vendadetalhada.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_vendadetalhada.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_vendadetalhada.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_vendadetalhada.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_38.addWidget(self.tb_vendadetalhada)

        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 40))
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"border-style: none;\n"
"border-radius: 00px;")

        self.verticalLayout_43.addWidget(self.label_32, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lb_fpagamento_2 = QLabel(self.frame_15)
        self.lb_fpagamento_2.setObjectName(u"lb_fpagamento_2")
        self.lb_fpagamento_2.setMinimumSize(QSize(110, 0))
        self.lb_fpagamento_2.setMaximumSize(QSize(110, 16777215))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.lb_fpagamento_2.setFont(font5)
        self.lb_fpagamento_2.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")
        self.lb_fpagamento_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.lb_fpagamento_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_18.addLayout(self.verticalLayout_43)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)

        self.label_38 = QLabel(self.frame_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(60, 0))
        self.label_38.setMaximumSize(QSize(60, 16777215))
        self.label_38.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_18.addWidget(self.label_38)

        self.lb_valordescontovd = QLabel(self.frame_15)
        self.lb_valordescontovd.setObjectName(u"lb_valordescontovd")
        self.lb_valordescontovd.setMinimumSize(QSize(50, 30))
        self.lb_valordescontovd.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_18.addWidget(self.lb_valordescontovd)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_15)

        self.label_40 = QLabel(self.frame_15)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(100, 0))
        self.label_40.setMaximumSize(QSize(60, 16777215))
        self.label_40.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_18.addWidget(self.label_40)

        self.lb_valorprodutos_vd = QLabel(self.frame_15)
        self.lb_valorprodutos_vd.setObjectName(u"lb_valorprodutos_vd")
        self.lb_valorprodutos_vd.setMinimumSize(QSize(50, 30))
        self.lb_valorprodutos_vd.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_18.addWidget(self.lb_valorprodutos_vd)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)

        self.label_41 = QLabel(self.frame_15)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(60, 0))
        self.label_41.setMaximumSize(QSize(60, 16777215))
        self.label_41.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_18.addWidget(self.label_41)

        self.lb_valortotal_vd = QLabel(self.frame_15)
        self.lb_valortotal_vd.setObjectName(u"lb_valortotal_vd")
        self.lb_valortotal_vd.setMinimumSize(QSize(70, 30))
        self.lb_valortotal_vd.setMaximumSize(QSize(0, 30))

        self.horizontalLayout_18.addWidget(self.lb_valortotal_vd)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)


        self.verticalLayout_38.addWidget(self.frame_15)

        self.btn_pesquisar_5 = QPushButton(self.page_3)
        self.btn_pesquisar_5.setObjectName(u"btn_pesquisar_5")
        self.btn_pesquisar_5.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_5.setMaximumSize(QSize(100, 30))
        self.btn_pesquisar_5.setFont(font1)
        self.btn_pesquisar_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_5.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_38.addWidget(self.btn_pesquisar_5)

        self.stackedWidget_4.addWidget(self.page_3)

        self.verticalLayout_36.addWidget(self.stackedWidget_4)


        self.verticalLayout_27.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.entradaesaida)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_42 = QVBoxLayout(self.page_4)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_30 = QLabel(self.page_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 40))
        self.label_30.setFont(font3)
        self.label_30.setLayoutDirection(Qt.LeftToRight)
        self.label_30.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_30)

        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(700, 200))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tb_confirmarvenda = QTableWidget(self.frame_3)
        if (self.tb_confirmarvenda.columnCount() < 6):
            self.tb_confirmarvenda.setColumnCount(6)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tb_confirmarvenda.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        self.tb_confirmarvenda.setObjectName(u"tb_confirmarvenda")
        self.tb_confirmarvenda.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_confirmarvenda.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_confirmarvenda.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_15.addWidget(self.tb_confirmarvenda)


        self.verticalLayout_42.addWidget(self.frame_3)

        self.frame_14 = QFrame(self.page_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border-style: none;\n"
"border-radius: 00px;")

        self.verticalLayout_41.addWidget(self.label_31, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lb_fpagamento = QLabel(self.frame_14)
        self.lb_fpagamento.setObjectName(u"lb_fpagamento")
        self.lb_fpagamento.setMinimumSize(QSize(110, 0))
        self.lb_fpagamento.setMaximumSize(QSize(110, 16777215))
        self.lb_fpagamento.setFont(font5)
        self.lb_fpagamento.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")
        self.lb_fpagamento.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.lb_fpagamento, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_8.addLayout(self.verticalLayout_41)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_35 = QLabel(self.frame_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(60, 0))
        self.label_35.setMaximumSize(QSize(60, 16777215))
        self.label_35.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.label_35)

        self.lb_valorprodutos_2 = QLabel(self.frame_14)
        self.lb_valorprodutos_2.setObjectName(u"lb_valorprodutos_2")
        self.lb_valorprodutos_2.setMinimumSize(QSize(50, 30))
        self.lb_valorprodutos_2.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_8.addWidget(self.lb_valorprodutos_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_36 = QLabel(self.frame_14)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 0))
        self.label_36.setMaximumSize(QSize(60, 16777215))
        self.label_36.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.label_36)

        self.lb_valorprodutos = QLabel(self.frame_14)
        self.lb_valorprodutos.setObjectName(u"lb_valorprodutos")
        self.lb_valorprodutos.setMinimumSize(QSize(50, 30))
        self.lb_valorprodutos.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_8.addWidget(self.lb_valorprodutos)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_37 = QLabel(self.frame_14)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(60, 0))
        self.label_37.setMaximumSize(QSize(60, 16777215))
        self.label_37.setStyleSheet(u"border-style: none;\n"
"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.label_37)

        self.lb_valortotal = QLabel(self.frame_14)
        self.lb_valortotal.setObjectName(u"lb_valortotal")
        self.lb_valortotal.setMinimumSize(QSize(70, 30))
        self.lb_valortotal.setMaximumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.lb_valortotal)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_42.addWidget(self.frame_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_cancelar = QPushButton(self.page_4)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(110, 30))
        self.btn_cancelar.setMaximumSize(QSize(110, 30))
        self.btn_cancelar.setFont(font1)
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(220, 0, 0);\n"
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

        self.horizontalLayout_16.addWidget(self.btn_cancelar)

        self.btn_finalizarvenda_3 = QPushButton(self.page_4)
        self.btn_finalizarvenda_3.setObjectName(u"btn_finalizarvenda_3")
        self.btn_finalizarvenda_3.setMinimumSize(QSize(110, 30))
        self.btn_finalizarvenda_3.setMaximumSize(QSize(110, 30))
        self.btn_finalizarvenda_3.setFont(font1)
        self.btn_finalizarvenda_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizarvenda_3.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
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

        self.horizontalLayout_16.addWidget(self.btn_finalizarvenda_3)


        self.verticalLayout_42.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.cb_pagamento.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_realizarvenda.setText(QCoreApplication.translate("MainWindow", u"Realizar venda", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar produtos", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_entradaesaida.setText(QCoreApplication.translate("MainWindow", u"Entradas e sa\u00eddas", None))
        self.entry_pesquisar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tb_pesquisa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_pesquisa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem2 = self.tb_pesquisa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem3 = self.tb_pesquisa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem4 = self.tb_pesquisa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Valor venda", None));
        ___qtablewidgetitem5 = self.tb_pesquisa.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.entry_quantidade_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.entry_quantidade_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.btn_inserirnocarrinho.setText(QCoreApplication.translate("MainWindow", u"Inserir no carrinho", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Carrinho", None))
        ___qtablewidgetitem6 = self.tb_carrinho.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tb_carrinho.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem8 = self.tb_carrinho.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem9 = self.tb_carrinho.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem10 = self.tb_carrinho.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Valor venda", None));
        ___qtablewidgetitem11 = self.tb_carrinho.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.cb_pagamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Forma de pagamento", None))
        self.cb_pagamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Pix", None))
        self.cb_pagamento.setItemText(2, QCoreApplication.translate("MainWindow", u"Dinheiro", None))
        self.cb_pagamento.setItemText(3, QCoreApplication.translate("MainWindow", u"Cart\u00e3o de cr\u00e9dito", None))
        self.cb_pagamento.setItemText(4, QCoreApplication.translate("MainWindow", u"D\u00e9bito", None))

        self.cb_pagamento.setCurrentText(QCoreApplication.translate("MainWindow", u"Forma de pagamento", None))
        self.btn_finalizarvenda.setText(QCoreApplication.translate("MainWindow", u"Finalizar venda", None))
        self.btn_apagaritens.setText(QCoreApplication.translate("MainWindow", u"Apagar itens", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Desconto:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Total de produtos:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Valor total:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo de barra:", None))
        self.entry_codigo.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de venda:", None))
        self.entry_venda.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.entry_peso.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de custo:", None))
        self.entry_custo.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.entry_quantidade.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dimens\u00f5es:", None))
        self.entry_dimensoes.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome do produto:", None))
        self.entry_nome.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do produto:", None))
        self.entry_dimensoes_2.setPlaceholderText("")
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_irfornecedor.setText(QCoreApplication.translate("MainWindow", u"Definir fornecedor", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nome do fornecedor", None))
        self.entry_nfornecedor.setText("")
        self.entry_nfornecedor.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Telefone do fornecedor:", None))
        self.entry_tfornecedor.setText("")
        self.entry_tfornecedor.setPlaceholderText("")
        self.btn_salvar_2.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_irproduto.setText(QCoreApplication.translate("MainWindow", u"Definir produto", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.entry_pesquisar_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar_2.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem12 = self.tb_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem13 = self.tb_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem14 = self.tb_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem15 = self.tb_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem16 = self.tb_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Valor custo", None));
        ___qtablewidgetitem17 = self.tb_estoque.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Valor venda", None));
        ___qtablewidgetitem18 = self.tb_estoque.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Nome fornecedor", None));
        ___qtablewidgetitem19 = self.tb_estoque.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Telefone fornecedor", None));
        ___qtablewidgetitem20 = self.tb_estoque.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Dimens\u00f5es", None));
        ___qtablewidgetitem21 = self.tb_estoque.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem22 = self.tb_estoque.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Dimens\u00f5es:", None))
        self.entry_dimensoes_3.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de custo:", None))
        self.entry_custo_2.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo de barra:", None))
        self.entry_codigo_2.setPlaceholderText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.entry_peso_2.setPlaceholderText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de venda:", None))
        self.entry_venda_2.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.entry_quantidade_3.setPlaceholderText("")
        self.btn_editar_2.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_voltar_estoque.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do produto:", None))
        self.entry_dimensoes_4.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome do produto:", None))
        self.entry_nome_2.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Entradas e sa\u00eddas", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"Saida", None))
        self.entry_pesquisar_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar_6.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem23 = self.tb_entrada.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem24 = self.tb_entrada.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem25 = self.tb_entrada.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem26 = self.tb_entrada.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem27 = self.tb_entrada.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Valor Custo", None));
        ___qtablewidgetitem28 = self.tb_entrada.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Valor Venda", None));
        ___qtablewidgetitem29 = self.tb_entrada.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nome do Fornecedor", None));
        ___qtablewidgetitem30 = self.tb_entrada.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"N\u00famero do Fornecedor", None));
        ___qtablewidgetitem31 = self.tb_entrada.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Dimens\u00f5es", None));
        ___qtablewidgetitem32 = self.tb_entrada.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem33 = self.tb_entrada.horizontalHeaderItem(10)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.btn_entrada.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.entry_pesquisar_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar_3.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem34 = self.tb_saida.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem35 = self.tb_saida.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Quantidade de produtos", None));
        ___qtablewidgetitem36 = self.tb_saida.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Valor total", None));
        ___qtablewidgetitem37 = self.tb_saida.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem38 = self.tb_saida.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Forma de pagamento", None));
        ___qtablewidgetitem39 = self.tb_saida.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        self.btn_detalharvenda_2.setText(QCoreApplication.translate("MainWindow", u"Detalhar venda", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Venda detalhada", None))
        self.entry_pesquisar_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar_4.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem40 = self.tb_vendadetalhada.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem41 = self.tb_vendadetalhada.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem42 = self.tb_vendadetalhada.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem43 = self.tb_vendadetalhada.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem44 = self.tb_vendadetalhada.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Valor venda", None));
        ___qtablewidgetitem45 = self.tb_vendadetalhada.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Forma de pagamento:", None))
        self.lb_fpagamento_2.setText(QCoreApplication.translate("MainWindow", u"Cart\u00e3o de cr\u00e9dito", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Desconto:", None))
        self.lb_valordescontovd.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Total de produtos:", None))
        self.lb_valorprodutos_vd.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Valor total:", None))
        self.lb_valortotal_vd.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.btn_pesquisar_5.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Confirmar venda", None))
        ___qtablewidgetitem46 = self.tb_confirmarvenda.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem47 = self.tb_confirmarvenda.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem48 = self.tb_confirmarvenda.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem49 = self.tb_confirmarvenda.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem50 = self.tb_confirmarvenda.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem51 = self.tb_confirmarvenda.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Valor venda", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Forma de pagamento:", None))
        self.lb_fpagamento.setText(QCoreApplication.translate("MainWindow", u"Cart\u00e3o de cr\u00e9dito", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Desconto:", None))
        self.lb_valorprodutos_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Total de produtos:", None))
        self.lb_valorprodutos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Valor total:", None))
        self.lb_valortotal.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_finalizarvenda_3.setText(QCoreApplication.translate("MainWindow", u"Finalizar venda", None))
    # retranslateUi

