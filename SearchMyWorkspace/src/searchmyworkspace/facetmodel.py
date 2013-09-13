from PySide import QtCore
from PySide import QtGui
from roles import ResultRoles

class FacetModel(QtGui.QIdentityProxyModel):
    def __init__(self, parent=None):
        super(FacetModel, self).__init__(parent)
        