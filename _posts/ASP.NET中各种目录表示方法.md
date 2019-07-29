---
title: ASP.NET中各种目录表示方法
tags:
  - ASP.NET
  - 目录表示
  - 访问上一级目录
id: 58
categories:
  - C++ / Visual C++
date: 2015-06-19 11:50:47
---

在ASP.NET中跳转目录，有如下表示方法。

1、"<span style="color: #ff00ff;">**/xxx.xx**</span>" 表示从网站根目录开始,即网站根目录下的xxx.xx文件

2、"<span style="color: #ff00ff;">**./xxx.xx**</span>"表示本目录下的xxx.xx

3、"**<span style="color: #ff00ff;">../xxx.xx</span>**"表示上一级目录中的xxx.xx，当然，"../../xxx.xx"表上上一级目录中的xxx.xx

4、"<span style="color: #ff00ff;">**xxx/**</span>"表示当前目录下的xxx文件夹,也相当与"./xxx/"

&nbsp;