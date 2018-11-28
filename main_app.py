# -*- coding: utf-8 -*-
from PySide.QtGui import *
from controller.login import Login_Page
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    h = Login_Page()
    h.show()
    app.exec_()