svn基础知识学习  
参考链接：  
https://www.runoob.com/svn/svn-tutorial.html  
https://subversion.apache.org/  
https://www.visualsvn.com/  
https://tortoisesvn.net/  
https://www.zhihu.com/question/19930022/answer/24180458  

校验下载的源代码文件：  
gpg –import ./xxx.asc  
gpg –verify ./xxx.asc xxx.tar.bz2  
通常从官网下载的公钥或者使用官网指定的公钥ID下载的公钥，基本没有问题  
参考链接:  
https://subversion.apache.org/download.cgi#verifying  
https://github.com/xuxuedong/YBDTBlog_Ops/blob/master/gpg%E5%AD%A6%E4%B9%A0  

centos7下编译安装apache subversion server:  
参照如下链接：  
https://www.cnblogs.com/jkko123/p/6358461.html  
https://www.cnblogs.com/zhoulf/p/4305042.html  
./configure –prefix=/home/svn-1.12.0  
报错找不到apr  

以为缺少g++，yum install g++失败，通过如下博客  
https://blog.csdn.net/dream_1996/article/details/69397089  
得知，centos下安装g++的包名为gcc-g++  
yum install gcc-g++后，编译安装仍旧失败  

参照如下链接：  
https://www.cnblogs.com/jkko123/p/6358461.html  
需要依赖项apr,apr-util,zlib,serf,openssl，本打算yum安装这些包  
可是yum安装了这些包（除了serf）后，再次./configure –prefix=/home/svn-1.12.0时仍旧提示找不到apr  

查找包被安装到的路径  
rpm –qa | grep “apr” # 查询包含指定名的所有包  
rpm –ql xxx.xxx # 列出包中的文件  
参考链接：  
https://blog.csdn.net/hooloo/article/details/55667666  

手动指定apr的路径，进行编译  
./configure –prefix=/home/svn-1.12.0 –apr-with=xxx后仍旧报错，提示：找不到apr的配置，还是要进行编译安装  

从官网下载apr,apr-util,scons,serf  

编译apr  
./configure --prefix=/data/apr  
make  
make install  

编译apr-util  
./configure --prefix=/data/apr-util --with-apr=/data/apr  
make  
报错“xml/apr_xml.c:35:19: fatal error: expat.h: No such file or directory”  
参照如下博客：  
https://blog.csdn.net/hanzheng260561728/article/details/79655043  
提示缺少expat-devel库  
yum install expat-devel后  
make  
make install  
成功  

编译安装scons  
python setup.py install --prefix=/data/scons  
make  
make install  

编译安装serf  
/data/scons/bin/scons PREFIX=/data/serf APR=/data/apr APU=/data/apr-util  
/data/scons/bin/scons install  
cp /data/serf/lib/libserf-1.so* /usr/local/lib/  

下载，解压，并重命名为sqlite–amalgamation,移动到编译的目录下  

编译subversion  
./configure --prefix=/home/svn-1.12.0 --with-apr=/data/apr --with-apr-util=/data/apr-util --with-serf=/data/serf --enable-mod-activation --with-lz4=internal --with-utf8proc=internal  
期间碰到3处报错  
第1处报错，控制台给出解决方案，添加选项--with-lz4=internal解决  
第2处报错，参照如下链接：  
https://blog.csdn.net/qq_27868061/article/details/81094187  
添加选项--with-utf8proc=internal解决  
第3处报错，参照如下链接：  
http://mail-index.netbsd.org/pkgsrc-users/2019/04/23/msg028353.html  
http://subversion.1072662.n5.nabble.com/configure-error-failed-to-recognize-APR-INT64-T-FMT-on-this-platform-td204212.html  
需要改变apr1.7为apr1.6，重新编译apr，解决  
make  
make install  

配置svn server:  
执行svn时会报错  
svn: error while loading shared libraries: libserf-1.so.1: cannot open shared object file: No such file or director  
参照如下连接：  
https://www.cnblogs.com/jkko123/p/6358461.html  
cd /etc/ld.so.conf.d/  
vi user-libs.conf  
把我们拷贝serf的文件的目录加上  
/usr/local/lib  
ldconfig  
仍旧报错  
ldconfig: /usr/local/lib/libserf-1.so.1 is not a symbolic link  
检查发现  
cp /data/serf/lib/libserf-1.so* /usr/local/lib/  
会把正常文件和符号链接文件都拷贝为正常文件，将libserf-1.so.1改为符号链接文件，再执行  
ldconfig  
没有报错  
（ldconfig基本解释：更新缓存，缓存是寻找动态链接库文件的缓存，一般用于新安装了.so文件）  

其他依照文章配置即可，仓库目录我指定为/home/repos  

添加到/etc/rc.d/rc.local中实现开机自启，失败，参照如下链接：  
https://blog.csdn.net/lilovfly/article/details/76400731  
得知，此文件没有执行权限，添加执行执行权限，实现开机自启  

svn迁移从windows下的VisualSVN到linux下的subversion:  
参照如下链接：  
https://blog.csdn.net/tzhuwb/article/details/77757559  
http://coolnull.com/1413.html  
从windows下的svn中导出仓库，链接的文中有些问题，使用如下指令：  
svnadmin dump D:\Repositories\javashop_ru>javashop_ru.dump  
在linux端创建相同名称的仓库  
svnadmin create /home/repos/javashop_ru  
导入仓库  
svnadmin load javashop_ru<javashop_ru.dump  
然后修改用户访问权限以及用户名密码  
将其中一个仓库的authz和passwd文件拷贝到根目录下  
修改authz文件，添加如下内容:  
[/]  
user = rw  
修改passwd文件，添加如下内容：  
user = 123  
最后在访问上卡了我挺长时间。。。  
linux下多个仓库的访问需要地址指定每一个仓库名，直接指定地址根目录会报错“没有仓库被发现”  
svn://192.168.1.128:3690/这样是不行的  
需要svn://192.168.1.128:3690/DocumentRoot这样  
