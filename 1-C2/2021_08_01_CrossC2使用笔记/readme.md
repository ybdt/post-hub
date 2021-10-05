CrossC2使用版本v3.0.1-dev

使用步骤：  
1、下载CrossC2-GithubBot-2021-09-13.cna、CrossC2Kit-GithubBot-2021-09-13.zip、genCrossC2.Linux  

2、将CrossC2Kit-GithubBot-2021-09-13.zip内的文件夹CrossC2Kit解压出来，并重命名CrossC2-GithubBot-2021-09-13.cna为CrossC2.cna  

3、将CrossC2Kit、CrossC2.cna、genCrossC2.Linux放到CobaltStrike客户端根目录下插件目录下，我这边创建目录Plugins后，将所有插件统一放到Plugins/下，创建目录Plugins/CrossC2，并将3个文件放到Plugins/CrossC2/下  

4、修改CrossC2.cna中$CC2_PATH的值为：/xx/xx/Plugins/CrossC2/，$CC2_BIN的值为：genCrossC2.Linux  

5、创建windows/beacon_https/reverse_https监听器  

6、拷贝teamserver目录的.cobaltstrike.beacon_keys到本地CobaltStrike客户端根目录下  

7、登录CS，选择Cobalt Strike->脚本管理器，加载./Plugins/CrossC2/CrossC2.cna和Plugins/CrossC2/CrossC2Kit/CrossC2Kit_Loader.cna  

（注意，当前方法不能使用C2Profile及CDN）  
8、使用CrossC2生成linux下payload，只需指定监听器和输出路径，其他默认即可，会生成2个文件，如CrossC2和CrossC2.lib，执行后可上线，如下图  
![image](./pic/1.png)  
