#include <QtCore/QCoreApplication>
#include <QtDebug>
#include <QtScript>
#include <QStringList>

#include "haha.h"

Q_SCRIPT_DECLARE_QMETAOBJECT(Haha, QObject*)

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    
    QScriptEngine engine;
    QScriptValue HahaClass = engine.scriptValueFromQMetaObject<Haha>();
    engine.globalObject().setProperty("Haha", HahaClass);

    QStringList l;
    l<<"2";
    QScriptValue v = qScriptValueFromSequence(&engine, l);
    engine.globalObject().setProperty("v", v);

    engine.evaluate("var h = new Haha()");
    qDebug()<<engine.evaluate("h.add(v)").toString();

    return a.exec();
}
