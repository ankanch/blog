---
title: matplotlib饼状图(pie)不能正确显示中文的解决办法
tags:
  - matplotlib
  - matplotlib绘图
  - pie
  - pie图
  - python
  - python数据分析
  - python数据挖掘
  - tieba-zhuaqu
  - 数据分析
  - 统计图
  - 饼状图
id: 623
categories:
  - Python
date: '2016-11-27T16:15:02.000Z'
---

# matplotlib饼状图\(pie\)不能正确显示中文的解决办法

还是之前那个[tieba-zhuaqu](https://github.com/ankanch/tieba-zhuaqu)项目，在使用matplotlib绘制饼状图（pie）的时候，发现不能显示中文。

[![1480233742985screencapture](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/11/1480233742985screencapture.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/11/1480233742985screencapture.png)

（[图片源地址：https://my.oschina.net/Kanonpy/blog/617535?p=1](https://my.oschina.net/Kanonpy/blog/617535?p=1)）

之前使用matplotlib绘制其它类型的图片的时候也发现不能显示中文，最后的解决办法都是使用FontProperties\(\) 来设置字体解决问题。

然而发现饼状图貌似不不能简单的通过在plt.pie（）中传入FontProperties\(\) 解决中文乱码的问题。

后面在[https://my.oschina.net/Kanonpy/blog/617535?p=1](https://my.oschina.net/Kanonpy/blog/617535?p=1)找到了解决办法，以及出现这个问题的原因。

在调用pie\(\)函数的时候，它会返回字体对象。而且返回的字体对象不支持中文字体。

根据那篇文章里的说法，我们只需要修改pie（）返回的字体对象即可，即将它返回的对象修改为支持中文的字体。

```
patches,l_text,p_text = plt.pie(ValueList, labels=Labels, colors=colors,autopct='%1.1f%%',explode=explode ,shadow=True, startangle=90) for font in l_text: font.set_fontproperties(FontProperties(fname=PATH_SUFFIX+'SIMLI.TTF')) plt.title(graphicTitle,fontproperties=font_set,y=1.05)
#重要全局变量 PATH_SUFFIX = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) PATH_SUFFIX+="\\userX\\" #插件根目录
```

这样，我们便可以正常显示中文字体了。

[![&#x7528;&#x6237;&#x7EF4;&#x5EA6;&#x6570;&#x636E;&#x5206;&#x6790;-&#x4E92;&#x52A8;&#x5BC6;&#x5207;&#x7528;&#x6237;&#xFF08;&#x5F02;&#x5E38;&#xFF09;](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/11/用户维度数据分析-互动密切用户（异常）.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/11/用户维度数据分析-互动密切用户（异常）.png)

关于在哪里寻找字体：

windows下字体路径：

**C:\Windows\Fonts**

Ubuntu下字体路径：

**/usr/share/fonts**

