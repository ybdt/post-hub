基于项目：https://github.com/lanyi1998/DNSlog-GO

下载到vps（ubuntu 18.04）上执行后报错：/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found，此时要么安装对应版本的库，要么在当前vps下重新编译

我选择重新编译，使用apt安装go环境，编译DNSlog-GO时会报错找不到库，可是库就在当前目录下啊，一番排查后发现，apt安装的go版本是1.10，这里涉及到一个环境变量GO111MODULE的知识点，总之go 1.10不能从当前目录下找到库，还是因为ubuntu 18.04版本太低了

重新从官方下载并安装1.18版本，配置环境变量，可成功编译

启动时发现53端口被占用，执行命令：systemctl stop systemd-resolved

阿里云购买一个域名：a.com，开始配置  
添加一个A记录，名为ns，值为vps的ip地址  
添加一个ns记录，名为log，值为ns.a.com（刚才添加的A记录）  

vps放行全部tcp、icmp、udp

config.yaml中如下
```
HTTP:
  port: 30000
  # {"token":"用户对应子域名"}
  user: {"changbaishanlab": "red"}
  consoleDisable: false
Dns:
  domain: log.changbaishanlab.online
```

参考文章：  
https://www.f12bug.com/archives/dnslog平台搭建  
https://cn-sec.com/archives/1526334.html  
https://cloud.tencent.com/developer/article/1948254  