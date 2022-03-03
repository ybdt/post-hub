# 修改apt源
cd /etc/apt/
cp ./sources.list ./sources.list.bak
rm ./sources.list
vim ./sources.list
```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiversie
```

参考链接：  
https://developer.aliyun.com/article/639051

# 修改pip源
cd ~
mkdir .pip
cd ./.pip
vim ./pip.conf
```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

参考链接：  
https://zhuanlan.zhihu.com/p/129867344  
https://www.linuxidc.com/Linux/2019-04/158178.htm

# 添加apt源，添加后可直接通过apt安装各个版本的python3
```
python3.8 --version
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
python3.8 --version
```
ubuntu18.04下默认python3为python3.6  
经测试，默认python3为哪个版本，安装的pip3即为哪个版本，即可修改默认python3，然后安装对应pip3

参考链接：  
https://www.yisu.com/ask/3907.html
