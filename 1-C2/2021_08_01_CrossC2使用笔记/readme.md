CrossC2使用版本v3.0.1-dev

# 1、不使用profile：
1.下载CrossC2-GithubBot-2021-09-13.cna、CrossC2Kit-GithubBot-2021-09-13.zip、genCrossC2.Linux  

2.将CrossC2Kit-GithubBot-2021-09-13.zip内的文件夹CrossC2Kit解压出来，并重命名CrossC2-GithubBot-2021-09-13.cna为CrossC2.cna  

3.将CrossC2Kit、CrossC2.cna、genCrossC2.Linux放到CobaltStrike客户端根目录下，我这边在客户端根目录下创建目录Plugins/CrossC2后，并将3个文件放到Plugins/CrossC2/下  

4.修改CrossC2.cna中$CC2_PATH的值为：/xx/xx/Plugins/CrossC2/，$CC2_BIN的值为：genCrossC2.Linux  

5.创建windows/beacon_https/reverse_https监听器  

6.拷贝teamserver目录的.cobaltstrike.beacon_keys到本地CobaltStrike客户端根目录下  

7.登录CS，选择Cobalt Strike->脚本管理器，加载./Plugins/CrossC2/CrossC2.cna和Plugins/CrossC2/CrossC2Kit/CrossC2Kit_Loader.cna  

8.使用CrossC2生成linux下payload，只需指定监听器和输出路径，其他默认即可，会生成2个文件，如CrossC2和CrossC2.lib，成功上线后如下图  
![image](./pic/1.png)  

# 2、使用profile：
1.用官方提供的profile：[https://github.com/gloxec/CrossC2/blob/cs4.1/protocol_demo/https.profile](https://github.com/gloxec/CrossC2/blob/cs4.1/protocol_demo/https.profile)替换自己profile中http-get和http-post部分（我这边将https.profile和c2profile.c中的www.google.com改为www.baidu.com），并编译官方提供的c源码：[https://github.com/gloxec/CrossC2/blob/cs4.1/protocol_demo/c2profile.c](https://github.com/gloxec/CrossC2/blob/cs4.1/protocol_demo/c2profile.c)  
2.然后编译：gcc c2profile.c -fPIC -shared -o lib_rebind_test.so  
生成payload时，指定rebind_dynamic_lib，其他步骤同上即可，成功上线后如下图  
![image](./pic/2.png)  

# 参考链接：  
https://github.com/gloxec/CrossC2/blob/cs4.1/README_zh.md  
https://hack-for.fun/67f2.html  
https://gloxec.github.io/CrossC2/zh_cn/usage/cna.html  
https://gloxec.github.io/CrossC2/zh_cn/protocol/  
