内网横向时，有些漏洞的利用工具是基于kali下的，因此我们需要在kali下配置代理

Kali 2023.2  
借助proxychains，配置文件位于/etc/proxychains4.conf  
修改最后一行
```
socks5 192.168.3.1 7890
```
经测试，执行如下命令
```
proxychains firefox
proxychains apt
```
均可以走代理