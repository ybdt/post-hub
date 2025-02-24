#!/bin/bash
# By Alphabug
# Github https://github.com/AlphabugX/csOnvps


# 初始配置
mkdir Alphabug_CS
cd Alphabug_CS
Alphabug_CS_PATH=`pwd`
K8_CS_FILE=$Alphabug_CS_PATH/"K8_CS_4.4_20211109.rar"
JDK_FILE=$Alphabug_CS_PATH/"jdk-8u202-linux-x64.tar.gz"


# 生成随机数
function radom_key(){
    KEY=`uuid | md5sum |awk -F' ' '{ print $1}'`
    echo $KEY
}


# 更新系统并安装需要的工具
sudo apt update && sudo apt install unrar uuid dos2unix -y


# 下载JDK
function download_jdk {
    if [ -f "$K8_CS_FILE" ];then
        K8_CS_MD5="913d774e5cf0bfad4adfa900997f7a1a"
        K8_CS_MD5_test=`md5sum $K8_CS_FILE | awk -F" " '{print $1}'`
        if [ $K8_CS_MD5 != $K8_CS_MD5_test];then
            K8_CS_FILE="NO"
            rm -rf $K8_CS_FILE
        fi
    else
        K8_CS_FILE="YES"
    fi

    if ((`curl https://objects.githubusercontent.com --connect-timeout 5 -m 5 -s | wc -l` > 10)) ; then
        echo "[+] Welcome to Github Script..."
        wget -L https://github.com/AlphabugX/csOnvps/releases/download/jdk-8u202-linux-x64/jdk-8u202-linux-x64.tar.gz
        if [ $K8_CS_FILE == "YES" ];then
            wget -c https://github.com/k8gege/Aggressor/releases/download/cs/K8_CS_4.4_20211109.rar
            unrar x K8_CS_4.4_20211109.rar -pk8gege.org
        fi
        wget -L https://raw.githubusercontent.com/AlphabugX/csOnvps/main/teamserver
    else
        echo "[+] Welcome to Gitee Script..."
        wget -L https://gitee.com/Alphabug/csOnvps/attach_files/900306/download/jdk-8u202-linux-x64.tar.gz_part_aa
        wget -L https://gitee.com/Alphabug/csOnvps/attach_files/900305/download/jdk-8u202-linux-x64.tar.gz_part_ab
        if [ $K8_CS_FILE == "YES" ];then
            wget -c https://github.com/k8gege/Aggressor/releases/download/cs/K8_CS_4.4_20211109.rar
            unrar x K8_CS_4.4_20211109.rar -pk8gege.org
        fi
        cat jdk-8u202-linux-x64.tar.gz_part_* > $JDK_FILE
        rm -rf jdk-8u202-linux-x64.tar.gz_part_*
        wget -L https://gitee.com/Alphabug/csOnvps/raw/master/teamserver
    fi
}


# 配置JDK
JDK_FLAG="YES"
if [ `echo $(java -version 2>&1) | awk -F" " '{print $1$3}' | tr -d '"'` != "java1.8.0_202" ];then
    if [ -f "$JDK_FILE" ]; then
        JDK_MD5="0029351f7a946f6c05b582100c7d45b7"
        JDK_MD5_test=`md5sum  $JDK_FILE | awk -F" " '{print $1}'`
        if [ $JDK_MD5 != $JDK_MD5_test] ;then
            rm -rf  $JDK_FILE
            download_jdk;
        fi
    else
        download_jdk
    fi
    tar xf  $JDK_FILE
    JDK_PATH=$Alphabug_CS_PATH/jdk1.8.0_202/
    update-alternatives --install /usr/bin/java java $JDK_PATH/bin/java 180202
    update-alternatives --set java $JDK_PATH/bin/java
    update-alternatives --install /usr/bin/keytool keytool $JDK_PATH/bin/keytool 180202
    update-alternatives --set keytool $JDK_PATH/bin/keytool
    JDK_FLAG="NO"
