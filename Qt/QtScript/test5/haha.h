#ifndef HAHA_H
#define HAHA_H

#include <QObject>
#include <QStringList>
#include <QVariantMap>

class Haha : public QObject
{
    Q_OBJECT

public:
    explicit Haha(QObject *parent = 0);
       
public slots:
    int add(const QVariantMap &m);
};

#endif // HAHA_H
