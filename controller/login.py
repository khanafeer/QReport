# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from view.login_page import Ui_Form as login_page
from model.model import Model
from .reports import Reports
import json

class Login_Page(QWidget,login_page):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.db = Model()
        self.report=Reports()
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground)
        self.login_btn.clicked.connect(self.check_auth)
        self.exit_btn.clicked.connect(exit)
        self.inform_lbl.hide()
        self.setWindowTitle(u'تسجيل الدخول')
        self.pass_lbl.returnPressed.connect(self.check_auth)
        self.report.show_case_info_out()


    def check_auth(self):
        username=self.user_lbl.text()
        password=self.pass_lbl.text()
        auth=self.db.login(username,password)

        if auth:
            self.report.show()
            self.close()


