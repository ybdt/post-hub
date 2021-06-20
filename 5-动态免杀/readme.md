# 结论

## 其他思路记录
1、Mimikatz还可以尝试分离免杀，参考：  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypassAV  
https://github.com/lengjibo/RedTeamTools/tree/master/windows/mimikatz_bypass  
2、调用其他API实现lsass的内存dump，参考：  
https://lengjibo.github.io/nod32-bypass/#more  
3、添加用户还可以尝试反射型dll注入，参考：  
https://github.com/lengjibo/NetUser/blob/master/rdi_net_user.cpp

## 2021/06/20测试总结
2021_06_19_CS内存中执行mimikatz过杀软提取密码 —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Mimikatz源码免杀                  —— 能过360安全卫士（此时的最新版v13）、不能过火绒（此时的最新版v5.0.61.1）  
2021_06_19_Procdump+Mimikatz过杀软提取密码   —— 不能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）  
2021_06_20_过杀软添加用户                    —— 能过360安全卫士（此时的最新版v13）、能过火绒（此时的最新版v5.0.61.1）
