#-------------------------------------------------
#
# Project created by QtCreator 2013-06-25T15:59:35
#
#-------------------------------------------------

QT       += core

QT       -= gui

TARGET = haha
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app
INCLUDEPATH += $$PWD \
    $$PWD/lua

LIBS += -Llua -llua

HEADERS += lua/lua.hpp
SOURCES += main.cpp
