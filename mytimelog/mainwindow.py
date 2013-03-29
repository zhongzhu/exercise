from PySide import QtCore
from PySide import QtGui
from mytimelog_ui import Ui_MainWindow
from treemodel import TreeModel

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
       
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
                
        self.setupUi(self)
        # setup treeView for drag and drop
        self.model = QtGui.QSortFilterProxyModel()
        self.model.setSourceModel(TreeModel())                  
        self.treeView.setModel(self.model)
        self.treeView.dragEnabled()
        self.treeView.acceptDrops()
        self.treeView.showDropIndicator()
        self.treeView.setDragDropMode(QtGui.QAbstractItemView.InternalMove) 
        self.treeView.expandAll()        
#        self.treeView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
#        self.treeView.setDropIndicatorShown(True)
        
        self.setCentralWidget(self.treeView)

        self.createConnections()
        
        self.load("haha.tlg")

    ''' connect signal/slot pairs '''
    def createConnections(self):
        self.fileNewAction.triggered.connect(self.fileNew)
        self.fileOpenAction.triggered.connect(self.fileOpen)
        self.fileSaveAction.triggered.connect(self.fileSave)
        self.editAddAction.triggered.connect(self.editAdd)
        self.editCutAction.triggered.connect(self.editCut)
        self.editPasteAction.triggered.connect(self.editPaste)
        self.editDeleteAction.triggered.connect(self.editDelete)
        
    def fileNew(self):
        QtGui.QMessageBox.about(self, "haha", "Hello World!")
        
    def fileOpen(self):
        dir = "."
        if self.model.fileName:
            dir = QtCore.QFileInfo(self.model.fileName).canonicalPath()
 
        (filename, selectedFilter) = QtGui.QFileDialog.getOpenFileName(self, "Timelog - Open", dir, "Timelogs (*.tlg)");
        if (filename):
            self.load(filename)
            
    def fileSave(self):
        saved = False
        
        if self.model.fileName == None:
            saved = self.fileSaveAs()
        else:
            self.model.save()
            self.setDirty(False)
            self.setWindowTitle('{} - {}[*]'.format(QtGui.QApplication.applicationName(), QtCore.QFileInfo(self.model.fileName).fileName()))
#            self.statusBar().showMessage(tr("Saved %1")
#                        .arg(model->filename()), StatusTimeout);
            saved = True
                
#        updateUi();
        return saved
                
    def fileSaveAs(self):
        filename = self.model.fileName
        dir = "."
        if filename:
            dir = QtCore.QFileInfo(filename).path()
            
        filename = QtGui.QFileDialog.getSaveFileName(self,
                 '{} - Save As'.format(QtGui.QApplication.applicationName()),
                dir,
                '{} (*.tlg)'.format(QtGui.QApplication.applicationName()))
        
        if not filename:
            return False
        
        if not '.tlg' in filename.lower():        
            filename += ".tlg"
        
        self.model.fileName = filename    
        
        return self.fileSave()
                    
    def editAdd(self):
        index = self.treeView.currentIndex();
        if self.model.insertRow(0, index):
            index = self.model.index(0, 0, index)
            self.setCurrentIndex(index)
#            self.treeView.edit(index)
            self.setDirty()
        else:
            print("edit add failed")    
            #TODO: updateUi()
                
    def editCut(self):
        index = self.treeView.currentIndex()   
#        if (model->isTimedItem(index))
#            stopTiming();
        self.setCurrentIndex(self.model.cut(index))
#        editPasteAction->setEnabled(model->hasCutItem());
                        
    def editPaste(self):
        self.setCurrentIndex(self.model.paste(self.treeView.currentIndex()))
#        editHideOrShowDoneTasks(
#                editHideOrShowDoneTasksAction->isChecked());

    def editDelete(self):        
        index = self.treeView.currentIndex()
        if not index.isValid():
            return;
        
#        QString name = model->data(index).toString();
#        int rows = model->rowCount(index);
#        if (model->isTimedItem(index))
#            stopTiming();
#            
#        QString message;
#        if (rows == 0)
#            message = tr("<p>Delete '%1'").arg(name);
#        else if (rows == 1)
#            message = tr("<p>Delete '%1' and its child (and "
#                         "grandchildren etc.)").arg(name);
#        else if (rows > 1)
#            message = tr("<p>Delete '%1' and its %2 children (and "
#                         "grandchildren etc.)").arg(name).arg(rows);
#        if (!AQP::okToDelete(this, tr("Delete"), message))
#            return;
        self.model.removeRow(index.row(), index.parent())
        self.setDirty()
#        updateUi();        
                        
    def load(self, fileName):
        self.model.load(fileName)
    
    def setDirty(self, dirty = True):
        self.setWindowModified(dirty)       
    
    def setCurrentIndex(self, index):
        if index.isValid():
            self.treeView.scrollTo(index)
            self.treeView.setCurrentIndex(index) 
                    
