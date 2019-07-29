---
title: Windows下使用命令安装Python的scipy库出错的解决方案
tags:
  - python库安装
  - scipy
  - scipy安装出错
id: 653
categories:
  - Python
date: 2017-01-14 15:39:37
---

最近在准备GSoC2017的时候一个项目需要用到Scipy库。

本来以为非常简单的事情，结果我硬是弄了10多分钟才解决。

正常来讲，安装一个python的库只需要通过一下命令即可：
<pre class="lang:sh decode:true ">pip install package-name</pre>
于是看到需要用到scipy库后我做的第一件事情就是使用以上命令尝试安装，然后不幸的是，报错了。

错误如下图：

[![QQ截图20170114112205](http://akakanch.com/wp-content/uploads/2017/01/QQ截图20170114112205.jpg)](http://akakanch.com/wp-content/uploads/2017/01/QQ截图20170114112205.jpg)

最开始以为是以为我python2和python3共存的缘故导致安装失败，可后面发现貌似并不是这样的。

在网络上搜索一番后，虽然没有找到财务原因，但是找到了如何解决这个错误。

解决方法如下：

下载scipy对应的whl包，如何通过pip直接安装whl包，而不是在pypi索引去搜索下载。

有一个网站，它的介绍如下：
<pre class="">This page provides 32- and 64-bit Windows binaries of many scientific open-source extension packages for the official [CPython distribution](http://www.python.org/download/) of the [Python](http://www.python.org/) programming language.</pre>
这个网站提供了windows下几乎所有python的科学计算库：

**[http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/)**

在上面那个网站找到对应的python版本下载，如何再用一下命令安装即可：

**查看你的python的32位还是64位直接在命令行输入python即可。**
<pre class="lang:sh decode:true">pip install package-name.whl</pre>
**在安装scipy的过程中还有可能会遇到MemoryError**，这种情况是由于内存不够，关点软件就行了。我之前在Ubuntu安装Scipy就遇到了该错误，，当时内存大概有600MB剩余，，，关了一个软件变成700MB剩余后解决了该问题。

===================

如果你不是windows，一切都要好办多了，基本上劝都可以通过pip install 命令来安装。

[参考：http://blog.csdn.net/u011177305/article/details/52334023](http://blog.csdn.net/u011177305/article/details/52334023)