#include <QtCore/QCoreApplication>
#include <QtDebug>
#include <QtScript>

#include "haha.h"

Q_SCRIPT_DECLARE_QMETAOBJECT(Haha, QObject*)

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    
    QScriptEngine engine;
    QScriptValue HahaClass = engine.scriptValueFromQMetaObject<Haha>();
    engine.globalObject().setProperty("Haha", HahaClass);

    engine.evaluate("var h = new Haha()");
    engine.evaluate("h.enabled = false");
    qDebug()<<engine.evaluate("'h is enabled:' + h.enabled").toString();

    return a.exec();
}
