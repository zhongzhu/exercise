#ifndef HAHA_H
#define HAHA_H

#include <QObject>
#include <QStringList>

//Q_DECLARE_METATYPE(QStringList *)

class Haha : public QObject
{
    Q_OBJECT

public:
    explicit Haha(QObject *parent = 0);
       
public slots:
    int add(const QStringList &l);
};

#endif // HAHA_H
