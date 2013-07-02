#include <QtCore/QCoreApplication>
#include <QDebug>

#include "lua/lua.hpp"

//lua�е��õ�c��������,ʵ�ּӷ�
int csum(lua_State* l)
{
    int a = lua_tointeger(l,1) ;
    int b = lua_tointeger(l,2) ;
    lua_pushinteger(l,a+b) ;
    return 1 ;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);

    char *pFileName = "haha.lua";

    if (luaL_dofile(L, pFileName) != 0) {
        return -1;
    }

    char *pFunctionName = "func_Add";
    lua_getglobal(L, pFunctionName);

    // 1+ 2 = ?
    lua_pushnumber(L, 3);
    lua_pushnumber(L, 2);

    if (lua_pcall(L, 2, 1, 0) != 0) {
        QString err = QString(lua_tostring(L, -1));
        lua_pop(L, 1); //��ջ�е���������Ϣ
        qDebug()<<err;
        return -1;
    }

    if (lua_isnumber(L, -1) == 1)
    {
        int nSum = lua_tonumber(L, -1);
        lua_pop(L, 1);
        qDebug()<<"result:"<<nSum;
        //        printf("[CLuaFn::CallFileFn]Sum = %d./n", nSum);
    }


//    lua_pushcfunction(L,csum) ;         //ע����lua��ʹ�õ�c����
//      lua_setglobal(L,"csum") ;           //�󶨵�lua�е�����csum

//      lua_getglobal(L,"mysum");           //����lua�е�mysum�������ú������ñ������ж����csum����ʵ�ּӷ�
//      lua_pushinteger(L,5) ;
//      lua_pushinteger(L,6) ;
//      if (lua_pcall(L,2,1,0) != 0) {
//          lua_pop(L, 1);
//          return -1;
//      }

//      int result = lua_tointeger(L, -1);
//      qDebug()<<"5 + 6 = "<<result;
//      lua_pop(L,1) ;

    lua_close(L);

    return a.exec();
}
