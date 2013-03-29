'''
Created on Dec 25, 2012

@author: zhzhong
'''

class Node(object):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        self.parentNode = parent
        self.children = []
        
        if parent:
            self.addChild(self)
        
    def addChild(self, node):
        node.parentNode = self
        self.children.append(node)        
        
    def child(self, row):
        return self.children[row]        

    def rowOfChild(self, child):
        return self.children.index(child)    
        