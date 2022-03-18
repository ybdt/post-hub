首先，github是基于git的一个提供版本控制（代码托管）等服务的网站  
其次，git是分布式版本控制系统，同一个git仓库可以分布到不同的机器上，这里的机器可以指公司的git服务器或者github

sudo apt install git  
git config --global user.name "YOUR NAME"  
git config --global user.email "YOUR EMAIL ADDRESS"  
#执行命令git可查看帮助信息  

#本地创建仓库，然后推送到远程github  
mkdir ./git-tmp  
cd ./git-tmp  
git init  
echo a>class.py  
git add ./class.py  
git commit -m "learn git and github"  
#通过ssh-kengen创建公钥私钥对  
#将公钥拷贝到github的Settings->“SSH and GPG keys”  
#在github中创建一个相同名称（git-tmp）的仓库  
git remote add origin git@github.com:xuxuedong/git-tmp.git  
git push -u origin master#注意中国访问github有时会有些慢，如果很慢可尝试挂上代理

#克隆远程github仓库到本地  
git clone git@github.com:xuxuedong/yibudengtian-ctf-db.git  
git rm -r 2019_12_02_xxe靶机渗透学习笔记/  
cp ../ybdt-opts/* ./  
git add ./2020-*  
git commit -m "arrange the file"  
git push origin master#注意中国访问github可能会有些慢，挂上代理会更快

参考链接：  
https://blog.csdn.net/u012526120/article/details/49401871  
https://help.github.com/en/github/getting-started-with-github/set-up-git  
https://stackoverflow.com/questions/7434449/why-use-git-rm-to-remove-a-file-instead-of-rm  
