from PySide import QtCore
from PySide import QtGui

mydata = ["haha", "hihi"]

class SearchResultsModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(SearchResultsModel, self).__init__(parent)

    def data(self, index, role):     
        if not index.isValid():
            return None

        obj = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            return mydata[index.row()]

        return None

    def rowCount(self, parent):
        return len(mydata)