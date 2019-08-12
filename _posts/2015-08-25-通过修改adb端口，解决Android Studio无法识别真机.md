---
title: 通过修改adb端口，解决Android Studio无法识别真机
tags:
  - adb
  - adb无法识别真机
  - android studio
  - 安卓adb端口
id: 121
categories:
  - Android开发 / Android Studio
date: '2015-08-25T21:34:25.000Z'
---

# 通过修改adb端口，解决Android Studio无法识别真机

**注意：该方法只适用于adb端口呗占用导致的无法识别真机！**

最近新换了windows10，在调试Android Studio程序时发现：**Android Studio无法识别真机**。

经过一番搜索，了解到是因为a**db端口被占用**，导致问题发生。

虽然adb的端口被占用了，但是占用端口的进程是必须启动的，不能被杀死，网上很多办法都说的是杀死占用端口的进程。尝试后发现这个方法并不适用于我。

所以在此推荐一个新的方法：通过修改adb的默认端口，来防止端口被占用。

## **方法如下：**

新建一个环境变量，名字为_**ANDROID\_ADB\_SERVER\_PORT**_，然后它的值设为一个新的端口号码，比如说9999。

再次启动Android Studio调试程序，adb就可以识别真机了。

[![adb\_set\_port](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/08/adb_set_port.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/08/adb_set_port.png)

如下图，现在可以识别真机了。

注意：输入**adb nodaemon server**可以查看哪个端口被占用了，没有端口呗占用，输入后会无反应。



`© kanch` → [zl AT kanchz DOT com](kanchisme@gmail.com) → _posted at {{page.date}}_
_last updated on 2019-08-12 16:02:21.020573_