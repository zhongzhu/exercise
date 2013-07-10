#include "haha.h"

Haha::Haha(QObject *parent) :
    QObject(parent)
{
}

int Haha::add(const QStringList &l)
{    
    return 1 + l.at(0).toInt();
}
