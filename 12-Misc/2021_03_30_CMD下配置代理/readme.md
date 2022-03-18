#### 使用SOCKS5代理，升级pip时会报错，使用HTTP代理，升级pip时则不会报错

使用HTTP代理
```
set http_proxy=http://127.0.0.1:8080
set https_proxy=http://127.0.0.1:8080
```

使用SOCKS5代理
```
set http_proxy=socks5://127.0.0.1:1080
set https_proxy=socks5://127.0.0.1:1080
```
