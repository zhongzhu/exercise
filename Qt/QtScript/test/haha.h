#ifndef HAHA_H
#define HAHA_H

#include <QObject>

class Haha : public QObject
{
    Q_OBJECT

public:
    explicit Haha(QObject *parent = 0);
       
public slots:
    void sayHello(const QString &name, QString &result);
};

#endif // HAHA_H
