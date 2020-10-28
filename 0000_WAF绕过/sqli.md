1、
```
/*!*/
解释：mysql为了兼容其他数据库，将mysql特有的东西放到/*!*/中，这样在其他数据库中会将其视为注释，但在mysql中会解释执行
```
参考实例：  
https://mp.weixin.qq.com/s/84se5CxYlVT05bcw654wKg 这篇文章用到了上述的技巧绕过了Mod_Security
