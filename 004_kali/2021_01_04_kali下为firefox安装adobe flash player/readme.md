事情起源于参加360众测考试，打算使用kali系统作为攻击机，结果访问考试环境时死活找不到“进入”按钮，排查了一圈，怀疑可能是因为没安装adobe flash player，故有此文

adobe官网下载flash player，我下载的版本是flash_player_npapi_linux.x86_64.tar.gz  
mkdir ./tmp  
unzip ./flash_player_npapi_linux.x86_64.tar.gz -d ./tmp  
cd ./tmp  
cp ./libflashplayer.so /usr/lib/mozilla/plugins/  
sudo cp -r ./usr/* /usr/

访问www.jlplib.com.cn  
能够成功访问flash部分

参考链接：  
https://null-byte.wonderhowto.com/how-to/install-flash-kali-linux-2-0-rolling-0171211/
