使用相对路径在github中添加图片，以为是添加的格式不对  
```
![image](./0.png)
```
后直接访问图片，发现都不能访问

查阅资料发现可能是由于v2ray科学上网导致的，网上的解决方案是添加如下到hosts文件  
192.30.253.112 github.com  
192.30.253.119 gist.github.com  
151.101.184.133 assets-cdn.github.com  
151.101.184.133 raw.githubusercontent.com  
151.101.184.133 gist.githubusercontent.com  
151.101.184.133 cloud.githubusercontent.com  
151.101.184.133 camo.githubusercontent.com  
151.101.184.133 avatars0.githubusercontent.com  
151.101.184.133 avatars1.githubusercontent.com  
151.101.184.133 avatars2.githubusercontent.com  
151.101.184.133 avatars3.githubusercontent.com  
151.101.184.133 avatars4.githubusercontent.com  
151.101.184.133 avatars5.githubusercontent.com  
151.101.184.133 avatars6.githubusercontent.com  
151.101.184.133 avatars7.githubusercontent.com  
151.101.184.133 avatars8.githubusercontent.com

但是添加后，不走代理的情况下，不能访问github，怀疑是上述中和github.com相关的前3条解析导致的，删除后，成功访问github，最终方案是添加如下到hosts文件  
151.101.184.133 raw.githubusercontent.com  
151.101.184.133 gist.githubusercontent.com  
151.101.184.133 cloud.githubusercontent.com  
151.101.184.133 camo.githubusercontent.com  
151.101.184.133 avatars0.githubusercontent.com  
151.101.184.133 avatars1.githubusercontent.com  
151.101.184.133 avatars2.githubusercontent.com  
151.101.184.133 avatars3.githubusercontent.com  
151.101.184.133 avatars4.githubusercontent.com  
151.101.184.133 avatars5.githubusercontent.com  
151.101.184.133 avatars6.githubusercontent.com  
151.101.184.133 avatars7.githubusercontent.com  
151.101.184.133 avatars8.githubusercontent.com

参考链接：  
https://v2ex.com/t/630242
