#### 能过360

借助项目https://github.com/hack2fun/BypassAV

1、插件导入CS后，生成x64的shellcode，实际上不会生成exe（可能是插件的问题），而是生成/tmp/temp.go  
2、cp /tmp/temp.go /mnt/Desktop  
3、go build temp.go  
```
go build -ldflags "-H windowsgui" DesertFox.go  #无命令行窗口，隐藏执行
```

编译后会被Windows Defender查杀  
VirusTotal上的检出率是11/68，如下图  
![image](./pic/a.png)  

使用U盘拷贝到一台装有360杀毒和360卫士物理机上，temp.exe位于U盘中执行时，会有“U盘执行可执行文件的风险提醒”  
拷贝到U盘以外的位置，扫描后，未检测到，如下图  
![image](./pic/0.png)  
执行后成功收到反连，如下图  
![image](./pic/1.png)
