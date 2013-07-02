#include "haha.h"

Haha::Haha(QObject *parent) :
    QObject(parent)
{
}

void Haha::sayHello(const QString &name, QString &result)
{
    result = "Hello " + name;
}
