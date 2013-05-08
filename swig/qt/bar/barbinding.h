#ifndef BARBINDING_H
#define BARBINDING_H

#include<string>

using namespace std;

class Bar;
class BarBinding
{
public:
    BarBinding();
    ~BarBinding();
    int len(const string &str);
private:
    Bar *p;
};

#endif // BARBINDING_H
