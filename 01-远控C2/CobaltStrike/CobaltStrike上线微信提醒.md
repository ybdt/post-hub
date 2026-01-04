原文有图文说明，我就不再赘述，可参考原文[https://xz.aliyun.com/t/10698](https://xz.aliyun.com/t/10698)中的[微信单人提醒](https://xz.aliyun.com/t/11099#toc-9)部分

参照原文后，会发生报错，有如下2处需要修改：  
01、vps会提示需要转发x11请求，解决办法：启动时需要加一个参数-Djava.awt.headless=true，修改后agscript如下

```
java -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Djava.awt.headless=true -classpath ./cobaltstrike.jar aggressor.headless.Start $*
```

02、启动时会有安全提醒，需要注释掉如下

```
This can be done by editing the accessibility.properties file for OpenJDK:
sudo vim /etc/java-8-openjdk/accessibility.properties
Comment out the following line:
assistive_technologies=org.GNOME.Accessibility.AtkWrapper
```

agscript-start.sh如下

```
./agscript CS公网IP CS端口 用户名 CS密码 PushPlus.cna
```

# 参考链接
https://github.com/microsoft/vscode-arduino/issues/644