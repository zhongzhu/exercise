from PySide.QtCore import *
from PySide.QtGui import *
from OneResultWidget import OneResultWidget

class SearchResultsDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(SearchResultsDelegate, self).__init__(parent)
        self.sampleOneResultWidget = OneResultWidget()

    def sizeHint(self, option, index):
        """ Returns the size needed to display the item in a QSize object. """
        return self.sampleOneResultWidget.sizeHint()
        # if index.column() == 3:
        #     starRating = StarRating(index.data())
        #     return starRating.sizeHint()
        # else:
        #     return QStyledItemDelegate.sizeHint(self, option, index)        

    def paint(self, painter, option, index):
        # text = "hello: %s" % index.model().data(index, Qt.DisplayRole)
        # painter.drawText(option.rect, Qt.AlignCenter, text)
        painter.save()
        palette = QPalette(option.palette)

        widget = OneResultWidget()
        widget.setPic("%d" % index.row())        
        pixmap = QPixmap(widget.size())        
        widget.render(pixmap)

        widgetRect = QRect(option.rect.x(), option.rect.y(), widget.width(), widget.height())
        print(option.rect.x(), option.rect.y(), widget.width(), widget.height())
        painter.drawPixmap(widgetRect, pixmap)
        # label->setPalette(palette);
        # label->setFixedSize(qMax(0,option.rect.width()),option.rect.height());
        # label->setHtml("<body>\n"
        #                "</style></head><body style=\"font-family:'MS Shell Dlg 2'; font-size:8.5pt; font-weight:400; font-style:normal;\">\n"
        #                "<img src=\":/image/square.png\"/>" "<span style=\" font-size:8pt;\">" "     "
        #                + text+ "</body>");
        # label->setStyleSheet("border-style:none");
        # paintWidget(painter,option.rect,label);
        
        painter.restore()