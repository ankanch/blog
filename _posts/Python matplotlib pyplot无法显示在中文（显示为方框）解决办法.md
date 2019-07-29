---
title: Python matplotlib pyplot无法显示在中文（显示为方框）解决办法
tags:
  - matplotlib
  - python
  - 显示中文
  - 爬虫
  - 编程
id: 487
categories:
  - Python
date: 2016-08-31 15:27:05
---

无法显示中文，大概如下图中顶部的样子：

[![figure_1](http://115.159.197.66/wp-content/uploads/2016/08/figure_1-300x225.png)](http://115.159.197.66/wp-content/uploads/2016/08/figure_1.png)

在网上搜索一番，提到的大多数解决方式都不可用，类似于下面这样：
<pre class="lang:python decode:true ">pyplot.title(u"中文")
pyplot.title(u'\u4e2d\u6587') #  (unicode编码)
pyplot.title('\xe4\xb8\xad\xe6\x96\x87') # (utf-8编码)</pre>
最后在一个博客上找到了解决方法，添加FontProperties 包，然后指定字体。

如下：
<pre class="lang:python decode:true ">from matplotlib import pyplot  
from matplotlib.font_manager import FontProperties  
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)  

pyplot.title(u'中文', fontproperties=font_set)</pre>
然后就完美解决了无法显示中文的问题。

[![figure_1](http://115.159.197.66/wp-content/uploads/2016/08/figure_1-1-300x225.png)](http://115.159.197.66/wp-content/uploads/2016/08/figure_1-1.png)

&nbsp;

参考来源：http://blog.csdn.net/garfielder007/article/details/51405139