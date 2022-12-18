# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 696)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:#353b48")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, -20, 1261, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.verticalLayoutWidget_3)
        self.Title.setObjectName(u"Title")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        self.Title.setFont(font1)
        self.Title.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#1e272e")
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Title)

        self.btn_sort = QPushButton(self.centralwidget)
        self.btn_sort.setObjectName(u"btn_sort")
        self.btn_sort.setGeometry(QRect(430, 470, 381, 121))
        font2 = QFont()
        font2.setPointSize(31)
        font2.setBold(True)
        self.btn_sort.setFont(font2)
        self.btn_sort.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sort.setStyleSheet(u"QPushButton {\n"
"  background-color:#00a8ff;\n"
"  border: 3px solid rgb(0, 71, 107);\n"
"  border-radius: 15px;\n"
"  color: #FFFFFF;\n"
"  line-height: normal;\n"
"  margin: 0;\n"
"  min-height: 60px;\n"
"  min-width: 0;\n"
"  outline: none;\n"
"  padding: 16px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  width: 100%;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
" background-color:rgb(0, 114, 171);\n"
"\n"
"}")
        self.btn_sort.setCheckable(False)
        self.btn_sort.setChecked(False)
        self.btn_sort.setAutoDefault(False)
        self.btn_sort.setFlat(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 160, 451, 271))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:#2f3640;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.te_input = QTextEdit(self.frame)
        self.te_input.setObjectName(u"te_input")
        self.te_input.setGeometry(QRect(0, 50, 451, 219))
        font3 = QFont()
        font3.setFamilies([u"Samim"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.te_input.setFont(font3)
        self.te_input.setStyleSheet(u"color:white;\n"
"border:1px solid white;\n"
"background-color:#1e272e;\n"
"padding:5px")
        self.te_input.setTabChangesFocus(True)
        self.lbl_input = QLabel(self.frame)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setGeometry(QRect(10, 0, 431, 41))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.lbl_input.setFont(font4)
        self.lbl_input.setStyleSheet(u"color:white")
        self.lbl_input.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(760, 160, 451, 271))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:#2f3640;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.te_output = QTextEdit(self.frame_2)
        self.te_output.setObjectName(u"te_output")
        self.te_output.setGeometry(QRect(0, 50, 451, 219))
        self.te_output.setFont(font3)
        self.te_output.setStyleSheet(u"color:white;\n"
"border:1px solid white;\n"
"background-color:#1e272e;\n"
"padding:5px")
        self.te_output.setTabChangesFocus(True)
        self.te_output.setReadOnly(True)
        self.lbl_output = QLabel(self.frame_2)
        self.lbl_output.setObjectName(u"lbl_output")
        self.lbl_output.setGeometry(QRect(10, 0, 429, 41))
        self.lbl_output.setFont(font4)
        self.lbl_output.setStyleSheet(u"color:white")
        self.lbl_output.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(500, 160, 251, 271))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color:#1e272e;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.le_sep = QLineEdit(self.frame_3)
        self.le_sep.setObjectName(u"le_sep")
        self.le_sep.setGeometry(QRect(20, 60, 211, 41))
        font5 = QFont()
        font5.setFamilies([u"Samim"])
        font5.setPointSize(19)
        font5.setBold(True)
        self.le_sep.setFont(font5)
        self.le_sep.setStyleSheet(u"color:white;\n"
"border:1px solid #00a8ff;\n"
"padding:5px")
        self.le_sep.setMaxLength(1)
        self.le_sep.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 251, 31))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#2f3640;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.btn_autosort = QCheckBox(self.frame_3)
        self.btn_autosort.setObjectName(u"btn_autosort")
        self.btn_autosort.setGeometry(QRect(60, 120, 151, 41))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.btn_autosort.setFont(font7)
        self.btn_autosort.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_autosort.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#1e272e;")
        self.btn_autosort.setIconSize(QSize(50, 50))
        self.btn_autosort.setChecked(True)
        self.cb_asc = QCheckBox(self.frame_3)
        self.cb_asc.setObjectName(u"cb_asc")
        self.cb_asc.setGeometry(QRect(60, 160, 151, 41))
        self.cb_asc.setFont(font7)
        self.cb_asc.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_asc.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#1e272e;")
        self.cb_asc.setIconSize(QSize(50, 50))
        self.cb_asc.setChecked(True)
        self.rb_merge = QRadioButton(self.frame_3)
        self.rb_merge.setObjectName(u"rb_merge")
        self.rb_merge.setGeometry(QRect(140, 220, 71, 20))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        self.rb_merge.setFont(font8)
        self.rb_merge.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#1e272e;")
        self.rb_merge.setIconSize(QSize(20, 20))
        self.rb_merge.setChecked(False)
        self.rb_insertion = QRadioButton(self.frame_3)
        self.rb_insertion.setObjectName(u"rb_insertion")
        self.rb_insertion.setGeometry(QRect(30, 220, 101, 20))
        self.rb_insertion.setFont(font8)
        self.rb_insertion.setStyleSheet(u"color:#00a8ff;\n"
"background-color:#1e272e;")
        self.rb_insertion.setChecked(True)
        self.label_6.raise_()
        self.le_sep.raise_()
        self.btn_autosort.raise_()
        self.cb_asc.raise_()
        self.rb_merge.raise_()
        self.rb_insertion.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1260, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.te_input, self.le_sep)
        QWidget.setTabOrder(self.le_sep, self.btn_autosort)
        QWidget.setTabOrder(self.btn_autosort, self.btn_sort)
        QWidget.setTabOrder(self.btn_sort, self.te_output)

        self.retranslateUi(MainWindow)

        self.btn_sort.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Insertion Sort", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Sorting", None))
        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"Sort Numbers", None))
        self.te_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your numbers here....", None))
        self.lbl_input.setText(QCoreApplication.translate("MainWindow", u"Input Numbers", None))
        self.te_output.setPlaceholderText("")
        self.lbl_output.setText(QCoreApplication.translate("MainWindow", u"Sorted Numbers", None))
        self.le_sep.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input/Output Seperator", None))
        self.btn_autosort.setText(QCoreApplication.translate("MainWindow", u"Auto sort", None))
        self.cb_asc.setText(QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.rb_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.rb_insertion.setText(QCoreApplication.translate("MainWindow", u"Insertion", None))
    # retranslateUi

