---
title: 利用VPS搭建shadowsocks服务器（转）
tags:
  - shadowsocks
  - VPN
  - VPS
  - 翻墙
id: 173
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 翻墙相关 / VPN
  - 转载
date: 2015-10-04 17:42:02
---

&nbsp;

继红杏出墙，时空隧道等一系列著名翻墙插件被封杀后，翻墙方式也越来越少。但对于博主这种重度谷歌用户，怎能屈服于GFW呢。

### **shadowsocks简介（搬运至互联网）**

shadowsocks是一款自定义协议的代理软件，由于其流量特征不明显，（直到不久前）一直可以稳定提供上网代理。shadowsocks客户端会在本地开启一个socks5代理，通过此代理的网络访问请求由客户端发送至服务端，服务端发出请求，收到响应数据后再发回客户端。因此使用shadowsocks需要一台墙外的服务器来部署shadowsocks服务端。

再来谈谈VPS服务器的问题吧，博主用的**[BudgetVM](https://www.budgetvm.com/account/aff.php?aff=3228)**的，用了1年多了，感觉还不错，同时呢，网上还给出了其它的VPS服务提供商，比较著名的还有[Linode](http://welcome.linode.com/features/?gclid=Cj0KEQjwnMOwBRCAhp-ysqCwypkBEiQAeSy1-basvgxVbtZ7mjtO5aY6BIm307OZrahN_rZLd-bzZ8caAji68P8HAQ)和[Digital Ocean](https://www.digitalocean.com/?utm_source=google&amp;utm_medium=brand_sem&amp;utm_campaign=Brand_Protection&amp;utm_term=digital%20ocean&amp;adgroup=9971414725&amp;matchtype=e&amp;network=g&amp;device=c&amp;position=1t1)，至于它们各自的易用性，还是读者自己每个都买一年试试吧。

* * *

&nbsp;

### **接下来进入在VPS上部署Shadowsocks服务器正题**

首先肯定要登陆你的VPS，登陆后按照以下命令，来安装和启动服务。

（PS，我用的CentOS6 32bit）

* * *

&nbsp;

##### **安装shadowsocks**

&nbsp;

打开shell，使用VPS服务商提供的root用户和密码SSH登录VPS。然后执行如下命令：

* * *

&nbsp;

###### **Debian/Ubuntu:**

<span style="color: #ff00ff;">apt-get install python-pip</span>
<span style="color: #ff00ff;">pip install shadowsocks</span>

<span style="color: #ff0000;">_请选择对应系统的命令_</span>

###### **CentOS:**

<span style="color: #ff00ff;">yum install python-setuptools &amp;&amp; easy_install pip</span>
<span style="color: #ff00ff;">pip install shadowsocks</span>

* * *

命令输入后，稍作等待，shadowsocks就安装好了。

有时Ubuntu会遇到第一个命令安装python-pip时找不到包的情况。pip官方给出了一个安装脚本，可以自

动安装pip。先下载脚本，然后执行即可：

<span style="color: #ff00ff;">wget https://bootstrap.pypa.io/get-pip.py</span>
<span style="color: #ff00ff;">python get-pip.py</span>

* * *

#### **接下来，编写配置文件**

&nbsp;

shadowsocks启动时的参数，如服务器端口，代理端口，登录密码等，可以通过启动时的命令行参数来设

定，也可以通过json格式的配置文件设定。推荐使用配置文件，方便查看和修改。

用vi新建一个配置文件：

<span style="color: #ff00ff;">vi /etc/shadowsocks.json</span>
然后输入如下内容：

<span style="color: #ff99cc;">{ </span>
<span style="color: #ff99cc;"> "server":"my_server_ip", </span>
<span style="color: #ff99cc;"> "server_port":25, </span>
<span style="color: #ff99cc;"> "local_address": "127.0.0.1", </span>
<span style="color: #ff99cc;"> "local_port":1080, </span>
<span style="color: #ff99cc;"> "password":"mypassword",</span>
<span style="color: #ff99cc;"> "timeout":300, </span>
<span style="color: #ff99cc;"> "method":"aes-256-cfb", </span>
<span style="color: #ff99cc;"> "fast_open": false</span>
<span style="color: #ff99cc;">}</span>

server改成你VPS服务器的IP地址！
使用 <span style="color: #ff00ff;">:wq </span>命令保存退出。

* * *

&nbsp;

#### **启动shadowsocks**

&nbsp;

如果已经写好了配置文件，启动shadowsocks服务器的命令如下：

<span style="color: #ff00ff;">ssserver -c /etc/shadowsocks.json</span>
后台启动和停止shadowsocks服务器：

<span style="color: #ff00ff;">ssserver -c /etc/shadowsocks.json -d start</span>
<span style="color: #ff00ff;">ssserver -c /etc/shadowsocks.json -d stop</span>
shadowsocks的日志保存在 /var/log/shadowsocks.log

* * *

&nbsp;

#### **安装并启动shadowsocks客户端**

shadowsocks支持windows、Mac OS X、Linux、Android、iOS等多个平台。

[Shadowsocks客户端下载，个平台使用教程，请看这里：](https://s-s.pw/)

[https://s-s.pw/](https://s-s.pw/)

下载安装客户端以后，只需按服务器的配置填写IP地址、服务器端口、本地端口（如果没有本地端口选

项，就是默认的1080）、密码、加密方式等参数，启动就可以了。

<span style="line-height: 1.5;">[![SSsetsd](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/10/SSsetsd.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/10/SSsetsd.png)</span>

<span style="line-height: 1.5;">客户端支持全局代理和PAC代理两种方式，后者会使用一个脚本来自动检查一个网站是否在需要代理的网</span>

站列表中，自动选择直接连接或代理连接。

PAC列表可以在线更新（地址：[https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt](https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt)）

&nbsp;