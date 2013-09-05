from PySide import QtCore
from PySide import QtGui
from oneresult_ui import Ui_Form

class OneResultWidget(QtGui.QWidget, Ui_Form):
       
    def __init__(self, parent = None):
        super(OneResultWidget, self).__init__(parent)
                
        self.setupUi(self)