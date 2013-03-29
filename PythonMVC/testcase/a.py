'''
Created on Feb 10, 2012

@author: zhzhong
'''
from xml.dom import minidom
from xml.dom.minidom import *

class A:
    def haha(self):
        b = B()
        b.create();

class B:
    def create(self):
        return A()

if __name__ == '__main__':
    
#    doc = minidom.parse('a.xml') 
#    root  = doc.documentElement
#    for n in root.childNodes:
#        print(n.nodeName, n.nodeValue, n.nodeType)
        
#    nodes = root.getElementsByTagName('procedure')
#    print(nodes)
    
    a = A()
    a.haha()