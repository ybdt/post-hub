# 搭建过程
搭建ASP环境-win7安装IIS并运行ASP程序
https://blog.csdn.net/LeoD3201/article/details/44829997

目录浏览或默认文档问题
https://blog.csdn.net/simpleshao/article/details/88738586

从[https://msdn.itellyou.cn/](https://msdn.itellyou.cn/)下载SQL Server 2000以及Access

[Microsoft][ODBC Microsoft Access 驱动程序] 不能更新。数据库或对象为只读。  
修改access数据库文件所在目录的权限，创建用户Everyone，并为Everyone分配所有权限  
参考链接：https://bbs.csdn.net/topics/50064352

# 由于中间尝试过很多命令，不确定以下命令是否起作用
1、WINDOWS\temp文件夹的权限也要相同设置以下

2、开启32位应用程序支持  
```
Cscript C:\inetpub\adminscripts\adsutil.vbs SET W3SVC/AppPools/Enable32bitAppOnWin64 1
```
