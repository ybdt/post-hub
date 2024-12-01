# Linux提权
## 0x01 一键提权
参考项目
```
Linux-Exploit-Suggester -> https://github.com/The-Z-Labs/linux-exploit-suggester
Linux-Exploit-Suggester-2 -> https://github.com/jondonas/linux-exploit-suggester-2
Traitor -> https://github.com/liamg/traitor
LinPEAS - Linux Privilege Escalation Awesome Script -> https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS
```
## 0x02 SUID提权
原理
```
linux下有一个特殊的权限机制，文件在运行时可以获取文件属主的权限，表现形式是权限位中带有s，如下所示：
-rwsr-xr-x. 1 root root 52K May 18  2022 /usr/bin/at
同时，这个文件如果还能执行命令，则可以用来提权

参考链接：
https://web.archive.org/web/20230922193909/https://tttang.com/archive/1793/
```
参考项目
```
GTFOBins -> https://gtfobins.github.io/
```

# Windows提权
## 0x01 一键提权
参考项目
```
Kernelhub项目：https://github.com/Ascotbe/Kernelhub
windows-kernel-exploits项目：https://github.com/SecWiki/windows-kernel-exploits
```
## 0x02 土豆提权
参考文章
```
https://forum.butian.net/share/860
https://github.com/uknowsec/SweetPotato
```