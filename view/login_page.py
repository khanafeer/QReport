# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/login_page.ui'
#
# Created: Sat Nov 10 15:28:30 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.login_w = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_w.sizePolicy().hasHeightForWidth())
        self.login_w.setSizePolicy(sizePolicy)
        self.login_w.setMinimumSize(QtCore.QSize(320, 200))
        self.login_w.setStyleSheet(".QWidget\n"
"{\n"
"background:rgba(0, 0, 0,150);\n"
"}\n"
"QLineEdit\n"
"{\n"
"color:#000;\n"
"border: 1px solid #032632;\n"
"}\n"
".QLabel\n"
"{\n"
"color:#fff;\n"
"}\n"
".QPushButton\n"
"{\n"
"background:#000;\n"
"border-radius:8px;\n"
"border: 0px solid;\n"
"color:#fff;\n"
"}\n"
"")
        self.login_w.setObjectName("login_w")
        self.gridLayout = QtGui.QGridLayout(self.login_w)
        self.gridLayout.setContentsMargins(25, 25, 25, 25)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.exit_btn = QtGui.QPushButton(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtCore.Qt.PointingHandCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/imgs/018-power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(30, 30))
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 4, 0, 1, 1)
        self.inform_lbl = QtGui.QLabel(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inform_lbl.sizePolicy().hasHeightForWidth())
        self.inform_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inform_lbl.setFont(font)
        self.inform_lbl.setStyleSheet("QLabel\n"
"{\n"
"background:#bd1e1e;\n"
"color:#fff;\n"
"}")
        self.inform_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.inform_lbl.setMargin(5)
        self.inform_lbl.setObjectName("inform_lbl")
        self.gridLayout.addWidget(self.inform_lbl, 1, 0, 1, 2)
        self.pass_lbl = QtGui.QLineEdit(self.login_w)
        self.pass_lbl.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_lbl.sizePolicy().hasHeightForWidth())
        self.pass_lbl.setSizePolicy(sizePolicy)
        self.pass_lbl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_lbl.setObjectName("pass_lbl")
        self.gridLayout.addWidget(self.pass_lbl, 3, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.user_lbl = QtGui.QLineEdit(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_lbl.sizePolicy().hasHeightForWidth())
        self.user_lbl.setSizePolicy(sizePolicy)
        self.user_lbl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.user_lbl.setFont(font)
        self.user_lbl.setStyleSheet("")
        self.user_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.user_lbl.setObjectName("user_lbl")
        self.gridLayout.addWidget(self.user_lbl, 2, 0, 1, 2)
        self.login_btn = QtGui.QPushButton(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtCore.Qt.PointingHandCursor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/imgs/maps-and-flags (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QtCore.QSize(30, 30))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.login_w, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_lbl, self.pass_lbl)
        Form.setTabOrder(self.pass_lbl, self.login_btn)
        Form.setTabOrder(self.login_btn, self.exit_btn)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_btn.setText(QtGui.QApplication.translate("Form", "اغلاق", None, QtGui.QApplication.UnicodeUTF8))
        self.inform_lbl.setText(QtGui.QApplication.translate("Form", "تحذيرات", None, QtGui.QApplication.UnicodeUTF8))
        self.pass_lbl.setPlaceholderText(QtGui.QApplication.translate("Form", "كلمة السر", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">تسجيل الدخول</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.user_lbl.setPlaceholderText(QtGui.QApplication.translate("Form", "اسم المستخدم", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("Form", "دخول", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
