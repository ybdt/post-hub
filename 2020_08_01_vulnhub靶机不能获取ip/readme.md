下载后使用vmware导入，出现提示，点击“重试”即可

导入后执行命令"nmap -sn -T4 172.16.35.0/24"，不能扫描到靶机ip

尝试1：  
怀疑是ip段172.16.35.0/24的问题，改为192.168.18.0/24，仍旧不行

尝试2：  
由于靶机介绍中推荐virtualbox，改用vbox，仍旧不行

尝试3： 
去网上搜索文章，开机时在欢迎界面输入“e”进入命令编辑模式，提示将ro改为rw signie init=/bin/bash，ctrl+x后会卡在某个地方，不能进入root shell

尝试4：  
继续排查，觉得可能是将ro及这一行后边的内容都改为rw signie init=/bin/bash，成功进入root shell

尝试5：  
经测试发现有些靶机在进入上述的root shell下会出现部分乱码的情况（比如靶机FunBox，字符“/”就需要shift+7，但是靶机MoriartyCorp就没有这个问题），果断弃用出现字符乱码的靶机

尝试6（问题的根本原理）：  
寻找不会出现字符乱码的靶机，执行命令"ip a"，查看当前网卡名称，用当前网卡名称替换/etc/network/interfaces中的网卡名称，如果其中无内容，可添加如下：  
auto eth0  
iface eth0 inet dhcp  
执行dhclient后能够获取ip，但是强制关机再启动后，仍旧获取不到ip  
执行"/etc/init.d/networking restart"失败，执行"systemctl restart network"仍旧失败，强制关机再启动后，仍旧获取不到ip  
此刻我不想弄了，疯了疯了！！！

尝试7（根本原理+新东西=解决新问题）：  
查阅资料发现ubuntu从17.10版本起更改了网络配置方式，新的配置文件位于/etc/netplan/00-installer-config.yaml，用当前网卡名称替换/etc/netplan/00-installer-config.yaml中的网卡名称，重启后成功获取到靶机ip

解决完成大概1-2天（4-6个小时左右），8月1号解决完成

参考链接：  
https://blog.csdn.net/qq_41918771/article/details/103636890  
https://blog.csdn.net/PeterWuu/article/details/105640638  
https://zh.codepre.com/ubuntu-4234.html  
https://blog.csdn.net/jian8182/article/details/106687659
