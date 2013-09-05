from PySide import QtCore
from PySide import QtGui
from mainwindow_ui import Ui_MainWindow
from resultsmodel import *
from resultsdelegate import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
       
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
                
        self.setupUi(self)

        self.setWindowTitle("Search My Workspace")

        # Completer used to set my workspace
        completer = QtGui.QCompleter(self)
        fsmodel = QtGui.QFileSystemModel(self)
        fsmodel.setRootPath("")
        completer.setModel(fsmodel)
        self.lineEdit_workspace.setCompleter(completer)

        # List to display search results
        self.searchResultsModel = SearchResultsModel()
        self.listView_result.setModel(self.searchResultsModel)

        searchResultsDelegate = SearchResultsDelegate(self.listView_result)
        self.listView_result.setItemDelegate(searchResultsDelegate);

        # signal slots
        self.createConnections()                

    ''' connect signal/slot pairs '''
    def createConnections(self):
    	self.pushButton_search.clicked.connect(self.search)
    	self.pushButton_browser.clicked.connect(self.selectWorkspace)

    def search(self):
    	QtGui.QMessageBox.information(self, "info", "haha")

    def selectWorkspace(self):
    	wsPath = QtGui.QFileDialog.getExistingDirectory(self, "Select your workspace", "D:\\EasyTest", QtGui.QFileDialog.ShowDirsOnly)
    	QtGui.QMessageBox.information(self, "info", wsPath)
    	self.lineEdit_workspace.setText(wsPath)