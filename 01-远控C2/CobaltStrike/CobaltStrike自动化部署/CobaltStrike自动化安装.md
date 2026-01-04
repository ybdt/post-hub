发现自己经常需要在新环境下安装CobaltStrike，每次都手动安装效率有点低，故有此笔记

参考项目：https://github.com/AlphabugX/csOnvps

对项目中的自动化安装脚本进行解读，具体见文件run.sh

碰到4个坑：  
01 在一台已经安装jdk的vps上部署，部署后报错 Java: Error while loading shared libraries: libjli.so 解决办法是将vps重置后重新部署  
02 在全新的vps上部署，停止cobaltstrike后，执行 java -version 提示找不到java，执行 keytool 提示找不到keytool  
03 再次重置vps，部署后提示找不到teamserver，排查后发现apt install unrar失败，导致没能成功解压压缩包，手动安装unrar  
04 客户端连不上服务端，经测试，关闭socks5代理后，可成功连接  