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
date: '2016-01-21T11:36:51.000Z'
layout: posting
---

# Ubuntu下Codeblocks编译C++并运行后控制台无法显示中文解决办法

在Ubuntu下用codeblocks编译C++程序并运行后可能会遇到不支持中文的情况

具体地说，运行后的界面会是下图这个样子：

![CB\_TERMINAL\_PROBLEM \(4\)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-4.png)

简单地说就是对中文支持不完整，看起来怪怪的

这是由于codeblocks默认的启动终端的问题

打开codeblocks的General Settings 菜单

找到 Terminal to launch console program

如下图示：

![CB\_TERMINAL\_PROBLEM \(3\)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-3.png)

把默认的xterm -T $TITLE -e修改掉

改为：**gnome-terminal -t** **$TITLE -x**

如下图所示：

[![CB\_TERMINAL\_PROBLEM \(1\)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-1.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-1.png)

然后我们再次编译程序并运行

现在可以正常显示了

[![CB\_TERMINAL\_PROBLEM \(2\)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-2.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-2.png)

另外，这个貌似只适用于Ubuntu12.04以上的版本

我的是Ubuntu15.10

[ ](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/CB_TERMINAL_PROBLEM-3.png)



{% include post_footer.md %}