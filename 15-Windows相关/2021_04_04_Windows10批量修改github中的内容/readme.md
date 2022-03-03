由于要大量修改github.com中的内容，故寻找高效的批量方式

#### 1、下载GitHub Desktop
#### 2、如果不能clone仓库的话，需要为GitHub Desktop配置代理
```
#在c:\users\ybdt\.gitconfig中添加如下部分：
[http]
    proxy = socks5://127.0.0.1:1080
[https]
    proxy = socks5://127.0.0.1:1080
[git]
    proxy = socks5://127.0.0.1:1080
```
#### 3、如果github.com仓库的文件名中出现Windows下文件名中不能出现的字符，则会提示“check error”，需要修改仓库中的文件名
#### 4、clone到本地后，到指定文件夹C:\Users\ybdt\Documents\GitHub\web-hub下修改对应内容，然后GitHub Desktop中会提示修改的内容
#### 5、在summary中输入内容（这是被要求的字段）
#### 6、最后点击Push Origin
#### 7、如果要使用新的仓库，点击File->Clone Repository

参考链接：  
https://kassadin.moe/2019/07/17/003-how-to-set-proxy-for-Github-desktop/
