# 01-后门远控C2
```
# 后门远控C2
    0x01 参考链接
        https://www.vipshare.com/【WorkWin】
        https://www.netsupportmanager.com/zh-CN/【NetSupportManager】
        https://github.com/quasar/Quasar
        https://github.com/n1nj4sec/pupy
        https://github.com/Cr4sh/MicroBackdoor
        https://github.com/orangetw/tsh
        https://github.com/yuanyuanxiang/SimpleRemoter
        https://github.com/Cc28256/CcRemote
        https://github.com/rapid7/metasploit-framework
        https://github.com/BishopFox/sliver
        https://github.com/HavocFramework/Havoc
        https://github.com/HackerCalico/Magic_C2

    0x02 Windows权限维持
        1、启动文件夹
        2、注册表
        3、服务
        4、任务计划

    0x03 Linux权限维持
        1、修改/etc/shadow中密码
        2、写入ssh公钥
```

# 02-权限提升
```
# Windows下权限提升
    0x01 参考链接
        https://github.com/Ascotbe/Kernelhub
        https://github.com/SecWiki/windows-kernel-exploits
        https://forum.butian.net/share/860
        https://github.com/uknowsec/SweetPotato
        https://github.com/zcgonvh/DCOMPotato/tree/master
        https://forum.butian.net/share/860

# Linux下权限提升
    0x01 参考链接
        https://github.com/The-Z-Labs/linux-exploit-suggester
        https://github.com/jondonas/linux-exploit-suggester-2
        https://github.com/liamg/traitor
        https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS
        https://gtfobins.github.io/
    0x02 SUID提权
        原理很简单自行DeepSeek，具体做法是，执行如下命令寻找具有SUID位的可执行文件
        find / -perm -4000 -type f -exec ls -l {} \;
```

# 03-隧道搭建
```
# 隧道搭建
    0x01 参考链接
        https://github.com/CodeSecurityTeam/frp
        https://github.com/jpillora/chisel
        https://github.com/zema1/suo5
        https://github.com/L-codes/Neo-reGeorg
```

# 04-凭证窃取
```
# Windows下凭证窃取
    0x01 参考链接
        https://github.com/gentilkiwi/mimikatz
        https://github.com/StarfireLab/SharpWeb

# Linux下凭证窃取
    0x01 可以获取密文
        01、读取/etc/shadow后，使用cmd5进行解密：
            https://www.cmd5.com/
            注意，在cmd5中先识别类型，再进行解密
        02、若cmd5中不能解密，可尝试hashcat解密，使用如下网站识别加密类型：
            https://www.tunnelsup.com/hash-analyzer/
            https://hashcat.net/wiki/doku.php?id=example%20hashes
            爆破使用如下字典：
            https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
            最后执行如下命令：
            hashcat -m 3200 ./hash.txt ./rockyou.txt
    0x02 无法获取密文
        01、劫持ssh密码

# 软件凭据窃取
    https://github.com/AlessandroZ/LaZagne
```

# 05-主机敏感信息收集
```
# Windows下主机敏感信息收集
    0x01 参考链接
        https://github.com/aleenzz/InjectSQLServer【ASPX网站数据库密码加密存储】
        https://github.com/qwqdanchun/Pillager
        https://github.com/lintstar/SharpHunter
        https://github.com/GhostPack/Seatbelt

# Linux下主机敏感信息收集
```

# 06-内网探测扫描
```
https://github.com/shmilylty/netspy
https://github.com/shadow1ng/fscan
https://github.com/lcvvvv/kscan
nltest

通过webshell上传文件失败时，有时是因为文件过大，可尝试先分割，上传后再合并
md5sum f
split -b 3M --verbose f f_
cat f_aa f_ab f_ac > f
md5sum f
```

# 07-内网服务攻击
```
# 数据库攻击
    0x01 文章/工具
        https://github.com/SafeGroceryStore/MDUT
        https://github.com/jas502n/oracleShell
        https://github.com/RowTeam/SharpSQLTools
        https://github.com/0x727/SqlKnife_0x727
        https://github.com/quentinhardy/odat
        https://github.com/quentinhardy/msdat
    0x02 笔记
        SQLServer攻击参考 -> https://github.com/safe6Sec/PentestDB，备份见 -> 07-内网服务攻击/01-数据库攻击/SQLServer攻击.md
        有一段时期，SQLServer下可通过SQLPS绕过杀软执行Powershell上线C2，现在应该不行了

# 命令执行
    0x01 文章/工具
        https://github.com/rootclay/WMIHACKER
```

# 08-域渗透
```
# 域渗透
    0x01 笔记
        域环境下常规打法：上传bloodbound客户端搜集域内信息，把结果回传本地后，利用kali的bloodbound服务端解析，分析域内的薄弱环节
```

# 参考
```
https://github.com/safe6Sec/command
https://mp.weixin.qq.com/s/tqd9jJJv4bmzN6xVdpGDow
https://mp.weixin.qq.com/s/LK8zfWlz0s3v93sIY9DztQ【某师傅造的仿真环境，从GetShell到提权root】
```