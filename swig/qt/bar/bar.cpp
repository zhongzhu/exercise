#include <QString>
#include "bar.h"


Bar::Bar()
{
}
Bar::~Bar()
{
}

int Bar::len(const QString &str)
{
    return str.size();
}
