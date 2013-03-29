'''
Created on Dec 25, 2012

@author: zhzhong
'''
from PySide import QtCore
from PySide import QtGui
from node import Node

class Model(QtCore.QAbstractItemModel):
    '''
    classdocs
    '''

    def __init__(self, rows, columns, parent=None):
        super(Model, self).__init__(parent)
        self.rc = rows
        self.cc = columns    
        self.services = QtGui.QPixmap(":/images/services.png") 
        self.iconProvider = QtGui.QFileIconProvider()
        self.tree = [Node()] * rows
        
    def rowCount(self, parent):
        if (parent.isValid()):
            return 0
        else:
            return self.rc
        
    def columnCount(self, parent):
        return self.cc
    
    def flags(self, index):
        if not index.isValid():
            return 0
        
        return QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            return "Item {}:{}".format(index.row(), index.column())
        
        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                return self.iconProvider.icon(QtGui.QFileIconProvider.Folder)
            
            return self.iconProvider.icon(QtGui.QFileIconProvider.File)
        
        return None

    def index(self, row, column, parent):       
        if (0 <= row < self.rc) and (0 <= column < self.cc):
            if parent.isValid():
                # Tree
                print("Index Tree")
                parentNode = parent.internalPointer()
                node = self.creatNode(row, parentNode)
                if node:
                    return self.createIndex(row, column, node);                
            else:
                # Table/List
                return self.createIndex(row, column, None);

    
        return QtCore.QModelIndex()

    def parent(self, index):
        # Table/List: just return QtCore.QModelIndex()
#        print("parent")
        if index.isValid():          
            childNode = index.internalPointer()                        
            if childNode:
                # Tree only
                parentNode = childNode.parentNode            
                if parentNode:                   
                    grandParentNode = parentNode.parentNode
                    if grandParentNode:
                        row = grandParentNode.rowOfChild(parentNode)
                        return self.createIndex(row, 0, parentNode)
                
        return QtCore.QModelIndex()
    
#    def headerData(self, section, orientation, role):
#        if role == QtCore.Qt.DisplayRole:
#            return section
#        if role == QtCore.Qt.DecorationRole:
#            return self.services
        
#        return QtCore.QAbstractItemModel.headerData(section, orientation, role)   

    '''
        private functions
    '''
    def creatNode(self, row, parentNode):
        if parentNode and len(parentNode.children) == 0:
            parentNode.chilren = [Node(parentNode)] * self.rc
        
        v = None    
        if parentNode:
            v = parentNode.children
        else:
            v = self.tree
            
        return v[row]
            
