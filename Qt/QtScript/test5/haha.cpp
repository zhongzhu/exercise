#include "haha.h"

Haha::Haha(QObject *parent) :
    QObject(parent)
{
}

int Haha::add(const QVariantMap &m)
{    
    return m["a"].toInt() + m["b"].toInt();
}
