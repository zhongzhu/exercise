#include <QtCore/QCoreApplication>
#include <QDebug>

#include "lua/lua.hpp"

//lua中调用的c函数定义,实现加法
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
        lua_pop(L, 1); //从栈中弹出错误信息
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


//    lua_pushcfunction(L,csum) ;         //注册在lua中使用的c函数
//      lua_setglobal(L,"csum") ;           //绑定到lua中的名字csum

//      lua_getglobal(L,"mysum");           //调用lua中的mysum函数，该函数调用本程序中定义的csum函数实现加法
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
