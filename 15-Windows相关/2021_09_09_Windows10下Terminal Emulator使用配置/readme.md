### 使用Cmder
1、修改命令提示符
```
打开文件\vendor\clink.lua，定位到51行，将"λ"修改为"$"
```
2、修改启动路径
```
Settings->Startup->Tasks，选择对应的Task，修改右边的值为：
*cmd /k ""%ConEmuDir%\..\init.bat" -new_console:d:C:\Users\ybdt\Desktop"
```
### 2021/09/09 改用ConEmu
ConEmu更酷，改用ConEmu  
配置同上
