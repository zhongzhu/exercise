#include <QString>
#include <QtDebug>
#include "bar.h"

int main()
{
    Bar bar;
    QString str = "bar";

    qDebug()<<str<<" len is: "<<bar.len(str);

    return 0;
}
