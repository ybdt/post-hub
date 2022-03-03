### 1、添加软路由
```
route.exe add 172.30.0.0 mask 255.255.0.0 172.30.0.254
route.exe delete 172.30.0.0
```

### 2、添加端口映射
```
netsh interface portproxy show v4tov4
netsh interface portproxy delete v4tov4 listenport=4444 listenaddress=192.168.1.142
netsh interface portproxy add v4tov4 listenport=4444 connectaddress=192.168.202.129 connectport=4444 listenaddress=192.168.0.142
```

### 3、Windows下批处理同时启动多个程序
```
@echo off
echo starting ProtonXXX... start /D D:\ProtonXXX ProtonXXX.exe
echo starting GoogleDriveSync... start /D "C:\Program Files\Google\Drive" googledrivesync.exe
```
