找到/root/Desktop/tor-browser_en-US/Browser/start-tor-browser  
搜索root，注释掉如下内容
```
#if [ "`id -u`" -eq 0 ]; then
#	complain "The Tor Browser Bundle should not be run as root.  Exiting."
#	exit 1
#fi
```
保存后，即可正常运行
