目前主流的web代理socks流量有如下  
https://github.com/sensepost/reGeorg  
https://github.com/L-codes/Neo-reGeorg  
https://github.com/nccgroup/ABPTTS  
https://github.com/SECFORCE/Tunna  
https://github.com/FunnyWolf/pystinger

工具本文测试的工具是Neo-reGeorg

环境搭建：  
(verify)kali_x64_en-us->桥接  
win10_1909_pro_x64_zh-chs->桥接  
2008_r2_dat_zh-chs->桥接、NAT双网卡->phpstudy搭建php环境  
2012_r2_std_zh-chs->NAT

经测试，启动Neo-reGeorg后：  
win10_1909_pro_x64_zh-chs本地浏览器通过自身的代理功能走Neo-reGeorg后，成功访问2012_r2_std_zh-chs  
win10_1909_pro_x64_zh-chs本地浏览器通过proxifier走Neo-reGeorg后，成功访问2012_r2_std_zh-chs  
(verify)kali_x64_en-us本地浏览器通过自身的代理功能走Neo-reGeorg后，成功访问2012_r2_std_zh-chs  
(verify)kali_x64_en-us本地浏览器（通过命令行启动的chrome可以，直接在命令行启动firefox则不可以）通过proxychains走Neo-reGeorg后，成功访问2012_r2_std_zh-chs

(verify)kali_x64_en-us下通过proxychains走Neo-reGeorg实现nmap扫描内网存活主机及主机开放端口需要使用
```
nmap -v -sT -Pn 172.16.35.0/24
```
但是测试时发现，会把很多没开放的端口误报为开放，并且proxychains telnet 172.16.35.139 87时，87端口明明没开放，也能通，有时间再去进一步排查以及测试pystinger

参考链接：  
https://www.freebuf.com/articles/web/255801.html  
https://guangchuangyu.github.io/cn/2018/09/proxychains/  
https://rich4rd.cc/2019/08/24/e5-86-85-e7-bd-91-e6-b8-97-e9-80-8f-ef-bc-9acs-e4-bb-a3-e7-90-86proxychainsnmap-e8-bf-9b-e8-a1-8c-e5-86-85-e7-bd-91-e6-89-ab-e6-8f-8f/
