默认情况下mRemoteNG加密后的密码保存在C:\Users\username\AppData\Roaming\mRemoteNG\confCons.xml  

密码通过AES-GCM加密，默认密钥为：mR3m  

经测试，使用在线解密工具无法解密，故编写此工具：mRemoteNG_decrypt.py，工具会将结果输出到csv文件，如下图

（经测试，版本2.6可以，2.7不行，版本信息可从配置文件中看到）  

如下图
![image](./pic/mRemoteNG.png)  

参考链接：  
https://exexute.github.io/2019/05/08/HTB-windows-Bastion/  
https://github.com/kmahyyg/mremoteng-decrypt  
