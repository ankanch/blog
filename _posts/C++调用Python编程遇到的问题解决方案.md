---
title: C++调用Python编程遇到的问题解决方案
tags:
  - C++
  - C++调用Python
  - C++调用Python出错
  - python
  - 编程
  - 解决问题
  - 调试
id: 512
categories:
  - C++ / Visual C++
  - Linux / Unix /虚拟主机 / VPS
  - Python
date: 2016-09-25 23:59:12
---

最近在研究C++调用Python脚本，照着网上的教程做了一遍，应为我是ubuntu系统，所以，写完代码后，第一关编译就遇到了困难。

报错提示如图：

![2016-09-25-14-32-55](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-32-55.png)

大概意思是没有找到Python.h文件，WTF？？？？我系统上有python2.6和python3.5，怎么会没有Python.h这个文件呢。后面发现，这样include貌似默认会去Python2.6的目录寻找Python.h，然而我用的Python3.5，所以我吗需要安装Python3.5的dev包，命令如下：
<pre class="lang:c++ decode:true">sudo apt-get install python3-dev</pre>
[![2016-09-25-14-35-05](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-35-05.png)](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-35-05.png)

然后我又编译了一次，这次终于找到了Python.h头文件，但是又出现了新的错误，如下图所示，提示：PyString_FromString未声明，在网上查到，在Python3k之后，PyString_FromString全部变成了PyBytes_FromString，所以我们只需要将该函数替换为：PyBytes_FromString即可。

[![2016-09-25-14-34-21](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-34-21.png)](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-34-21.png)

接下来，我们使用以下指令编译该源文件，其中，-I参数指定了python include 库的位置，-L指定了python动态链接库的位置。
<pre class="lang:sh decode:true">g++ -o gt cppCallPython.cpp -I/usr/include/python3.5/ -L/u
sr/lib/python3.5 -lpython3.5</pre>
[![2016-09-25-14-50-37](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-50-37.png)](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-14-50-37.png)

不幸的是，又报错了，这次错误如上图所示，提示我们ld无法找到lpython这个程序。

在Google一番后，我发现通过以下命令可以获得更加详细的结果，提示具体哪些文件出问题了：
<pre class="lang:sh decode:true">sudo ld -lpython3.5 --verbose</pre>
[![2016-09-25-15-47-48](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-15-47-48.png)](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-15-47-48.png)

从上图请我们可以看到，ld无法正确的获取python相关的很多库文件，看到这么多文件，讲真，我也懵逼了，卧槽，这可怎么办，同样的，网上给出的最佳解决方法是一个一个去创建符号链接，卧槽，可是这么多啊！

无可奈何，我只有用ln -s准备一个一个开始创建符号链接。

可是我们要在那里去找那些文件的具体路径呢？

通过以下命令可以获得一个库文件的具体目录：
<pre class="lang:sh decode:true ">locate libpython3.5.so

sudo ln -s /usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/libpython3.5.so</pre>
![2016-09-25-15-48-27](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-15-48-27.png)

然后，我先对第一个文件创建了符号链接，然后尝试编译了下，发现，卧槽，居然成功了！！！

居然只创建了一个符号链接就成功了！！

然后，我们再次进行编译，你会发现，已经可以编译成功了。

[![2016-09-25-15-52-50](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-15-52-50.png)](http://115.159.197.66/wp-content/uploads/2016/09/2016-09-25-15-52-50.png)

然后就可以愉快的运行自己的C++调用Python的程序了

&nbsp;