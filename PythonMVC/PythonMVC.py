'''
Created on Feb 8, 2012

@author: zhzhong
'''

import sys    
from PySide.QtGui import QApplication
from PySide.QtCore import *
from MyView import MyView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MyView()
    dlg.show()   
    sys.exit(app.exec_())