fi
# ln -s $Alphabug_CS_PATH/jdk1.8.0_202/bin/* /usr/bin/


# 修改K8 CS的默认配置
IP=`curl ip.0xc2.cn`
PASSWORD=`radom_key`
KEYPASS=`radom_key`
dos2unix $Alphabug_CS_PATH/teamserver
cp  $Alphabug_CS_PATH/teamserver  $Alphabug_CS_PATH/K8_CS_4.4/
chmod 777 $Alphabug_CS_PATH/K8_CS_4.4/*
cd $Alphabug_CS_PATH/K8_CS_4.4/


# 获得随机端口
PORT=0
# 判断当前端口是否被占用，没被占用返回0，反之1
function Listening {
   TCPListeningnum=`netstat -an | grep ":$1 " | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
   UDPListeningnum=`netstat -an | grep ":$1 " | awk '$1 == "udp" && $NF == "0.0.0.0:*" {print $0}' | wc -l`
   (( Listeningnum = TCPListeningnum + UDPListeningnum ))
   if [ $Listeningnum == 0 ]; then
       echo "0"
   else
       echo "1"
   fi
}
function get_random_port {
   templ=0
   while [ $PORT == 0 ]; do
       temp1=`shuf -i $1-$2 -n1`
       if [ `Listening $temp1` == 0 ] ; then
              PORT=$temp1
       fi
   done
}
get_random_port 10000 65534;


# 配置Teamserver
sed -i "s/SET_TEAMSERVER_PORT/$PORT/g" teamserver
sed -i "s/SET_TEAMSERVER_KEY/$KEYPASS/g" teamserver
install_log="$Alphabug_CS_PATH/install.log"
echo "[+] Teamserver IP:" $IP >> $install_log
echo "[+] Teamserver Port:" $PORT >> $install_log
echo "[+] Teamserver Password:" $PASSWORD >> $install_log
echo "[+] Teamserver keyStorePassword:" $KEYPASS >> $install_log
nohup $Alphabug_CS_PATH/K8_CS_4.4/teamserver $IP $PASSWORD &
PID=`sudo ps -ef | grep $PASSWORD |awk -F" " '{ print $2 }' |tr "\n" " "` >> $install_log
echo "[+] Teamserver PID: "$PID >> $install_log
echo "[*] Teamserver Stop Command: kill -KILL "$PID >> $install_log
if [ $JDK_FLAG == "NO" ];then
    echo "[!] Remove Sun JDK Command: update-alternatives --remove java $JDK_PATH/bin/java"  >> $install_log
fi
# echo "[!] Remove Sun JDK Command:"  >> $install_log
# echo Zm9yIGl0ZW0gaW4gYGxzIC1sc2EgL3Vzci9iaW4vIHxncmVwIGpkayB8YXdrIC1GIiAiICd7IHByaW50ICQxMH0nYDsgZG8gZWNobyAiRGVsIC91c3IvYmluLyIkaXRlbTtybSAtcmYgIi91c3IvYmluLyIkaXRlbTtkb25lCg== | base64 -d >> $install_log
echo "[!] Remove Alphabug_CS Command: rm -rf "$Alphabug_CS_PATH  >> $install_log
cat $install_log
if [ ! -d "$Alphabug_CS_PATH/log" ]; then
    mkdir $Alphabug_CS_PATH/log
fi
mv $install_log $Alphabug_CS_PATH/log/`date +%Y%m%d_%H%M%S.log`


# 创建卸载脚本
uninstall=$Alphabug_CS_PATH/uninstall.sh
echo "kill -KILL "$PID >> $uninstall
if [ $JDK_FLAG == "NO" ];then 
    echo "update-alternatives --remove java $JDK_PATH/bin/java" >> $uninstall
fi
echo "rm -rf "$Alphabug_CS_PATH  >>$uninstall
chmod +x $uninstall
echo "[+] Install_Log Saved to file:" $install_log
echo "[+] uninstall.sh Saved to file:" $uninstall