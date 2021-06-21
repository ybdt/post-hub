## 待尝试思路记录
1、Mimikatz还可以尝试分离免杀，参考：  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypassAV  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypass  
2、调用其他API或使用procdump替代工具（如SqlDumper、SharpDump）dump进程lsass的内存，参考：  
https://lengjibo.github.io/nod32-bypass/#more  
https://uknowsec.cn/posts/notes/Mimikatz%E6%98%8E%E6%96%87%E5%AF%86%E7%A0%81%E6%8A%93%E5%8F%96.html  
3、添加用户还可以尝试反射型dll注入，参考：  
https://github.com/lengjibo/NetUser/blob/master/rdi_net_user.cpp  
4、对于不能直接提取密码的windows server，可在添加用户后尝试RDP会话劫持实现未授权登录，参考：  
https://mp.weixin.qq.com/s/GXvz4jXc8IPVQcXkB6L6_w  
5、借助darkarmour，可参考：  
https://www.cnblogs.com/cwkiller/p/14111601.html

## 2021/06/20测试总结
2021_06_19_CS内存中执行mimikatz过杀软提取密码 —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Mimikatz源码免杀                  —— 能过360安全卫士（此时的最新版v13）、不能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Procdump+Mimikatz过杀软提取密码   —— 不能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_20_过杀软添加用户                    —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）
