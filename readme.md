# 01-远控C2
```
0x01 远控优秀项目
    https://github.com/quasar/Quasar
    https://github.com/yuanyuanxiang/SimpleRemoter【主控端win10，被控端win11，虚拟机桥接，将生成的demo.exe和DLL放入被控端，经测试，可用】
    https://www.vipshare.com/【WorkWin】
    https://www.netsupportmanager.com/zh-CN/【NetSupportManager】
    https://github.com/moom825/xeno-rat
    https://anydesk.com/en

0x02 C2优秀项目
    https://www.cobaltstrike.com/
    https://bruteratel.com/
    https://nighthawkc2.io/
    https://github.com/n1nj4sec/pupy
    https://github.com/rapid7/metasploit-framework
    https://github.com/HavocFramework/Havoc
    https://github.com/BishopFox/sliver
    https://github.com/its-a-feature/Mythic
    https://github.com/Adaptix-Framework/AdaptixC2【类似Havoc，Client端C++ QT、Server端Golang、Beacon端C/C++】

0x03 Windows权限维持
    1、启动文件夹
    2、注册表
    3、服务
    4、任务计划

0x04 Linux权限维持
    1、修改/etc/shadow中密码
    2、写入ssh公钥
```

# 02-权限提升
```
# 0x01 Windows下权限提升
    01 优秀项目
        https://github.com/Ascotbe/Kernelhub
        https://github.com/SecWiki/windows-kernel-exploits
        https://forum.butian.net/share/860
        https://github.com/uknowsec/SweetPotato
        https://github.com/zcgonvh/DCOMPotato/tree/master
        https://forum.butian.net/share/860

# 0x02 Linux下权限提升
    01 优秀项目
        https://github.com/The-Z-Labs/linux-exploit-suggester
        https://github.com/jondonas/linux-exploit-suggester-2
        https://github.com/liamg/traitor
        https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS
        https://gtfobins.github.io/
    02 SUID提权
        原理很简单自行DeepSeek，具体做法是，执行如下命令寻找具有SUID位的可执行文件
        find / -perm -4000 -type f -exec ls -l {} \;
```

# 03-隧道搭建
```
0x01 优秀项目
    https://github.com/CodeSecurityTeam/frp【服务端Ubuntu 22.04，在Win10下编译后，，在Win11下执行，经测试可成功上线】
    https://github.com/jpillora/chisel
    https://github.com/zema1/suo5
    https://github.com/L-codes/Neo-reGeorg
0x02 Tailscale
    基于WireGuard的一次性Socks5代理，Socks5代理在建立的VPN隧道中，感觉还不错，暂未在实战中测试
    项目地址：https://github.com/Yeeb1/SockTail
```

# 04-凭证窃取
```
# 0x01 Windows下凭证窃取
    01 优秀项目
        https://github.com/gentilkiwi/mimikatz
        https://github.com/StarfireLab/SharpWeb
        https://dre4merp.github.io/2024/12/利用-seclogon-ppid-spoofing-实现-dump-lsass-内存/
        https://vari-sh.github.io/posts/doppelganger/
    02 键盘记录
        https://cicada-8.medium.com/im-watching-you-how-to-spy-windows-users-via-ms-uia-c9acd30f94c4【创新的键盘记录方式，绕过EDR监控】
        https://github.com/CICADA8-Research/Spyndicapped

# 0x02 Linux下凭证窃取
    01 可以获取密文
        1.1 读取/etc/shadow后，使用cmd5进行解密：
            https://www.cmd5.com/
            注意，在cmd5中先识别类型，再进行解密
        1.2 若cmd5中不能解密，可尝试hashcat解密，使用如下网站识别加密类型：
            https://www.tunnelsup.com/hash-analyzer/
            https://hashcat.net/wiki/doku.php?id=example%20hashes
            爆破使用如下字典：
            https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
            最后执行如下命令：
            hashcat -m 3200 ./hash.txt ./rockyou.txt
    02 无法获取密文
        01、劫持ssh密码

# 0x03 软件凭据窃取
    https://github.com/AlessandroZ/LaZagne
    https://github.com/moonD4rk/HackBrowserData
    https://github.com/qwqdanchun/Pillager
    https://github.com/djhohnstein/SharpWeb
    https://github.com/Meckazin/ChromeKatz
```

# 05-主机敏感信息收集
```
# 0x01 Windows下主机敏感信息收集
    01 优秀项目
        https://github.com/aleenzz/InjectSQLServer【ASPX网站数据库密码加密存储】
        https://github.com/qwqdanchun/Pillager
        https://github.com/lintstar/SharpHunter
        https://github.com/GhostPack/Seatbelt

# 0x02 Linux下主机敏感信息收集
```

# 06-内网探测扫描
```
0x01 优秀项目
    https://mp.weixin.qq.com/s/tqd9jJJv4bmzN6xVdpGDow
    https://github.com/shmilylty/netspy
    https://github.com/shadow1ng/fscan
    https://github.com/lcvvvv/kscan
    nltest

0x02 文件切割
    通过webshell上传文件失败时，有时是因为文件过大，可尝试先分割，上传后再合并
    md5sum f
    split -b 3M --verbose f f_
    cat f_aa f_ab f_ac > f
    md5sum f
```

# 07-内网服务攻击
```
# 0x01 数据库攻击
    01 优秀项目
        https://github.com/SafeGroceryStore/MDUT
        https://github.com/jas502n/oracleShell
        https://github.com/RowTeam/SharpSQLTools
        https://github.com/0x727/SqlKnife_0x727
        https://github.com/quentinhardy/odat
        https://github.com/quentinhardy/msdat
    02 SQLServer攻击
        SQLServer攻击参考 -> https://github.com/safe6Sec/PentestDB，备份见 -> 07-内网服务攻击/01-数据库攻击/SQLServer攻击.md
        有一段时期，SQLServer下可通过SQLPS绕过杀软执行Powershell上线C2，现在应该不行了

# 0x02 命令执行
    01 优秀项目
        https://github.com/rootclay/WMIHACKER
```

# 08-内网钓鱼攻击
```
# 通达OA
CSS路径：D:\MYOA\webroot\static\theme\9\ipanel.css
JS路径：D:\MYOA\webroot\static\js\ba\agent.js

# 泛微OA
CSS路径：D:\WEAVER\ecology\cloudstore\dev\init.css
JS路径：D:\WEAVER\ecology\js\timeZone\timeZone.js

# 万户OA
CSS路径：d:\jboss\jboss-as\server\oa\deploy\defaultroot.war\scripts\desktop\popwin.css
JS路径：d:\jboss\jboss-as\server\oa\deploy\defaultroot.war\desktop.jsp
上面的JS是在JSP页面中插入<script>代码块，所以需要在</body>标签前面插入
```

# 09-域渗透
```
# 0x01 域渗透
    01 信息收集
        域环境下常规打法：上传bloodbound客户端搜集域内信息，把结果回传本地后，利用kali的bloodbound服务端解析，分析域内的薄弱环节
    02 LOLAD
        https://lolad-project.github.io/
```