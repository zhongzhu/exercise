#include "haha.h"

Haha::Haha(QObject *parent) :
    QObject(parent)
{
}

void Haha::setEnabled(bool enabled)
{
    m_enabled = enabled;
}

bool Haha::isEnabled()
{
    return m_enabled;
}
