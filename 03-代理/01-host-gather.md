# 0x01-基于主机的信息收集
```
01、lscpu查看是一台物理机还是虚拟机
02、查看每一个用户的.bash_history内容（里面有好多宝藏）
03、查看每一个用户的~/.ssh/下是否有公钥私钥对，有公钥私钥对的话，也许能免密登录其他主机
04、查看每一个用户的~/.ssh/下是否有authorized_keys，有的话，可以查看哪些用户登录过，配合lastlog可查看哪些用户从哪个ip登录过
05、通过netstat -antup获知监听哪些端口，即获知提供哪些服务，当发现提供mysql服务，可直接通过本机登录mysql数据库
06、通过netstat -antup获知连接哪些端口，即获知连接到哪些服务，当发现连接到mysql服务，可查看mysql配置文件，进而尝试连接mysql数据库
07、查看crontab -l
08、查看dns配置cat /etc/resolv.conf、cat /etc/hosts
```