# 前言
Windows Server自2012起，不能直接通过mimikatz抓密码，想抓密码需要修改注册表，然后让用户重新登录，可实战中有的场景是服务器管理员一直没有登录（可能这台服务器被遗忘了。。），此时我们可以退而求其次，不抓取密码通过一个技巧直接登录管理员Administrator的桌面

# 过程
假如我们拿到一个system权限的webshell（针对中间件如php-fpm、Tomcat、Weblogic的上传攻击或漏洞攻击通常都是system权限）  
kill掉杀软添加用户或通过某种技巧绕过防护添加用户，并将添加的用户添加到管理员组  
通过代理工具将目标的远程桌面端口映射出来  
用新添加的用户登录到目标的远程桌面  
首先需要通过psexec启动一个system权限的cmd（注意，后面的命令tscon 1需要system权限），命令行下执行tscon 1切换到管理员Administrator的桌面，这里1为Administrator的会话id，可通过query user查询  

# 结果
结果展示如下图  
![pic](./pic/01.png)  
![pic](./pic/01.png)  