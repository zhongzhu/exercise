'''
Created on Dec 13, 2012

@author: zhzhong
'''

class TaskItem(object):
    def __init__(self, name = "", done = False, parent=None):
        self.parentItem = parent
        self.name = name
        self.done = done
        self.childItems = []
        self.dateTimes = []
        
        if parent:
            parent.addChild(self)
        
    def addChild(self, item):
        item.parentItem = self
        self.childItems.append(item) 

    def insertChild(self, row, item):
        item.parentItem = self
        self.childItems.insert(row, item)

    def takeChild(self, row):
        item = self.childItems.pop(row)
        assert(item)
        item.parentItem = None
        
        return item
    
    def swapChildren(self, oldRow, newRow):
        self.childItems[oldRow], self.childItems[newRow] = self.childItems[newRow], self.childItems[oldRow] 
        
    def child(self, row):
        return self.childItems[row]   
    
    def childCount(self):
        return len(self.childItems)         

    def parent(self):
        return self.parentItem
    
    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0    
    
    def todaysTime(self):
        return "haha"
        
    def totalTime(self):
        return "hihi"            

    def addDateTime(self, start, end):
        self.dateTimes.append((start, end))
        
    def rowOfChild(self, child):
        return self.childItems.index(child)