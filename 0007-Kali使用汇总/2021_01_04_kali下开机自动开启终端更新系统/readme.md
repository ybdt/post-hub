先放结论：  
gnome-terminal -e 'bash -c "apt -y update && apt -y upgrade && apt -y autoremove && sleep 5"'

之前考虑的都是.bashrc、注册成服务什么的，后来发现不行，需要通过桌面启动终端才行
