D:\GitHub\exercise\swig>D:\swigwin-2.0.9\swig -python example.i
D:\GitHub\exercise\swig>gcc -shared -o _example.pyd example.c example_wrap.c -I"D:\Python27\include" -L"D:\Python27\libs" -lpython27