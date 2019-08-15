---
title: 给WordPress博客添加favicon图标
tags:
  - favicon
  - wordpress
  - wordpress添加favicon
id: 52
categories:
  - 网站制作相关
date: '2015-06-18T13:22:00.000Z'
---

# 给WordPress博客添加favicon图标

首先解释下什么是favicon（[来自维基百科](https://zh.wikipedia.org/wiki/Favicon)） **Favicon**是_favorites icon_的缩写，亦被称为**website icon**（网页图标）、**page icon**（页面图标）或**urlicon**（[URL](https://zh.wikipedia.org/wiki/URL)图标）。Favicon是与某个[网站](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%AB%99)或[网页](https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5)相关联的[图标](https://zh.wikipedia.org/wiki/%E5%9B%BE%E6%A0%87)。网站设计者可以多种方式创建这种图标，而目前也有很多[网页浏览器](https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5%E6%B5%8F%E8%A7%88%E5%99%A8)支持此功能。浏览器可以将favicon显示于浏览器的地址栏中，也可置于书签列表的网站名前，还可以放在标签式浏览界面中的页标题前。 因此，你需要现拥有一个favicon文件。

你可以自己制作图标文件可以利用 [Icon Works](http://icon-works.com/)

也可以将自己已有的图片在线转换成ico图标文件，推荐这个工具 [在线制作ico图标](http://www.bitbug.net/)

然后，将你做好的favicon.ico**放入你web服务器的根目录**。（当然也可以使其他目录，我们需要记住路径）

进入wordpress管理后台，打开 **外观-&gt;编辑**

选择文件目录中的 **顶部（header.php）**，并打开它。

在&lt;head&gt;&lt;/head&gt;间加入以下代码： \*\*&lt;link rel="shortcuticon"href="[http://example.com/favicon.ico](http://example.com/favicon.ico)"type="image/vnd.microsoft.icon"&gt;&lt;/span&gt; ****&lt;link rel="icon" href="[http://example.com/favicon.ico](http://example.com/favicon.ico)" type="image/vnd.microsoft.icon\*\*"&lt;/span&gt;&gt;&lt;/span&gt;&lt;/span&gt;

如果你将favicon.ico放在了网站根目录，则把加粗部分换成你的域名即可。

