#include "haha.h"

Haha::Haha(QObject *parent) :
    QObject(parent)
{
}

int Haha::add(QStringList &l)
{
    return 1 + l.at(0).toInt();
}

int Haha::add2(const QStringList &l)
{    
    return 1 + l.at(0).toInt();
}
