```
netsh interface portproxy show v4tov4
netsh interface portproxy delete v4tov4 listenport=4444 listenaddress=192.168.1.142
netsh interface portproxy add v4tov4 listenport=4444 connectaddress=192.168.202.129 connectport=4444 listenaddress=192.168.0.142
```