#ifndef BAR_H
#define BAR_H

#if defined(BAR_LIBRARY)  
    #define BARSHARED_EXPORT __declspec(dllexport)  
#else  
    #define BARSHARED_EXPORT __declspec(dllimport)  
#endif

#include <string>
using namespace std;

class QString;

class BARSHARED_EXPORT Bar {
public:
    Bar();
    ~Bar();
    int len(const QString &str);
};

#endif // BAR_H
