//barbinding.cpp

#include <QString>
#include "barbinding.h"
#include "bar.h"

BarBinding::BarBinding()
{
    p = new Bar();
}

BarBinding::~BarBinding()
{
    if (p) {
        delete p;
        p = NULL;
    }
}

int BarBinding::len(const string &str)
{
    if (p) {
        QString s(str.c_str());
        return p->len(s);
    } else {
        return -1;
    }
}

