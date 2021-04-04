华为nova2下安装google play store失败  
从http://www.apkmirror.com/中下载termux  
通过数据线传到手机上并安装  

进入termux后执行如下指令：  
pkg install curl  
curl -OL https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh  
chmod +x metasploit.sh  
ls -alh  
./metasploit.sh  
After few minutes it will ask “Do you want to continue? [y/n] → Press y  

但是执行完报错如下：  
[*] Metasploit requires the Bundler gem to be installed  
    $ gem install bundler  

解决方式是执行如下指令：  
gem install bundler  
bundle install  

还是报错如下：  
缺少Gemfile.local（好像是，记不清了）  

解决方式是执行如下指令：  
apt update  
apt -y upgrade  
apt -y install git ruby ruby-dev make clang autoconf curl wget ncurses-utils libsqlite-dev postgresql postgresql-dev libpcap-dev libffi-dev libxslt-dev pkg-config  
git clone -b termux https://github.com/timwr/metasploit-framework.git  
cd metasploit-framework  
gem install bundler  
gem install nokogiri -- --using-system-libraries  
bundle install --gemfile Gemfile.local  
./msfconsole  

还是报错如下：  
can't find gem bundler ( >= 0.a) with executable bundle  

解决方式是执行如下指令：  
gem install bundler -v 1.15.1  

参考链接：  
https://techglimpse.com/metasploit-error-gem-bundler-solution/  
https://lucideustech.blogspot.com/2018/02/attacking-windows-platform-with.html?m=1  
https://github.com/rapid7/metasploit-framework/issues/8765  
https://stackoverflow.com/questions/47026174/find-spec-for-exe-cant-find-gem-bundler-0-a-gemgemnotfoundexception
