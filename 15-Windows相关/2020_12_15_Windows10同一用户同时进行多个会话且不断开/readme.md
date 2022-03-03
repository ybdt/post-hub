起因源于我通过ipad中的远程桌面客户端连接win10的时候，win10会自动锁屏，登陆win10后，ipad又会自动退出，反复登陆感觉太麻烦，故有此文  

使用stascorp的rdpwrap，[官网的仓库](https://github.com/stascorp/rdpwrap/)现在已经被关闭了，幸亏我之前存了一份  
现将我备份的分享给大家：链接：https://pan.baidu.com/s/1pPy4w06zobXzIHrm5zbTeA 提取码：7cq5   

解压后执行RDPConf.exe，在弹出的界面中取消勾选“Single session per user”，其他不用动，其中的Diagnostics部分会告诉你诊断结果，如果提示你未受支持，是因为你的远程桌面服务的版本大于它默认配置文件中所支持的最高版本，则需要用解压后的rdpwrap.ini（来自[这里](https://github.com/sebaxakerhtc/rdpwrap)）替换C:\Program Files\RDP Wrapper\下的rdpwrap.ini  

再次执行RDPConf.exe  
没问题后执行install.bat，执行完之后重启计算机  
然后执行RDPCheck.exe检查一下是否开启成功  

参考链接：  
https://blog.csdn.net/ljy1221/article/details/103731212  
https://github.com/sebaxakerhtc/rdpwrap  

最后，如果想ipad连接的时候，win10不锁屏，还可以使用第三方的远程管理软件如teamviewer、向日葵、anydesk  


2020/05/16更新  
采用上述方式后，发现有诸多问题，如：  
win10开机后，ubuntu连接win10，win10仍会自动锁屏  
ipad连接win10后，不能看到win10的桌面，会进入另一个会话  
故，卸载rdpwrap，改用anydesk作为替代，无上述问题
