gpg（也叫gnupg）源于openpgp，openpgp是在1997年由开发pgp的那位牛逼的人提交给IETF由此开源的，而pgp1991年发布的商业软件  

基于非对称加密算法，特点为公钥加密的信息，只能用私钥解密，即使是公钥也不能解密，反之同理，所以，如果能用公钥解密的话，就一定是用对应的私钥加密的，也就能证明是所有者发布的，但由于很耗费计算资源，故通常的用法为，先对目标信息进行hash运算，再对保存hash运算结果的文件进行签名，当然也可以直接对文件进行签名  

那公钥去哪找呢？于是诞生了公钥服务器，从公钥服务器检索公钥，进行验证，就OK了，就这么简单，涉及到的常用命令如下  
ubuntu16.04 server下校验debian：  
gpg2 --list-keys  
gpg2 --recv-keys 0x12345678 或者 gpg --import subversion.asc  
gpg2 --verify ./SHA256SUMS.gpg ./SHA256SUMS  
参考链接：  
https://blog.lancitou.net/pgp-tutorial/  
https://snowolf.iteye.com/blog/1879836  

参照debian官方的校验部分  
“我如何校验我的下载是debian官方创建的，且是真实的authentic（没被篡改）和准确的（没有损坏的）？”  
这里有SHA1SUMS，SHA256SUMS，等文件，它们包含着镜像的校验值。这些校验值也是被签名的，如SHA1SUMS.sign，SHA256SUMS.sign，等等。  
一旦你已经下载了一个镜像，你可以：  
检查镜像的校验值是否匹配校验值文件  
检查校验值文件是否被篡改过  

总结：  
检查校验值是为了防止一些问题或攻击，（如下载中损坏，会导致校验值不匹配，或者在路由器中转时被替换）  
检查校验文件签名是为了防止一些攻击（如dns劫持，会导致校验值匹配，但是签名会不匹配）  

校验过程中，将SHA256SUMS和SHA256SUMS.gpg文件中的内容拷贝粘贴是不行的，会校验失败，必须通过迅雷下载下来  

gnupg1和gnupg2的区别  
简而言之：  
gnupg1：主要用于服务器（中的其他程序）和嵌入式设备，体积小  
gnupg2：主要用于桌面和命令行，带有其他模块  
该安装并使用哪个？  
两个都安装，一般用gpg2去验证即可  
参考链接：  
https://superuser.com/questions/655246/are-gnupg-1-and-gnupg-2-compatible-with-each-other  

当进行gpg验证的时候，如何确定gpg公钥是真的？  
gpg验证最大的薄弱环节就是，公钥被伪造，所以验证的方式就是对照公钥ID，可以通过直接向公钥的提供者当面或者电话验证指纹，从而确定公钥的真实性问题。  
如果不能直接验证的话，只能通过其他侧面的方式验证，拿debian举例  
首次验证时，会提示没有ID为12345678的公钥  
然后官网一般也会有显示公钥ID为12345678（https://www.debian.org/CD/verify）  
从第三方的gpg检验文章中（https://linuxconfig.org/how-to-verify-an-authenticity-of-downloaded-debian-iso-images），也会发现一个  
公钥ID为12345678  
如上3个如果都一致的话，那便几乎没有问题，其实更好的方式还是来自于长年累月你对他公钥ID的熟悉  
另外  
一般官网指定的gpg密钥或者密钥ID比较可信  
参考连接：  
https://jin-yang.github.io/post/security-pgp-introduce.html  
https://serverfault.com/questions/569911/how-to-verify-an-imported-gpg-key  

下载的iso如果有公钥服务器的话，用指定的公钥服务器来下载公钥，否则用默认的公钥服务器下载  
如ubuntu，debian指定了公钥服务器，parrot则没有指定公钥服务器  

主流的公钥服务器有哪些？  
sks公钥池，等等  
参考链接：  
https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving  

gpg官网推荐使用的公钥服务器为pool.sks-keyservers.net（即sks公钥池）  
参考链接：  
https://www.gnupg.org/faq/gnupg-faq.html#new_user_default_keyserver  

gpg默认的keyserver为keys.gnupg.net，即sks公钥池（https://sks-keyservers.net/）的别名  
参考链接：  
https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving  
https://blog.lancitou.net/pgp-tutorial/  
