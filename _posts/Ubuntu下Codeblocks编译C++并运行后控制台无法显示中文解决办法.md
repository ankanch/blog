---
title: Ubuntu下Codeblocks编译C++并运行后控制台无法显示中文解决办法
tags:
  - C++
  - Codeblocks
  - Ubuntu
  - 控制台
  - 终端
  - 终端不显示中文
id: 371
categories:
  - C++ / Visual C++
  - Linux / Unix /虚拟主机 / VPS
date: 2016-01-21 11:36:51
---

&nbsp;

在Ubuntu下用codeblocks编译C++程序并运行后可能会遇到不支持中文的情况

具体地说，运行后的界面会是下图这个样子：

![CB_TERMINAL_PROBLEM (4)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-4.png)

简单地说就是对中文支持不完整，看起来怪怪的

这是由于codeblocks默认的启动终端的问题

打开codeblocks的General Settings 菜单

找到 Terminal to launch console program

如下图示：

![CB_TERMINAL_PROBLEM (3)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-3.png)

把默认的<span style="color: #000000;">xterm -T $TITLE -e</span>修改掉

改为：**<span style="color: #ff00ff;">gnome-terminal -t $TITLE -x</span>**

如下图所示：

[![CB_TERMINAL_PROBLEM (1)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-1.png)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-1.png)

然后我们再次编译程序并运行

现在可以正常显示了

[![CB_TERMINAL_PROBLEM (2)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-2.png)](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-2.png)

另外，这个貌似只适用于Ubuntu12.04以上的版本

我的是Ubuntu15.10

[
](http://115.159.197.66/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-3.png)