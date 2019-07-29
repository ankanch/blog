---
title: 关联本地仓库和GitHub仓库
tags:
  - Git
  - Github
  - SSH
  - SSH Key
  - ssh-keygen
  - 版本库
id: 503
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 转载
date: 2016-09-20 19:04:40
---

本篇文章适用于你已经在本地创建了一个Git仓库，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步。

首先我们需要一个SSH key，这个SSH key可以帮助GitHub判断是哪个用户推送的信息。
<pre class="lang:sh decode:true ">$ ssh-keygen -t rsa -C "注册邮箱"
比如：
$ ssh-keygen -t rsa -C "kanchisme@gmail.com"</pre>
然后用户主目录/.ssh/下有两个文件，id_rsa是私钥，id_rsa.pub是公钥

然后我们需要获取刚才生成的SSH key，打开.ssh下的id_rsa.pub文件，里面的内容就是key的内容。

然后我们复制整个文件的内容，粘贴到GitHub的SSH Key页面，如图：

[![qq%e6%88%aa%e5%9b%be20160920185818](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/09/QQ截图20160920185818-1024x553.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/09/QQ截图20160920185818.png)

保存后，如果我们要从远程仓库克隆一份到本地可以通过git clone：
<pre class="lang:sh decode:true ">git clone git@github.com:ankanch/xx.git</pre>
如果要将本地库关联远程库，就需要在本地仓库目录运行命令git remote add origin：
<pre class="lang:sh decode:true ">git remote add origin git@github.com:ankanch/xx.git</pre>
推送master分支的所有内容到GitHub：
<pre class="lang:sh decode:true ">git push -u origin master</pre>
第一次使用加上了-u参数，是推送内容并关联分支。

推送成功后就可以看到远程和本地的内容一模一样，下次只要本地作了提交，就可以通过命令：
<pre class="lang:sh decode:true ">git push origin master</pre>
有了推送更新到GitHub，那必然有拉取远程某个分支更新到本地，使用如下命令即可：
<pre class="lang:sh decode:true ">git pull origin master</pre>

* * *

大家在执行以上命令的时候可能会遇到错误，比如Permission Denied，可能是因为公钥没有复制正确或者SSH Agent未开启的原因。

不过，我觉得，大多数情况都是SSH Agent未开启的原因。

要解决这种问题，请运行Git Bash，注意，是Git Bash，而不是Windows的命令行，然后依次执行以下命令即可：
<pre class="lang:sh decode:true ">cd X:\\Projects-X\\Tieba-zhuaqu     
eval "$(ssh-agent -s)"               
ssh-add Q:\\SSHkeys\\GitHubPull\\githubKey
git push -u origin master</pre>
上面的代码首先切换到了本地Git仓库，然后，开启SSH Agent，选择密钥，然后推送更新。