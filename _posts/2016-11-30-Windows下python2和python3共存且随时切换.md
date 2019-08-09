---
title: Windows下python2和python3共存且随时切换
tags:
  - py
  - py.exe
  - python
  - python2
  - python23共存
  - python3
  - Windows
id: 634
categories:
  - Python
date: '2016-11-30T22:50:23.000Z'
---

# Windows下python2和python3共存且随时切换

最近在使用Google App Engine，然后自己准备部署个python爬虫部署在GAE上面，然后开始跟着谷歌的教程创建hello world程序。完毕后，想到，自己只需要稍微修改下谷歌的代码，然后在默认的main.py里面添加路由，调用自己的函数即可。

当然要修改代码，必须得先下载代码才行，但是谷歌给出的脚本为python2的脚本，并没有python3的脚本。虽然我们已经知道通过[3to2](https://wiki.python.org/moin/3to2)可以转换python3代码到python2。但是这是不得已才会使用的方法，所以最好的办法仍然是使用python2来运行。

那么，就需要python2和python3在windows上共存了。

（修改exe程序名字是可以实现的，但是这样的话，pip就会出错。）

不过，后面在python官网上找到了解决方案

实现，我们需要安装python2（安装完毕后不要加入到PATH里面。）

然后python3内置了py.exe 通过这个程序，我们可以选择使用哪个python版本来运行脚本

下面的代码展示了分别用python2和python3运行脚本：

\#使用python2运行h.py py -2 k.py

## 使用python3运行h.py

py -3 k.py &lt;/pre&gt; 如果觉得这样太麻烦，可以通过在源代码文件第一行添加：

```
#! python3
#! python2
```

然后我们只需要：

```
py h.py
```

关于不同版本之间pip的使用：

使用如下命令即可运行指定版本的pip：

py -2 -m pip install XXX

py -3 -m pip install XXX&lt;/pre&gt;  

