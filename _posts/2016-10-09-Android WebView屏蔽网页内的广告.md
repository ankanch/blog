---
title: Android WebView屏蔽网页内的广告
tags:
  - android studio
  - Android开发
  - HTML元素
  - Java
  - Java Script
  - JS
  - WebView
  - 屏蔽广告
id: 551
categories:
  - Android开发 / Android Studio
date: '2016-10-09T19:56:03.000Z'
layout: posting
---

# Android WebView屏蔽网页内的广告

最近在做一个新闻聚合应用，类似与RSS。聚合新闻标题，当用户点击后，在应用内（或应用外）打开新闻。

然后，就发现有些站点居然广告掺不忍睹。。。。

[![screenshot_20161009-202650](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202650-169x300.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202650.png)[![screenshot_20161009-202659](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202659-169x300.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202659.png)

所以，开始研究如何屏蔽广告，这样才可以让应用更加的美观。

在网上查了一番后，发现可以通过注入Java Script代码，来实现对指定元素的过滤（隐藏或者删除，分别讲这两种，接下来）

## 法1：通过seletor来隐藏标签。

首先，我们需要获取指定元素的seletor，获取方法如下图（右键新窗口打开，查看大图）：

Chrome浏览器中F12打开开发者工具，然后右键菜单，copy，copy seletor就可以获得一个唯一的seletor

[![222](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/222-1024x576.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/222.png)

获取到seletor后，我们对WebView重写onPageFinished函数，加入以下代码：

下面的代码将Java Script注入到webView中，然后，通过这个seletor去寻找相应的元素，并处理。

wv.setWebViewClient(new WebViewClient(){

```java
        @Override
        public void onPageFinished(WebView view, String url) {
                //屏蔽百度嵌入广告
                view.loadUrl("javascript:function setTop(){document.querySelector('#BAIDU_SSP__wrapper_u2578965_0').style.display=\"none\";}setTop();");
        }
    });
```

然后，我们再打开网页，就会发现，在网页加载完成后，广告就会自动去掉。

## 法2：直接删除标签

通过以下代码，并传入HTML元素的ID值，即可实现直接删除标签：

```java
view.loadUrl("javascript:var con = document.getElementById('gamesliderwrap'); con.parentNode.removeChild(con); ");
```

[![screenshot_20161009-202817](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202817-169x300.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202817.png) [![screenshot_20161009-202822](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202822-169x300.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-202822.png)

## 写在最后：

由于上面的方法都是在页面加载完成后再注入Java Script代码，再进行广告屏蔽的。

这样，用户还是会先看到广告，所以，我建议在页面加载完成前，显示另外一个fregment提示正在加载，或者直接隐藏WebView，等到页面加载完成后再显示。如下图：

[![screenshot_20161009-210540](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-210540-169x300.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/Screenshot_20161009-210540.png)

也可以在onPageStart中写While循环，来循环执行Java Script注入代码。这样HTML元素一显示，就会被处理掉。



{% include post_footer.md %}