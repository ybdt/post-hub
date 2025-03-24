# 01、后门远控C2
```
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

Windows下权限维持
1、启动文件夹
2、注册表
3、服务
4、任务计划

Linux下权限维持
1、修改/etc/shadow中密码
2、写入ssh公钥
```

# 02、权限提升
```
Windows下权限提升
https://github.com/Ascotbe/Kernelhub
https://github.com/SecWiki/windows-kernel-exploits
https://forum.butian.net/share/860
https://github.com/uknowsec/SweetPotato

Linux下权限提升
https://github.com/The-Z-Labs/linux-exploit-suggester
https://github.com/jondonas/linux-exploit-suggester-2
https://github.com/liamg/traitor
https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS
https://gtfobins.github.io/
```

# 03、隧道搭建
```
https://github.com/CodeSecurityTeam/frp
https://github.com/jpillora/chisel
https://github.com/zema1/suo5
https://github.com/L-codes/Neo-reGeorg
```

# 04、凭据窃取
```
Linux下凭据窃取
1、读取/etc/shadow后，去cmd5解密，在cmd5中先识别类型，再尝试解密
```

# 05、主机敏感信息收集
```
https://github.com/aleenzz/InjectSQLServer【ASPX网站数据库密码加密存储】
https://github.com/GhostPack/Seatbelt
https://github.com/lintstar/SharpHunter
https://github.com/qwqdanchun/Pillager
```

# 06、内网探测扫描
```
https://github.com/shmilylty/netspy
https://github.com/shadow1ng/fscan
nltest

通过webshell上传文件失败时，有时是因为文件过大，可尝试先分割，上传后再合并
md5sum f
split -b 3M --verbose f f_
cat f_aa f_ab f_ac > f
md5sum f
```

# 07、内网漏洞利用
```
【免杀的横向移动命令执行】https://github.com/rootclay/WMIHACKER
```

# 08、域渗透
域环境下常规打法：上传bloodbound客户端搜集域内信息，把结果回传本地后，利用kali的bloodbound服务端解析，分析域内的薄弱环节

# 参考
```
https://github.com/safe6Sec/command
https://mp.weixin.qq.com/s/tqd9jJJv4bmzN6xVdpGDow
```