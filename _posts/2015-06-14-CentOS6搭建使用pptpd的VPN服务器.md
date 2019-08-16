---
title: CentOS6搭建使用pptpd的VPN服务器
tags:
  - CentOS6
  - PPTP的VPN搭建
  - VPS搭建
id: 16
categories:
  - Linux / Unix /虚拟主机 / VPS
date: '2015-06-14T18:55:01.000Z'
---

我的安装环境: *CentOS 6*

首先,检测是否可以安装pptp
```shell
 cat /dev/ppp 
 cat: /dev/ppp: No such device or address 
 cat /dev/net/tun 
 cat: /dev/net/tun: File descriptor in bad state
```
以上输出表示不支持ppp

centos7.x 如果使用iptables要先卸载firewalld：
```shell
systemctl stop firewalld 
systemctl disable firewalld
yum -y remove firewalld
```
**1.安装ppp服务及相关组件**
```shell
yum install -y ppp iptables 
```
注：centos7.x 还需要 yum -y install iptables-services

**2.下载pptpd最新版本的rpm包** 

pptpd最新安装包地址[http://poptop.sourceforge.net/yum/stable/packages/](http://poptop.sourceforge.net/yum/stable/packages/)

**centos7.x** 
x64: 
```shell
http://dl.fedoraproject.org/pub/epel/7/x86_64/p/pptpd-1.4.0-2.el7.x86_64.rpm
```

 或者直接安装
 ```shell
  yum -y install pptpd
  ```

**3.安装下载好的相应rpm包** 

例如32bit的centos5.x：
```shell
 rpm -ivh pptpd-1.4.0-1.rhel5.i386.rpm
 ```

**4.设置pptpd解析用的dns**
```shell
vi /etc/ppp/options.pptpd ms-dns 8.8.8.8 ms-dns 8.8.4.4
```

**5.设置拨号时候用的：用户名、拨号方式、用户密码、来源ip地址**

用户名和密码可以随便设置，拨号方式只能填pptpd，来源ip用*号代表不限制
```shell
vi /etc/ppp/chap-secrets myusername pptpd mypassword *
```

**6.设置本地ip和远端ip**

本地ip就是建立拨号后分配给你的，远端ip是分配给服务器的
```shell
vi /etc/pptpd.conf localip 192.168.8.1 remoteip 192.168.8.11-30
```
**7.设置ip转发状态为生效，然后立即载入**

和第9步的NAT转发有关
```shell
vi /etc/sysctl.conf net.ipv4.ip_forward = 1 /sbin/sysctl -p
```
**8.启动pptpd服务，并且设置为开机启动**
```shell
/sbin/service pptpd start chkconfig pptpd on
```
**9.启动iptables规则，设置NAT转发，然后保存**

iptables本身就是开机启动的，不需要再用chkconfig iptables on了
```shell
/sbin/service iptables restart /sbin/iptables -t nat -A POSTROUTING -s 192.168.8.0/24 -o venet0 -j MASQUERADE (vps用venet0,否则用eth0)
service iptables save 
```
避免造成一些网页无法显示，MSN无法登陆的解决办法： 添加下面的iptables规则，设置 session MTU 为 1356，然后保存。
```shell
iptables -I FORWARD -p tcp –syn -s 192.168.8.0/24 -j TCPMSS –set-mss 1356
service iptables save 
```
执行 
```shell
/sbin/iptables -t nat -A POSTROUTING -s 192.168.8.0/24 -o venet0 -j MASQUERADE 
```

命令， 如果返回iptables: Unknown error 4294967295，表明系统还不支持，需要联系客服开通iptables_nat模块支持。 或者使用：
```shell
/sbin/iptables -t nat -A POSTROUTING -o venet0 -s 192.168.8.0/24 -j SNAT –to-source xxx.xxx.xxx.xxx
```

 1.检查PPP是否支持MPPE
```shell
strings ‘/usr/sbin/pppd’ |grep -i mppe | wc –lines
```
如果以上命令输出为“0”则表示不支持；输出为“30”或更大的数字就表示支持。 

2.以下命令检查内核MPPE补丁是否安装成功，MPPE module可否载如：
```shell
 modprobe ppp-compress-18 && echo success
```
**如果显示错误：** iptables: Saving firewall rules to /etc/sysconfig/iptables: /etc/init.d/iptables: line 268: restorecon: command not found 解决方法：yum install policycoreutils

**3.如果端口没有开启则开启下面相关端口：
```shell
iptables -I INPUT -p tcp –dport 1723 -j ACCEPT iptables -I INPUT -p tcp –dport 47 -j ACCEPT iptables -I INPUT -p gre -j ACCEPT
```


{% include post_footer.md %}