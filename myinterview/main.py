'''
Created on Dec 25, 2012

@author: zhzhong
'''

import sys
from PySide import QtCore
from PySide import QtGui
import interview_rc
from model import Model

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    page = QtGui.QSplitter()
    data = Model(3, 2, page);
    selections = QtGui.QItemSelectionModel(data)
    
    table = QtGui.QTableView()
    table.setModel(data)
    table.setSelectionModel(selections)
#    table.horizontalHeader().setMovable(True)
#    table.verticalHeader().setMovable(True)
    # Set StaticContents to enable minimal repaints on resizes.
#    table.viewport().setAttribute(QtCore.Qt.WA_StaticContents)
    page.addWidget(table)
    
    list = QtGui.QListView()
    list.setModel(data);
    list.setSelectionModel(selections);
    list.setViewMode(QtGui.QListView.IconMode);
    list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection);
    list.setAlternatingRowColors(False);
#    list.viewport().setAttribute(Qt::WA_StaticContents);
#    list.setAttribute(Qt::WA_MacShowFocusRect, false);
    page.addWidget(list);    
    
    
    tree = QtGui.QTreeView()
    tree.setModel(data);
    tree.setSelectionModel(selections);
    tree.setUniformRowHeights(True);
    tree.header().setStretchLastSection(False);
#    tree.viewport().setAttribute(Qt::WA_StaticContents);
    # Disable the focus rect to get minimal repaints when scrolling on Mac.
#    tree.setAttribute(Qt::WA_MacShowFocusRect, false);
    page.addWidget(tree);
    
    page.setWindowIcon(QtGui.QPixmap(":/images/interview.png"))
    page.setWindowTitle("Interview")
    page.show()

    sys.exit(app.exec_())
            