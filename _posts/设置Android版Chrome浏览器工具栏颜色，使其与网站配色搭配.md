---
title: 设置Android版Chrome浏览器工具栏颜色，使其与网站配色搭配
tags:
  - android
  - Chrome
  - HTML
  - 网站配色
  - 网页制作
id: 493
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 网站制作相关
date: 2016-09-17 14:17:40
---

大家在访问我博客和其它一些网站的时候会发现，如果你们用的手机版的chrome浏览器，就会发现，即使是在手机端，浏览器标题栏窗口的颜色也会随着网页主题配色改变。而一般手机浏览器工具栏窗口的颜色都是固定的，无法随网页配色改变。

改变浏览器工具栏颜色的作用只有一个，那就是让配色和网页看起来更加的和谐，美观。

[![screenshot_20160917-140845](http://115.159.197.66/wp-content/uploads/2016/09/Screenshot_20160917-140845-169x300.png)    ](http://115.159.197.66/wp-content/uploads/2016/09/Screenshot_20160917-140845.png)[![screenshot_20160917-140833](http://115.159.197.66/wp-content/uploads/2016/09/Screenshot_20160917-140833-1-169x300.png)](http://115.159.197.66/wp-content/uploads/2016/09/Screenshot_20160917-140833-1.png)

&nbsp;

实现方法非常简单，只需要在网站的head标签部分加入如下代码即可实现：
<pre class="lang:css decode:true">&lt;meta name="theme-color" content="#cc3333"&gt;</pre>
在content部分填入自己需要设置的颜色即可。

&nbsp;

&nbsp;