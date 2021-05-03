如题，不能选择内容，然后每次粘贴的话，都会粘贴一行

经排查，当关闭输入法ibus时，vscode下可以选择内容（无语。。。）

卸载ibus输入法：  
apt purge ibus  
apt autoremove

安装fcitx输入法框架和谷歌拼音输入法：  
apt install fcitx fcitx-googlepinyin im-config  
执行im-config  
确定后选择fcitx  
重启后，新输入法生效

参考链接：  
https://blog.csdn.net/SouthWind0/article/details/80561184
