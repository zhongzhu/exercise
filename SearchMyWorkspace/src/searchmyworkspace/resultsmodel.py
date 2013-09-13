from PySide import QtCore
from PySide import QtGui
from roles import ResultRoles
from searcher import Searcher

# results = [ 
#     {ResultRoles.TitleRole: "path/to/your/testcase/a.tc", 
#     ResultRoles.PreviewContentRole: """    comment ***************  1. How to format a string using % and variables***************          eval $i = 9
#         eval $i = 9
#       eval $j = 5
#       eval $str = "abc %1 def %2"
#       eval $str = $str.arg($i).arg($j)""",
#       ResultRoles.AuthorRole:"zhu@haha.com"},
#     {ResultRoles.TitleRole: "path/to/your/sanity/b.tc", 
#      ResultRoles.PreviewContentRole: """        print g_arr: $str
#         if $local_arr.size() != 3
#           failCase failed for arr type, size is wrong
#         if ($local_arr[0] != "a") || ($local_arr[1] != "b") || ($local_arr[2] != "c")
#           failCase failed for arr type, content is wrong""",
#           ResultRoles.AuthorRole:"hihi@haha.com"}
#          ]

class SearchResultsModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(SearchResultsModel, self).__init__(parent)
        self.results = []

    def search(self, query):
        searcher = Searcher(query)        
        self.results = searcher.search().docs
        self.reset()

    def data(self, index, role):     
        if not index.isValid():
            return None

        if index.row() >= len(self.results):
            return None

        if role == QtCore.Qt.DisplayRole:
            return self.results[index.row()]["tcname"]
        elif role == ResultRoles.TypeRole:
            return self.results[index.row()]["type"]    
        elif role == ResultRoles.AuthorRole:
            return self.results[index.row()]["author"]                
        elif role == ResultRoles.DateRole:
            return self.results[index.row()]["created"]                      
        elif role == ResultRoles.TitleRole:
            return self.results[index.row()]["tcname"]
        elif role == ResultRoles.PreviewContentRole:
            return self.results[index.row()]["content"]
        else:
            return None

    def rowCount(self, parent):
        return len(self.results)