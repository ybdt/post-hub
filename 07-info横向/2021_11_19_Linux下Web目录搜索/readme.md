### 场景
拿到一个命令执行的口子后，想要反弹shell，但目标不出网，考虑传Webshell，但不知道目标Web路径，此时可以搜索index.jsp所在的目录  
通常会想到使用find搜索
```
find / -name index.jsp
```
不过使用此命令在有的场景下会搜索很长时间仍旧没有结果，猜测可能是目标的文件系统太大或者其他问题

### 解决
改用更快的locate搜索
```
locate index.jsp
```
