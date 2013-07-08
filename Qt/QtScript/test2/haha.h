#ifndef HAHA_H
#define HAHA_H

#include <QObject>
#include <QStringList>

class Haha : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool enabled WRITE setEnabled READ isEnabled)

public:
    explicit Haha(QObject *parent = 0);
       
public slots:
    void setEnabled(bool enabled);
    bool isEnabled();

private:
    bool m_enabled;
};

#endif // HAHA_H
