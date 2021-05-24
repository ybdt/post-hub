0、设置执行sudo时不用输入密码
su - root
chmod u+w /etc/sudoers
将对应行改为：%sudo ALL=(ALL:ALL) NOPASSWD:ALL
chmod u-w /etc/sudoers

1、更改源为阿里源（https://developer.aliyun.com/mirror/）
sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vim /etc/apt/sources.list

2、通过设置，让kali系统不自动锁屏、休眠

3、安装chrome（https://www.google.com/intl/zh-CN/chrome/）
dpkg -i ./google-chrome-stable_current_amd64.deb
3.1、chrome在root下不能启动
vim /opt/google/chrome/google-chrome
最后一行改为：exec -a "$0" "$HERE/chrome" "$@" --no-sandbox
3.2、安装SwitchyOmega
命令行执行：google-chrome --proxy-server="http://127.0.0.1:8080"
到chrome商店中搜索SwitchyOmega并安装
3.3、如何关闭chrome提示的keyring？
右键点击桌面的chrome launcher，在Command中添加选项“--password-store=basic”
最终选项为“/usr/bin/google-chrome-stable %U --password-store=basic”

4、宿主机到虚拟机的复制粘贴有时会失效，故创建共享文件夹
通过vmware设置共享目录
sudo apt install open-vm-tools-desktop fuse
vmware-hgfsclient查看一下
sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/ -o subtype=vmhgfs-fuse,allow_other,nonempty（不加nonempty，会在每次启动终端时提示几行字符）
将“sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/ -o subtype=vmhgfs-fuse,allow_other”添加到~/.zshrc（注意最新版是ZSH）

5、终端中的字体非常小，太累眼睛
Settings（设置）->Appearance（外观）->Fonts（字体）->DPI改为150

6、安装中文输入法
sudo apt install fcitx fcitx-googlepinyin
打开Fcitx Configuration -> 点击坐下加“+” -> 取消勾选仅选择“only show current language” -> 添加中文

7、firefox登录账户来同步浏览器工具
删除书签工具栏多余的书签，遵照之前的火狐定制配置，删除多余组件，调整新装组件的顺序

8、工具迁移
创建文件夹kali-tool-backup-2021_01_26-32_item，再将要拷贝的文件及文件夹放到创建的文件夹中，最后tar -zcvf ./kali-tool-backup-2021_01_26-32_item.tar.gz ./kali-tool-backup-2021_01_26-32_item/
burp需要进行首次配置参考：https://github.com/ybdt/pentest-hub/blob/main/2021_01_26_burpsuite%E6%BF%80%E6%B4%BB%E9%85%8D%E7%BD%AE%E6%B5%81%E7%A8%8B/readme.md
创建burp启动器，添加以下4项即可
Name:
Command:
Working Directory:
Icon:（从Images Files中选择图像）
其他启动器照此创建

9、重新安装AWVS
参照：https://github.com/ybdt/pentest-hub/blob/main/2021_01_26_AWVS%E7%A0%B4%E8%A7%A3%E7%89%88%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97/readme.md
桌面创建一个URL发射器
