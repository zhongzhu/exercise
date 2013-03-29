from PySide import QtCore
from taskitem import TaskItem

COLUMN_COUNT = 3
Name, Today, Total = 0, 1, 2

TaskTag = "TASK"
NameAttribute = "NAME"
DoneAttribute = "DONE"
WhenTag = "WHEN"
StartAttribute = "START"
EndAttribute = "END"        

MimeType = "application/vnd.qtrac.xml.task.z"
    
class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)
        self.fileName = None
        self.rootItem = TaskItem()
        self.cutItem = None        
        
    def flags(self, index):          
        theFlags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        
        if index.isValid() and index.column() == Name:
            theFlags |= QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled
        
        return theFlags
        
    def data(self, index, role):
        if (not index.isValid()) or (index.column() < 0) or (index.column() >= COLUMN_COUNT):
            return None

        item = index.internalPointer()
        if item:
            column = index.column()
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                if column == Name:
                    return item.name
                elif column == Today:
                    return item.todaysTime()
                elif column == Total:
                    return item.totalTime()                            
            elif  role == QtCore.Qt.CheckStateRole:
                if column == Name:
                    if item.done:
                        return QtCore.Qt.Checked
                    else:
                        return QtCore.Qt.Unchecked  
            else:
                return None    
            
        return None
            
    def columnCount(self, parent):         
        if parent.isValid() and parent.column() != Name:
            return 0
        else:
            return COLUMN_COUNT        
    
    def index(self, row, column, parent):
        if row < 0 or column < 0 or column >= COLUMN_COUNT or (parent.isValid() and parent.column() != 0):
            return QtCore.QModelIndex()

        parentItem = self.itemForIndex(parent)
        assert(parentItem)
        
        if row >= parentItem.childCount():
            return QtCore.QModelIndex()
        
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        
        return QtCore.QModelIndex()    

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        if childItem:
            parentItem = childItem.parent()
            if parentItem == self.rootItem:
                return QtCore.QModelIndex()
            
            grandParentItem = parentItem.parent()
            if grandParentItem:
                row = grandParentItem.rowOfChild(parentItem)
                return self.createIndex(row, 0, parentItem)
        
        return QtCore.QModelIndex()
            
    def rowCount(self, parent):
        if parent.column() > Name:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if section == Name:
                return "Task/Subtask/..."
            elif section == Today:
                return "Time (Today)"
            elif section == Total:
                return "Time (Total)"
                
        return None        
    
    def setData(self, index, value, role):
        if (not index.isValid()) or index.column() != Name:
            return False
        
        item = self.itemForIndex(index)
        if item:
            if role == QtCore.Qt.EditRole:
                item.name = value
            elif role == QtCore.Qt.CheckStateRole:
                item.done = value
            else:
                return False
            
            self.dataChanged.emit(index, index)            
            return True
        
        return False
    
    def insertRows(self, row, count, parent):
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
                
        self.beginInsertRows(parent, row, row + count - 1)
        
        for i in range(count):
            item = TaskItem("New Task", False)
            parentItem.insertChild(row, item)

        self.endInsertRows()

        return True       
    
    def removeRows(self, row, count, parent):        
        if not self.rootItem:
            return False
        
        item = self.itemForIndex(parent)

        self.beginRemoveRows(parent, row, row + count - 1)
        for i in range(count):
            item.takeChild(row)
        self.endRemoveRows()
        
        return True

        
    def load(self, filename):
        if filename:
            self.fileName = filename
        else:
            raise ValueError
            
        f = QtCore.QFile(self.fileName)
        if not f.open(QtCore.QIODevice.ReadOnly):
            raise IOError
        
        #clear()
        #self.rootItem = TreeItem()           
        reader = QtCore.QXmlStreamReader(f) 
        self.readTasks(reader, self.rootItem)

        # important, used to ask the view to redraw its contents        
        self.reset()
        
    def save(self, filename = None):        
        if filename:
            self.fileName = filename
        
        if not self.fileName:
            raise "no filename specified"    
                
        f = QtCore.QFile(self.fileName)
        if not f.open(QtCore.QIODevice.WriteOnly|QtCore.QIODevice.Text):
            raise f.errorString()            
    
        writer = QtCore.QXmlStreamWriter(f)
        writer.setAutoFormatting(True)
        writer.writeStartDocument()
        writer.writeStartElement("TIMELOG")
        writer.writeAttribute("VERSION", "2.0")
        self.writeTaskAndChildren(writer, self.rootItem)
        writer.writeEndElement() #TIMELOG
        writer.writeEndDocument()
                
    def readTasks(self, reader, task):
        while not reader.atEnd():
            reader.readNext()
            name = reader.name()
            
            if reader.isStartElement():
                if name == TaskTag:
                    name = reader.attributes().value(NameAttribute)
                    done = reader.attributes().value(DoneAttribute) == "1"
                    task = TaskItem(name, done, task)
                    
                elif name == WhenTag:
                    start = QtCore.QDateTime.fromString(reader.attributes().value(StartAttribute), QtCore.Qt.ISODate)
                    end = QtCore.QDateTime.fromString(reader.attributes().value(EndAttribute), QtCore.Qt.ISODate)
                    task.addDateTime(start, end)
                    
            elif reader.isEndElement():
                if name == TaskTag:
                    task = task.parent()
                    
    def writeTaskAndChildren(self, writer, task):        
        if task != self.rootItem:
            writer.writeStartElement(TaskTag);
            writer.writeAttribute(NameAttribute, task.name)
            if task.done:
                writer.writeAttribute(DoneAttribute, "1")
            else:
                writer.writeAttribute(DoneAttribute, "0")
                
        for (start, end) in task.dateTimes:
            writer.writeStartElement(WhenTag);
            writer.writeAttribute(StartAttribute, start.toString(QtCore.Qt.ISODate))
            writer.writeAttribute(EndAttribute, end.toString(QtCore.Qt.ISODate))
            writer.writeEndElement() #When
            
        for child in task.childItems:
            self.writeTaskAndChildren(writer, child)
            
        if task != self.rootItem:
            writer.writeEndElement() #TASK         
                    
    def itemForIndex(self, index):
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item
            
        return self.rootItem           
                    
    def cut(self, index):
        if not index.isValid():
            return index
        
        self.cutItem = self.itemForIndex(index)
        assert(self.cutItem)
        
        parent = self.cutItem.parent();
        assert(parent)
        
        row = parent.rowOfChild(self.cutItem)
        assert(row == index.row())
        
        self.beginRemoveRows(index.parent(), row, row)
        child = parent.takeChild(row)
        self.endRemoveRows()
        assert(child == self.cutItem)
        
        if row > 0:
            row = row - 1
            return self.createIndex(row, 0, parent.child(row))

        if parent != self.rootItem:
            grandParent = parent.parent()
            assert(grandParent)
            return self.createIndex(grandParent.rowOfChild(parent), 0, parent)
    
        return QtCore.QModelIndex()
    
    def paste(self, index):
        if not index.isValid() or not self.cutItem:
            return index
        
        sibling = self.itemForIndex(index)
        assert(sibling)
        parent = sibling.parent()
        assert(parent)        
        row = parent.rowOfChild(sibling) + 1
        
        self.beginInsertRows(index.parent(), row, row)
        parent.insertChild(row, self.cutItem);
        child = self.cutItem
        self.cutItem = None
        self.endInsertRows()
        
        return self.createIndex(row, 0, child)

    ''' Drag and Drop '''       
    def supportedDropActions(self):
        return QtCore.Qt.MoveAction
    
    def mimeTypes(self):
        types = [MimeType]
        return types
    
    def mimeData(self, indexes):
        mimeData = QtCore.QMimeData()
        
        if not len(indexes) == 1:
            return mimeData
        
        item = self.itemForIndex(indexes[0])
        if item:
            xmlData = QtCore.QByteArray()
            writer = QtCore.QXmlStreamWriter(xmlData)
            self.writeTaskAndChildren(writer, item)
            mimeData.setData(MimeType, xmlData)
                   
        return mimeData
                   
    def dropMimeData(self, data, action, row, column, parent):
        print('******************dropMimeData')
        
        # Returns true if the data and action can be handled by the model; 
        # otherwise returns false.
        if action == QtCore.Qt.IgnoreAction:
            return True             

        if (action != QtCore.Qt.MoveAction)  or (column > Name) or (not data) or (not data.hasFormat(MimeType)):
            return False
                                                                                       
        parentItem = self.itemForIndex(parent)
        if parentItem:
#            emit stopTiming();
            xmlData = data.data(MimeType)
            reader = QtCore.QXmlStreamReader(xmlData)
            
            if row == -1:
                if parent.isValid():
                    row = parent.row()
                else:
                    row = self.rootItem.childCount()
                    
            self.beginInsertRows(parent, row, row)
            self.readTasks(reader, parentItem)
            self.endInsertRows()
            
            return True

        return False
    