默认情况下：加密后的密码保存在C:\Users\username\AppData\Roaming\mRemoteNG\confCons.xml  

密码通过AES中的GCM模式加密，默认密钥为：mR3m  

经测试，通过在线AES解密工具选择GCM模式也无法解密，可使用mRemoteNG_decrypt.py解密  

如下图  
![image](./pic/mRemoteNG.png)  

参考链接：  
https://exexute.github.io/2019/05/08/HTB-windows-Bastion/  
https://github.com/kmahyyg/mremoteng-decrypt  
