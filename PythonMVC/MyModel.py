'''
Created on Feb 8, 2012

@author: zhzhong
'''
from PySide.QtCore import *
from PySide.QtGui import *
from testcase.TestCase import *


class MyModel(QAbstractItemModel):
    COLUMN_COUNT = 3
       
    def __init__(self, tc):
        QAbstractItemModel.__init__(self)
        self.tc = tc

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Horizontal and role == Qt.DisplayRole):
            if section == 0:
                return 'Action'
            elif section == 1:
                return 'Object'
            elif section == 2:
                return 'Parameter'
            else:
                return None
        
        return None

    def columnCount(self, parent_idx):
        return self.COLUMN_COUNT;

    def rowCount(self, parent_idx):
        # The rowCount() function simply returns the number of child items 
        # for the TreeItem that corresponds to a given model index, 
        # or the number of top-level items if an invalid index is specified:
        if not parent_idx.isValid():
            return self.tc.rootStep.childCount()
        
        parent_obj = parent_idx.internalPointer()
        return parent_obj.childCount()

    def index(self, row, column, parent_idx):
        assert column != None     
        
        if not parent_idx.isValid():
            functionStep = self.tc.rootStep.child(row)
            return self.createIndex(row, column, functionStep)
#            group = self.group_agent.get_group_by_row(row)
#            return self.createIndex(row, column, group)

        parent_obj = parent_idx.internalPointer()
#        if parent_obj.get_type() == Object.GROUP:
#            item = parent_obj.get_user_by_row(row)
#            return self.createIndex(row, column, item)
        if parent_obj.hasChildren():
            child = parent_obj.child(row)
            return self.createIndex(row, column, child)

        return QModelIndex()

    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return None

        obj = index.internalPointer()
        if role == Qt.DisplayRole:
            return obj.dataForColumn(index.column())

        return None

    def parent(self, child_index):
        if not child_index.isValid():
            return QModelIndex()

        child_obj = child_index.internalPointer()
#        if obj.get_type() == Object.USER:
#            parent_obj = obj.group
#            row = self.group_agent.index(parent_obj)
#            return self.createIndex(row, FIRST_COLUMN, parent_obj)
        parent_obj = child_obj.parent
        if parent_obj == self.tc.rootStep:
            return QModelIndex()
        
        grandfather_obj = parent_obj.parent
        row = grandfather_obj.rowNumber(parent_obj)
        
        return self.createIndex(row, 0, parent_obj)                

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
