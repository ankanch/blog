---
title: Windows下使用命令安装Python的scipy库出错的解决方案
tags:
  - python库安装
  - scipy
  - scipy安装出错
id: 653
categories:
  - Python
date: '2017-01-14T15:39:37.000Z'
---

# Windows下使用命令安装Python的scipy库出错的解决方案

最近在准备GSoC2017的时候一个项目需要用到Scipy库。

本来以为非常简单的事情，结果我硬是弄了10多分钟才解决。

正常来讲，安装一个python的库只需要通过一下命令即可：

```
pip install package-name
```

错误如下图：

[![QQ&#x622A;&#x56FE;20170114112205](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2017/01/QQ截图20170114112205.jpg)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2017/01/QQ截图20170114112205.jpg)

最开始以为是以为我python2和python3共存的缘故导致安装失败，可后面发现貌似并不是这样的。

在网络上搜索一番后，虽然没有找到财务原因，但是找到了如何解决这个错误。

解决方法如下：

下载scipy对应的whl包，如何通过pip直接安装whl包，而不是在pypi索引去搜索下载。

有一个网站，它的介绍如下：

```
This page provides 32- and 64-bit Windows binaries of many scientific open-source extension packages for the official [CPython distribution](http://www.python.org/download/) of the [Python](http://www.python.org/) programming language.
```

[**http://www.lfd.uci.edu/~gohlke/pythonlibs/**](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

在上面那个网站找到对应的python版本下载，如何再用一下命令安装即可：

**查看你的python的32位还是64位直接在命令行输入python即可。**

```
pip install package-name.whl
```

===================

如果你不是windows，一切都要好办多了，基本上劝都可以通过pip install 命令来安装。

[参考：http://blog.csdn.net/u011177305/article/details/52334023](http://blog.csdn.net/u011177305/article/details/52334023)



`© kanch` → [zl AT kanchz DOT com](kanchisme@gmail.com) → _posted at {{page.date}}_
_last updated on 2019-08-12 16:02:21.020573_