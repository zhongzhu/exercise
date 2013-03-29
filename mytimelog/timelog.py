import sys
from PySide import QtCore
from PySide import QtGui
import mainwindow
#from treemodel import TreeModel

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    
#    model = TreeModel()
#    model.load("haha.tlg")
#    view = QtGui.QTreeView()
#    view.setModel(model)
#    view.setWindowTitle("Simple Tree Model")
#    view.show()
    app.setApplicationName("Timelog")
    mainwindow = mainwindow.MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())