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

    QString fileName = "haha.js";
    QFile scriptFile(fileName);
    if (!scriptFile.open(QIODevice::ReadOnly)) {
        return -1;
    }
    QTextStream b(&scriptFile);
    QString contents = b.readAll();
    scriptFile.close();

    QScriptValue result = engine.evaluate(contents, fileName);
    qDebug()<<result.toString();

    return a.exec();
}
