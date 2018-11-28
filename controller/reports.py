# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.table_model import MyTableModel
from view.reports import Ui_Form as reports
from model.model import Model
import json
import datetime
from view.branches_dw import Ui_Form as branches
import xml.etree.ElementTree as ET


class Branches(QWidget,branches):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

class Reports(QWidget,reports):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.db = Model()
        self.branch = Branches()
        self.stackedWidget_3.setCurrentIndex(0)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground)
        self.fill_combobox()
        self.all_report.clicked.connect(self.open_all_report)
        self.detailed_report.clicked.connect(self.open_detailed_page)
        self.w1.setContentsMargins(20, 20, 20, 20)
        self.w2.setContentsMargins(20, 20, 20, 20)
        self.widget_7.setContentsMargins(9,9,9,9)
        self.setWindowTitle(u'تقارير')
        for i in self.findChildren(QDateTimeEdit):
            i.setDateTime(datetime.datetime.now())
        self.pushButton.clicked.connect(self.branches_pre)
        self.branch.tableWidget.clicked.connect(self.del_itm)
        self.branch_le_3.currentIndexChanged.connect(self.set_server)

        self.search_btn.clicked.connect(self.show_report_in_table_view)
        self.search_btn_tm.clicked.connect(self.show_report_detailed_in_table_view)
    def set_server(self):
        x = self.branch_le_3.currentText()
        self.db.set_server(x)
    def del_itm(self,index):
        try:
            if index.column() == 2:
                    if self.dialoge_only(u'هل انت متاكد متاكد من الحذف',u'') == QMessageBox.Ok:
                        name = self.branch.tableWidget.item(index.row(), 0).text()
                        tree = ET.parse('branches.xml')
                        root = tree.getroot()
                        for profile in root[0].findall(".//item[@name='{}']".format(name)):
                            print profile
                            root[0].remove(profile)

                        # create a new XML file with the results
                        tree.write('branches.xml')
                        self.show_case_info_out()
        except:pass

    def show_case_info_out(self):
        try:
            self.branch.tableWidget.setRowCount(0)
            for i in self.db.get_branches():
                n = self.branch.tableWidget.rowCount()
                self.branch.tableWidget.insertRow(n)
                self.branch.tableWidget.setItem(n,0,QTableWidgetItem(i[0]))
                self.branch.tableWidget.setItem(n, 1, QTableWidgetItem(i[1]))
                self.branch.tableWidget.setItem(n,2,QTableWidgetItem(u'حذف'))
                self.branch.tableWidget.item(n,2).setBackground(QColor(238, 49, 36))
            else:
                n = self.branch.tableWidget.rowCount()
                self.branch.tableWidget.insertRow(n)
                edt = QLineEdit()
                edt_2 = QLineEdit()
                edt_2.setStatusTip(str(n))
                self.branch.tableWidget.setCellWidget(n, 0, edt)
                self.branch.tableWidget.setCellWidget(n, 1, edt_2)
                edt.returnPressed.connect(lambda: edt_2.setFocus())
                edt_2.returnPressed.connect(self.insert_out)
                edt.setFocus()
            self.fill_branches()
        except:
            pass
    def insert_out(self):
        row = int(self.sender().statusTip())
        name = self.branch.tableWidget.cellWidget(row, 0).text()
        details = self.branch.tableWidget.cellWidget(row, 1).text()
        if name and details:
            self.insert_info(name,details)
            self.show_case_info_out()
    def insert_info(self,name,ip):
        tree = ET.parse('branches.xml')
        root = tree.getroot()

        # adding an element to the root node
        attrib = {'name':name,'ip':ip}
        ET.SubElement(root[0], 'item', attrib)
        tree.write('branches.xml')
    def branches_pre(self):
        self.branch.showNormal()
        self.branch.raise_()
        self.branch.activateWindow()
    def fill_branches(self):
        self.branch_le_3.clear()
        self.branch_le_3.addItems([i[0] for i in self.db.get_branches()])
    def fill_combobox(self):
        try:
            services=self.db.get_services()
            terminals=self.db.get_terminals()
            username=self.db.get_username()
            s=json.loads(services)
            t=json.loads(terminals)
            u=json.loads(username)
            self.service_le_3.addItem(u'الكل')
            for i in s:
                self.service_le_3.addItem(i.get("name"))

            self.terminal_le_3.addItem(u'الكل')
            for i in t:
                self.terminal_le_3.addItem(i.get("name"))

            self.user_le_3.addItem(u'الكل')
            for i in u:
                self.user_le_3.addItem(i.get("username"))

            self.fill_branches()
        except:pass

    def open_detailed_page(self):
        self.stackedWidget_3.setCurrentIndex(1)

    def open_all_report(self):
        self.stackedWidget_3.setCurrentIndex(0)

    def show_report_in_table_view(self):
        start=self.st_date_gen.dateTime().toPython()
        end = self.end_date_gen.dateTime().toPython()
        service = self.service_le_3.currentText()
        terminal = self.terminal_le_3.currentText()
        user = self.user_le_3.currentText()
        reports = self.db.get_reports(start,end,service,terminal,user)
        self.tableWidget_gen.setRowCount(0)
        for i in reports:
            n = self.tableWidget_gen.rowCount()
            self.tableWidget_gen.insertRow(n)
            self.tableWidget_gen.setItem(n,0,QTableWidgetItem(unicode(i['num'])))
            self.tableWidget_gen.setItem(n,1,QTableWidgetItem(unicode(i['service_name'])))
            self.tableWidget_gen.setItem(n,2,QTableWidgetItem(unicode(i['terminal_name'])))
            self.tableWidget_gen.setItem(n,3,QTableWidgetItem(unicode(i['user_name'])))
            self.tableWidget_gen.setItem(n,4,QTableWidgetItem(unicode(i['date_join'])))
            self.tableWidget_gen.setItem(n,5,QTableWidgetItem(unicode(i['date_call'])))
            self.tableWidget_gen.setItem(n,6,QTableWidgetItem(unicode(i['date_end'])))
        self.tableWidget_gen.resizeColumnsToContents()

    def show_report_detailed_in_table_view(self):
        start=self.st_date_tm.dateTime().toPython()
        end = self.end_date_tm.dateTime().toPython()
        service = self.radioButton.isChecked()

        reports = self.db.get_reports_detailed(start,end,service)
        self.tableWidget_tm.setRowCount(0)
        avg1 = 0
        avg2 = 0
        for i in reports:
            n = self.tableWidget_tm.rowCount()
            self.tableWidget_tm.insertRow(n)
            self.tableWidget_tm.setItem(n,0,QTableWidgetItem(unicode(i['name'])))
            self.tableWidget_tm.setItem(n,1,QTableWidgetItem(unicode(i['avg1'])))
            self.tableWidget_tm.setItem(n,2,QTableWidgetItem(unicode(i['avg2'])))
            avg1 += i['avg1']
            avg2 += i['avg2']
        self.label.setText(unicode(avg1))
        self.label_3.setText(unicode(avg2))
        self.tableWidget_tm.resizeColumnsToContents()

    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()