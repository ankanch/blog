---
title: Ubuntu下连接不上WiFi，无法弹出输入密码对话框的解决方法
tags:
  - Ubuntu
  - Ubuntu连不上wifi
  - wifi
  - wifi连接失败
  - 无法连接wifi
id: 501
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 转载
date: '2016-09-19T13:13:21.000Z'
layout: posting
---

# Ubuntu下连接不上WiFi，无法弹出输入密码对话框的解决方法

该问题的情况是：

一直显示正在连接网络，无论是否有密码，而且不会弹出输入密码的对话框。

解决方法：

编辑/etc/modprobe.d/iwlwifi.conf文件即可解决

首先要打开终端，然后输入：

```
sudo vim /etc/modprobe.d/iwlwifi.conf
options iwlwifi 11n_disable=1
```

我的系统是 Ubuntu 16.04 LTS



{% include post_footer.md %}