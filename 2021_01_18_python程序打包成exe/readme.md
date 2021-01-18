通过pyinstaller就2步  
pip install pyinstaller  
pyinstaller your_program.py  
参考链接：  
https://www.pyinstaller.org/  

通过py2exe  
通过官网下载安装包http://www.py2exe.org/  
创建一个文件setup.py，就4行，如下：  
1：from distutils.core import setup  
2：import py2exe  
3：  
4：setup(console=["hello.py"]); # 其中hello.py为你要打包的控制台应用程序名  
然后执行python setup.py py2exe  
报错：ImportError: DLL load failed: %1 不是有效的 Win32 应用程序。  
谷歌得知，可能是由于python的版本为64位，py2exe版本为32位导致的，经查看，本机的python为64位  
从python官网下载32位python2.7.15  
然后通过pip安装py2exe报错，使用之前下载的安装包成功安装  
执行python setup.py py2exe成功打包  

参考链接：  
https://blog.csdn.net/puma004/article/details/40742953  
https://blog.csdn.net/qq_28618765/article/details/72841934  
https://blog.csdn.net/churximi/article/details/50381827
