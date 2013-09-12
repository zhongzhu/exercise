from PySide.QtCore import *
from PySide.QtGui import *
from tccodehighlighter import Highlighter

class MyItemSize(object):
    # size for displayed items
    MarginSize = 8
    PreviewWindowHeight = 100    
    TitleHeight = 20    

class SearchResultsDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(SearchResultsDelegate, self).__init__(parent)
        #self.sampleOneResultWidget = OneResultWidget()

    def sizeHint(self, option, index):
        """ Returns the size needed to display the item in a QSize object. """
        return QSize(option.rect.width(),  MyItemSize.MarginSize * 2 + MyItemSize.PreviewWindowHeight + MyItemSize.TitleHeight)
        # return self.sampleOneResultWidget.sizeHint()
        # if index.column() == 3:
        #     starRating = StarRating(index.data())
        #     return starRating.sizeHint()
        # else:
        #     return QStyledItemDelegate.sizeHint(self, option, index)        

    def paint(self, painter, option, index):
        """
        *** ITEM LAYOUT
        +----------------------------------------------------------+
        |                          margin                          |
        +-+------------------------------------------------------+-+
        | |                      tc title                        | |
        |M|------------------------------------------------------|M|
        | |                      preview window                  | | M = Margin
        +-+------------------------------------------------------+-+
        |                          margin                          |
        +----------------------------------------------------------+
        """

        if not index.isValid():
            pass

        QApplication.style().drawPrimitive(QStyle.PE_PanelItemViewItem, option, painter)

        # tc title
        titleRect = QRect()
        titleRect.setX(option.rect.x() + MyItemSize.MarginSize)
        titleRect.setY(option.rect.y() + MyItemSize.MarginSize)
        titleRect.setWidth(option.rect.width() - MyItemSize.MarginSize * 2)
        titleRect.setHeight(MyItemSize.TitleHeight)

        painter.save()
        f = QFont()
        f.setBold(True)
        painter.setFont(f)

        title = "the/path/to/your/testcase/getName.tc"

        fontMetrics = QFontMetrics(f)
        painter.drawText(titleRect, Qt.AlignLeft | Qt.AlignTop, fontMetrics.elidedText(title, Qt.ElideRight, titleRect.width()))
        painter.restore()

        # Preview window
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)

        previewWindow = QTextEdit()
        previewWindow.setFont(font)
        previewWindow.resize(option.rect.width() - MyItemSize.MarginSize * 2, MyItemSize.PreviewWindowHeight)

        highlighter = Highlighter(previewWindow.document())       
        previewWindow.setPlainText("print(\"haha\");")

        pixmap = QPixmap(previewWindow.size())        
        previewWindow.render(pixmap)

        previewWindowRect = QRect(option.rect.x() + MyItemSize.MarginSize, option.rect.y() + MyItemSize.MarginSize + MyItemSize.TitleHeight, previewWindow.width() - MyItemSize.MarginSize * 2, previewWindow.height())
        painter.drawPixmap(previewWindowRect, pixmap)
