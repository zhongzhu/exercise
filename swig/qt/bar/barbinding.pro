TEMPLATE = lib
QT       -= gui

TARGET = _bar

INCLUDEPATH += $$PWD \
    D:/Python27/include

HEADERS += barbinding.h

SOURCES += barbinding.cpp \
	bar_wrap.cxx

LIBS += -L$$PWD/release -lbar -LD:/Python27/libs -lpython27
