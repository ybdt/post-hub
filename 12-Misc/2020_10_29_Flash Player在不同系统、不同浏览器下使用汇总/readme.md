问题源于我登录公司oa，却提示需要flash player  

首先可通过访问吉林省图书馆（jlplib.com.cn），测试当前chrome浏览器是否有flash player  
ubuntu下的chrome浏览器有flash player，默认是关闭的，但即使开启，访问博鸿科技oa系统时，仍不能访问，提示需要flash player  
windows下的chrome浏览器有flash player，默认是关闭的，但即使开启，访问博鸿科技oa系统时，仍不能访问，提示需要flash player  

可通过访问吉林省图书馆（jlplib.com.cn），以及结合查看firefox的附加组件中是否有shockwave flash，查看firefox浏览器下是否有flash player  
windows下的firefox浏览器的附加组件中有shockwave flash，访问吉林省图书馆（jlplib.com.cn）时，默认会提醒开启，访问博鸿科技oa系统时，也是提醒开启  
ubuntu下的firefox浏览器的附加组件中没有shockwave flash，访问吉林省图书馆（jlplib.com.cn）时，默认会不能显示，访问博鸿科技oa系统时，也是不能显示  
本打算从附加组件中安装shockwave flash，但没有搜到，后经查阅，好像需要系统安装的方式，命令行下执行：  
sudo apt install flashplugin-installer  
然后重启firefox，在附加组件中仍没有shockwave flash，但访问吉林省图书馆（jlplib.com.cn）时，会提醒开启，访问博鸿科技oa系统时，也是提醒开启  

对于windows下的edge和ie，不能访问吉林省图书馆（jlplib.com.cn）时，也不能访问博鸿科技oa系统  
能访问吉林省图书馆（jlplib.com.cn）时，edge不能访问博鸿科技oa系统，ie能访问博鸿科技oa系统  
原因不清楚，猜测博鸿科技oa系统不能适配新版flash player  
