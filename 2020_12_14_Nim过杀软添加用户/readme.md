参考自：  
https://mp.weixin.qq.com/s?__biz=MzU0MjUxNjgyOQ==&mid=2247486414&idx=1&sn=a6ea7ea5f99364fd321112f9b81b5b8b&exportkey=AaDdzYZzU29Zs1xkXDz%2FYeQ%3D&pass_ticket=uywmwG50B9SRCCijI3nkcLmPfqWsDYj7afHS8UbBj949CenjRXueIAhbRa63W8hx&wx_header=0  
https://github.com/lengjibo/NetUser

netuser.exe是我编译后的  
前提条件：需要管理员权限  
用户名：ybdt  
密码：1qaz@WSX

原理：  
直接调用Windows API中的NetUserAdd和NetLocalGroupAddMembers  
利用小众语言nim的天然静态免杀性  

免杀效果：  
![image](./pic/0.png)
