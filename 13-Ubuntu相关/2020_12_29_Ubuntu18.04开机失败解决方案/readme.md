问题描述：  
前一天强制关机，今天早上开机提示“ext4 read failed ...”

解决方案：  
再次强制关机，开机后会进入启动项选择界面，选择“Advanced options for ubuntu”，进入子菜单后会有4个选项  
linux ...  
linux ... recovery mode  
linux ...  
linux ... recovery mode  
选择第3个，第3个是最后一次正确的内核，即可成功进入系统

参考链接：  
https://blog.csdn.net/u010953609/article/details/89487164  
https://ywnz.com/linuxjc/5006.html

# update on 2021/02/22
最近频繁的出现开机失败的问题，甚至开机后会突然关机  
不能继续装死，遂花时间解决之

查阅一番资料后发现，可能是由于之前多次强制关机导致的文件系统错误（这里要注意，linux系统下不要轻易强制关机或强制重启）  
开机按Esc进入开机菜单，选择Recovery模式->选择fsck，但不能执行fsck，查阅后发现，磁盘只分了一个区且挂载到了根目录下，是不能执行fsck的  
尝试在根目录下“touch /fsckforce”，并写入“fsck -y /dev/sda1”，重启后并没有强制执行fsck

继续查阅资料，目前只有两条路：  
1、制作一个类似win pe的ubuntu启动盘，取消挂载到根目录的分区，然后使用fsck修复  
2、直接改用windows系统

ubuntu的GUI还是差点意思，导致偶尔会卡死，我这性格肯定会强制关机，故选择第2条路
