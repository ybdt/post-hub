# 0x00 简介
原理：go语言实现的loader  
测试的杀软：360全家桶、腾讯电脑管家、火绒、Windows Defender  
CS：Cobalt Strike 4.2  
Metasploit：暂未测试  

# 0x00 结论
能过360全家桶、腾讯电脑管家  
不能过Windows Defender、火绒  

# 0x01 注意
腾讯电脑管家：关闭自动举报  
360杀毒：关闭用户体验、程序错误、可疑文件  
360安全卫士：关闭用户体验、云安全、网址云安全  
火绒：关闭用户体验  
Windows Defender：关闭自动提交样本  

# 0x02 过程
1、Kali下安装go环境，参考：https://blog.csdn.net/Soda_199/article/details/107021540  
2、下载项目：https://github.com/hack2fun/BypassAV  
```
CS导入插件后，生成x64的shellcode，实际上不会生成exe（可能是插件的问题），而是生成/tmp/temp.go  
cp /tmp/temp.go /mnt/Desktop  
go build temp.go  

go build -ldflags "-H windowsgui" DesertFox.go#无命令行窗口隐藏执行
```
3、CS导入插件后，Attacks->BypassAV，勾选x64的shellcode，能够生成exe  
4、拷贝到宿主机后，使用Defender扫描，未检测为病毒，但执行的时候会提示病毒  
5、拷贝到装有360、火绒、腾讯的虚拟机下测试，只有火绒检测为病毒，如下图  
![image](./pic/1.png)  
6、关闭火绒保留360、腾讯，执行shellcode，成功上线CS，如下图  
![image](./pic/2.png)  
