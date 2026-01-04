# 指定磁盘下搜索特定名称的文件
```
dir D:\ /S /B | find "orange1.jsp"
/S          显示指定目录和所有子目录中的文件。
/B          使用空格式(没有标题信息或摘要)。
```

# 全盘搜索特定名称的文件

```
cmd /v:off /Q /c "for /f %i in (^'wmic logicaldisk get caption ^| findstr ":"^') do dir %i\ /b /s 2>nul | findstr "ToDesk_Lite.exe""
```



# 查看历史命令

```
cmd下：doskey /history
powershell下：Get-History
```