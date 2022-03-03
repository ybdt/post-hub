文件系统FAT32不支持超过4GB的单个文件（windows安装镜像中目录sources下的install.wim就超过了4GB）  
想使用超过4GB的单个文件，需要使用文件系统NTFS  
可是引导模式UEFI不支持NTFS  
如果引导模式改为legacy BIOS，则对应的分区表格式MBR会限制硬盘的最大容量为2TB，可服务器的硬盘有4T  
还是需要使用UEFI，以及对应的GPT格式  
所以需要想办法解决UEFI支持NTFS？  
参考链接：  
https://blog.csdn.net/WPwalter/article/details/79392731  
https://rufus.ie/downloads/  

遇到的坑：  
教程中使用的是版本2.8.xxx，最新版是3.5.xxx，我使用最新版，参照教程，刻录过程碰到好多错误  
使用版本2.8.xxx，成功刻录  
启动后，使用默认选项即可，只是勾选上“检查设备坏块”  

以后懂原理可以使用不同的工具，因为怎么调整参数，以及报错什么意思我都知道，如果不想去学那个原理，则尽量保持和教程一摸一样  
结果发现，install.wim没超过4GB，fuck！！！  

windows安装期间将mbr格式转换为gpt格式  
参考链接：https://blog.csdn.net/WPwalter/article/details/79392645  
（或许也可以删除分区，重新创建，还没测试）  

分区表格式gpt及mbr，区别及查看方式？  
主要区别：gpt支持识别大于2TB的磁盘  
参考链接：  
https://www.reneelab.com.cn/m/mbr-gpt-difference.html  
https://baijiahao.baidu.com/s?id=1606373985523544941&wfr=spider&for=pc  

经查阅资料发现，可能是由于intel cpu从6代开始，主板中不自带usb驱动程序，同时win7中默认不自带驱动程序  


## 更新
提示驱动问题，解决方案如下：  

对win7启动盘写入驱动程序，过程参考https://www.gigabyte.cn/WebPage/-79/usb.html 或 https://www.zhihu.com/question/52060664 ，其中  
Windows USB Installation Tool的下载地址https://download.gigabyte.cn/FileList/Utility/mb_utility_windowsimagetool.zip  
可是最后我的写入提示失败，经检查，我刻录的启动盘是iso是08非08 r2，怀疑可能因为这个  
或  
刻录一个12 r2的系统盘，安装过程中提示系统的mbr分区表和u盘启动盘的gpt分区表不兼容  
重新刻录，在分区表处选择mbr和gpt，重启启动，成功启动  
