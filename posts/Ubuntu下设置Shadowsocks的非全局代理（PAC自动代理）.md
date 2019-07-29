---
title: Ubuntu下设置Shadowsocks的非全局代理（PAC自动代理）
tags:
  - genepac
  - PAC
  - shadowsocks
  - Ubuntu
  - Ubuntu代理设置
  - 全局代理
  - 翻墙
  - 自动代理
id: 380
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 翻墙相关 / VPN
date: 2016-01-21 17:38:25
---

&nbsp;

shadowsocks就不容我多介绍了吧，对于我这种重度google用户来说，装了Ubuntu后也要保持一直翻墙。

在我在Ubuntu上安装了shadowsocks后发现，卧槽，这尼玛算半成品吧，只有全局代理。。。。

和windows，Mac，手机上的客户端相差太远了吧。

[shadowsocks各平台客户端下载请点击我](https://shadowsocks.com/client.html)

下面进入正题。

首先我们要安装Genepac，它可以用来生成我们自己的PAC文件，同时它还支持获取gfwlist的时候设置代理。

（安装Genepac之前，请务必确认你已经安装了pip，如果没没有安装，文章末尾有说明）

然后我们用下面这个命令安装Genepac：
<pre class="lang:sh decode:true">sudo pip install genpac</pre>
为了方便管理生成的pac文件，我们在/home/目录下新建一个文件夹，命名为shadowsocks
<pre class="lang:default decode:true ">mkdir ~/shadowsocks
cd shadowsocks</pre>
然后我们在刚刚建立的shadowsocks文件夹里面打开终端

用以下命令生成pac文件
<pre class="lang:sh decode:true ">genpac --proxy="SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" -o autoproxy.pac --gfwlist-url="https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt"
</pre>
生成pac文件后，我们打开系统设置-&gt;网络-&gt;代理，如图：

[![pac_set](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/pac_set.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/pac_set.png)

设置代理为自动，然后配置URL填入我们刚刚生成的那个pac文件的路径即可。

* * *

pip的安装

（内容来自：[How to install pip on Ubuntu-saltycrane.com](http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)）

对于Ubuntu12.10以上的版本，依次输出以下命令即可：
<pre class="lang:sh decode:true">$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv</pre>
对于12.10之前的版本，请参考我上面贴出的网站

&nbsp;