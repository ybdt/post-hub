# 搜索
## 搜索包含特定字符串内容的文件
```
grep -rn "jdbc:oracle" /opt/SuperMap/TongWeb7.0.4.1/domains/tw_80/
```
## find命令替换
```
locate

locate命令要比find -name快得多，原因在于它不搜索具体目录，而是搜索一个数据库/var/lib/mlocate/mlocate.db 。这个数据库中含有本地所有文件信息。
```