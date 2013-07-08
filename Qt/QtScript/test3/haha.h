#ifndef HAHA_H
#define HAHA_H

#include <QObject>
#include <QStringList>

class Haha : public QObject
{
    Q_OBJECT

public:
    explicit Haha(QObject *parent = 0);
       
public slots:
    int add(QStringList &l);
    int add2(const QStringList &l);
};

#endif // HAHA_H
