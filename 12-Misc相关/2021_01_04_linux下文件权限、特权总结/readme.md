复习一下linux下命令ln的用法：  
ln target link_name  
ln /bin/ping#创建硬链接到当前目录  
ln /bin/ping ./#创建硬链接到指定目录  
ln -t ./ /bin/ping#创建硬链接到指定目录  
默认是创建硬链接，想创建软链接需要加上选项-s

linux下动态链接库的搜寻方式  
参考链接：  
http://shibing.github.io/2016/08/20/%E5%8A%A8%E6%80%81%E9%93%BE%E6%8E%A5%E4%B8%8Erpath/

对linux下/执行ls -alh会发现/tmp/的权限是：  
drwxrwxrwt  22 root root  32K 10月 12 11:19 tmp  
这里的t表示：任何人都有权限在此目录下写文件，但不能删除别人的文件  
想要为目录分配权限t，可执行：  
mkdir ./test/  
chmod 1777 ./test/  https://blog.csdn.net/u014791046/article/details/51908325  
另外一种形式：chmod [u|g|o|a][+|-]t ./test/经测试发现，chmod [u|g]+t ./test/无效，chmod [o|a]+t ./test/只对其他用户有效  
参考链接：  
https://blog.csdn.net/u014791046/article/details/51908325

linux下对一个文件的r、w、x分别是：是否能查看文件内容、是否能编辑文件内容（对内容添加、修改、删除）、是否能执行文件  
linux下对一个目录的r、w、x分别是：是否能查看目录内容、是否能编辑目录内容（在目录下添加、删除文件）、是否能进入目录  
查阅资料后进一步总结如下：  
![image](./0.png)  
参考链接：  
https://blog.csdn.net/Garfield777/article/details/95377619  
https://blog.csdn.net/cdu09/article/details/10310103
