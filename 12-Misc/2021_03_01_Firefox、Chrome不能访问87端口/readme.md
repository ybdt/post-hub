问题原因：  
Firefox、Chrome出于安全考虑，限制了对某些端口的访问

解决方案：  
1、Firefox  
地址栏访问about:config  
在搜索栏输入network.security.ports.banned.override，这应该是一个不存在的键，值类型选择字符串，点击加号，值输入87,6666  
页面刷新即可访问  
2、Chrome  
linux下配置launcher，给launcher加个选项“--explicitly-allowed-ports”，最终如下：  
```
/usr/bin/google-chrome-stable %U --password-store=basic --explicitly-allowed-ports=87,6666
```
windows下配置快捷方式，给快捷方式加个选项“--explicitly-allowed-ports”，最终如下：  
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --explicitly-allowed-ports=87,6666
```
页面刷新即可访问

参考链接：  
https://blog.csdn.net/qq_35720307/article/details/88661850
