有时作者并未发布最新版编译后的二进制，需要自己编译
```
查看当前 GOOS 环境变量
set GOOS

设置编译后运行的操作系统
set GOOS=linux
设置编译后运行的操作系统架构
set GOARCH=amd64
设置禁用CGO
set CGO_ENABLED=0

go build -ldflags="-s -w " -trimpath
```

参考链接  
[https://blog.frytea.com/archives/607/](https://blog.frytea.com/archives/607/)  
[https://www.zhangbj.com/p/657.html](https://www.zhangbj.com/p/657.html)  