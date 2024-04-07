发现自己经常需要在新环境下安装Metasploit，每次都要查阅官方文档效率有点低，故有此笔记

# Windows下安装
```
下载安装器，地址：https://windows.metasploit.com/metasploitframework-latest.msi
一路下一步即可
```

# Linux（Ubuntu18.04）下安装
一条命令自动安装
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
chmod 755 msfinstall && \
./msfinstall
```

# 参考链接
https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html  