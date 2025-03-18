以frp 0.61.1为例

frps.toml
```
[common]
bind_addr = 0.0.0.0
bind_port = 7000
dashboard_port = 7500
dashboard_user = 123456
dashboard_pwd = 123456
```

frpc.toml
```
[common]
server_addr = ip_of_vps
server_port = 7000

[http_proxy]
type = tcp
remote_port = 6000
plugin = http_proxy

[socks5_proxy]
type = tcp
remote_port = 6005
plugin = socks5
```

浏览器配置代理，http://ip_of_vps:6000，Edge浏览器下F12 -> 网络 -> 随便选一个请求 -> 在标头中可以看到远程地址为代理服务器地址