## CobaltStrike、Metasploit静态免杀思路
### 1、loader + shellcode
1.1、c语言实现的loader  
1.2、go语言实现的loader  
1.3、loader变形  
```
异或加密
睡眠函数，C语言睡眠函数：Sleep(1000)
base64编码
gzip压缩
```
1.4、（多篇文章提到）生成64位的shellcode比32位shellcode免杀效果更好一些

## 待尝试思路记录：
DNS分离免杀：https://mp.weixin.qq.com/s/bM_rsh8KxXwwyEkbHRTKsw  

狼组团队：https://github.com/wgpsec/CS-Avoid-killing  
https://mp.weixin.qq.com/s/G1hmsDVTO2208Ymlia_ggQ  
https://github.com/An0ny-m0us/DesertFox  
知道创宇公司：https://github.com/knownsec/shellcodeloader  

Kill杀软：https://github.com/Yaxser/Backstab + https://github.com/secretsquirrel/SigThief

## 待尝试思路记录
1、Mimikatz还可以尝试分离免杀，参考：  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypassAV  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypass  
2、调用其他API或使用procdump替代工具（如SqlDumper、SharpDump）dump进程lsass的内存，参考：  
https://lengjibo.github.io/nod32-bypass/#more  
https://uknowsec.cn/posts/notes/Mimikatz%E6%98%8E%E6%96%87%E5%AF%86%E7%A0%81%E6%8A%93%E5%8F%96.html  
3、添加用户还可以尝试反射型dll注入，参考：  
https://github.com/lengjibo/NetUser/blob/master/rdi_net_user.cpp  
https://github.com/bats3c/DarkLoadLibrary/tree/master/DarkLoadLibrary  
4、对于不能直接提取密码的windows server，可在添加用户后尝试RDP会话劫持实现未授权登录，参考：  
https://mp.weixin.qq.com/s/GXvz4jXc8IPVQcXkB6L6_w  
5、借助darkarmour，可参考：  
https://www.cnblogs.com/cwkiller/p/14111601.html

## 2021/06/20测试总结
2021_06_19_CS内存中执行mimikatz过杀软提取密码 —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Mimikatz源码免杀                  —— 能过360安全卫士（此时的最新版v13）、不能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Procdump+Mimikatz过杀软提取密码   —— 不能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_20_过杀软添加用户                    —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）

## 待尝试思路记录
1、免杀shellcode并绕过杀毒添加自启动  
https://wtfsec.org/posts/%E5%85%8D%E6%9D%80shellcode%E5%B9%B6%E7%BB%95%E8%BF%87%E6%9D%80%E6%AF%92%E6%B7%BB%E5%8A%A0%E8%87%AA%E5%90%AF%E5%8A%A8/  
2、Monitor持久化  
https://mp.weixin.qq.com/s/ubNB9FAp3h2r7PqGUC9e0g  
3、foxmail中设置开机自启，杀软没有任何提示，研究foxmail开机自启方式，尝试foxmail白利用的方式实现开机自启  
4、QQ音乐的默认安装中会勾选开机自启动，且不会被杀软查杀，可尝试模仿QQ音乐的开机自启方式
