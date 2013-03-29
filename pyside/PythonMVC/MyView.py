'''
Created on Feb 8, 2012

@author: zhzhong
'''

from PySide.QtCore import *
from PySide.QtGui import *
from ui_PythonMVC import Ui_Dialog
from MyModel import *
from testcase.TestCase import *

class MyView(QDialog, Ui_Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        super(MyView, self).__init__(parent)
        self.setupUi(self)
        
        # setup model
        tc = TestCase('a.xml')
        tc.load(tc.tcFileName)
        self.model = MyModel(tc)
        self.treeView.setModel(self.model)

        ''' connect signal/slot pairs '''
        #self.aboutButton.clicked.connect(self.about)
        