#include <QtCore/QCoreApplication>
#include <QtDebug>
#include <QtScript>
#include <QStringList>
#include <QVariantMap>

#include "haha.h"

Q_SCRIPT_DECLARE_QMETAOBJECT(Haha, QObject*)

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    
    QScriptEngine engine;
    QScriptValue HahaClass = engine.scriptValueFromQMetaObject<Haha>();
    engine.globalObject().setProperty("Haha", HahaClass);

    QVariantMap map;
    map["a"] = 3;
    map["b"] = 4;

    QScriptValue v = engine.toScriptValue(map);
    engine.globalObject().setProperty("m", v);

    engine.evaluate("var h = new Haha()");
    qDebug()<<engine.evaluate("h.add(m)").toString();

    return a.exec();
}
