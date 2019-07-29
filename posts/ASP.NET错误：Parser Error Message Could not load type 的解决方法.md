---
title: 'ASP.NET错误：Parser Error Message: Could not load type 的解决方法'
tags:
  - ASP.NET
  - Could not load type
id: 100
categories:
  - 网站制作相关
date: 2015-07-22 22:11:35
---

&nbsp;

&nbsp;

目前已知以下两种可能会引起Parser Error Message: Could not load type "..."如下：

* * *

&nbsp;

<span style="color: #993300;">**第一种**</span>是由于aspx文件开头的代码：
<pre class=""><%@Page Language="C#" AutoEventWireup="true" CodeBehind="SteamLoginWebPage.aspx.cs" Inherits="SteamLogin.WebPage" %></pre>
上面代码红色加粗部分改为CodeFile即可解决问题

* * *

&nbsp;

<span style="color: #993300;">**第二种**</span>则是文件系统的bin文件没有放到服务器根目录导致

将bin文件夹移到服务器根目录即可解决。

&nbsp;