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
date: '2015-10-04T17:42:02.000Z'
layout: posting
---

# 利用VPS搭建shadowsocks服务器（转）

继红杏出墙，时空隧道等一系列著名翻墙插件被封杀后，翻墙方式也越来越少。但对于博主这种重度谷歌用户，怎能屈服于GFW呢。

## **shadowsocks简介（搬运至互联网）**

shadowsocks是一款自定义协议的代理软件，由于其流量特征不明显，（直到不久前）一直可以稳定提供上网代理。shadowsocks客户端会在本地开启一个socks5代理，通过此代理的网络访问请求由客户端发送至服务端，服务端发出请求，收到响应数据后再发回客户端。因此使用shadowsocks需要一台墙外的服务器来部署shadowsocks服务端。

再来谈谈VPS服务器的问题吧，博主用的[**BudgetVM**](https://www.budgetvm.com/account/aff.php?aff=3228)的，用了1年多了，感觉还不错，同时呢，网上还给出了其它的VPS服务提供商，比较著名的还有[Linode](http://welcome.linode.com/features/?gclid=Cj0KEQjwnMOwBRCAhp-ysqCwypkBEiQAeSy1-basvgxVbtZ7mjtO5aY6BIm307OZrahN_rZLd-bzZ8caAji68P8HAQ)和[Digital Ocean](https://www.digitalocean.com/?utm_source=google&amp;utm_medium=brand_sem&amp;utm_campaign=Brand_Protection&amp;utm_term=digital%20ocean&amp;adgroup=9971414725&amp;matchtype=e&amp;network=g&amp;device=c&amp;position=1t1)，至于它们各自的易用性，还是读者自己每个都买一年试试吧。

## **接下来进入在VPS上部署Shadowsocks服务器正题**

首先肯定要登陆你的VPS，登陆后按照以下命令，来安装和启动服务。

（PS，我用的CentOS6 32bit）

#### **安装shadowsocks**

打开shell，使用VPS服务商提供的root用户和密码SSH登录VPS。然后执行如下命令：

**Debian/Ubuntu:**

apt-get install python-pip pip install shadowsocks

_请选择对应系统的命令_

**CentOS:**

yum install python-setuptools && easy\_install pip pip install shadowsocks

命令输入后，稍作等待，shadowsocks就安装好了。

有时Ubuntu会遇到第一个命令安装python-pip时找不到包的情况。pip官方给出了一个安装脚本，可以自

动安装pip。先下载脚本，然后执行即可：

wget [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) python get-pip.py

### **接下来，编写配置文件**

shadowsocks启动时的参数，如服务器端口，代理端口，登录密码等，可以通过启动时的命令行参数来设

定，也可以通过json格式的配置文件设定。推荐使用配置文件，方便查看和修改。

用vi新建一个配置文件：

vi /etc/shadowsocks.json 然后输入如下内容：

{  "server":"my\_server\_ip",  "server\_port":25,  "local\_address": "127.0.0.1",  "local\_port":1080,  "password":"mypassword",  "timeout":300,  "method":"aes-256-cfb",  "fast\_open": false }

server改成你VPS服务器的IP地址！ 使用 :wq命令保存退出。

### **启动shadowsocks**

如果已经写好了配置文件，启动shadowsocks服务器的命令如下：

ssserver -c /etc/shadowsocks.json 后台启动和停止shadowsocks服务器：

ssserver -c /etc/shadowsocks.json -d start ssserver -c /etc/shadowsocks.json -d stop shadowsocks的日志保存在 /var/log/shadowsocks.log

### **安装并启动shadowsocks客户端**

shadowsocks支持windows、Mac OS X、Linux、Android、iOS等多个平台。

[Shadowsocks客户端下载，个平台使用教程，请看这里：](https://s-s.pw/)

[https://s-s.pw/](https://s-s.pw/)

下载安装客户端以后，只需按服务器的配置填写IP地址、服务器端口、本地端口（如果没有本地端口选

项，就是默认的1080）、密码、加密方式等参数，启动就可以了。

客户端支持全局代理和PAC代理两种方式，后者会使用一个脚本来自动检查一个网站是否在需要代理的网

站列表中，自动选择直接连接或代理连接。

PAC列表可以在线更新（地址：[https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt](https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt)）



{% include post_footer.md %}