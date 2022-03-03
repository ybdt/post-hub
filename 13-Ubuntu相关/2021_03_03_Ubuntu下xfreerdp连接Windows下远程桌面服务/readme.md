echo "">/home/user/.config/freerdp/known_hosts#用于解决连接同一防火墙不同端口时的密钥不匹配问题
xfreerdp /u:"user" /p:"pass" /v:10.0.100.248:3389 /size:1855x1010 +clipboard /drive:home,/home/user/桌面
