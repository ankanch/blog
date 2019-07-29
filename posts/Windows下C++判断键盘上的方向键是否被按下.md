---
title: Windows下C++判断键盘上的方向键是否被按下
tags:
  - C++
  - C++判断键盘按下
  - C++读取字符
  - 方向键判断
id: 197
categories:
  - C++ / Visual C++
date: 2015-10-19 23:56:56
---

&nbsp;

我在使用C++做一个贪吃蛇程序的时候，卡在了如何利用C++判断方向键这里。

我原本想的是：直接用<span style="color: #ff00ff;">getch()</span>判断按下按键的ASCII码是否为方向键的。可是我在[维基百科的ASCII页面](https://en.wikipedia.org/wiki/ASCII)上并没有找到 **↑ ↓ → ←** 几个按键的ASCII码。[在经过一番搜索后得到答案：http://bbs.csdn.net/topics/40312175](http://bbs.csdn.net/topics/40312175)  答案如下：
<pre class="lang:c++ decode:true ">#define VK_LEFT           0x25  //=37
#define VK_UP             0x26  //=38
#define VK_RIGHT          0x27  //=39
#define VK_DOWN           0x28  //=40</pre>
然后我在我的程序里用<span style="color: #ff00ff;">switch</span>语句<span style="color: #ff00ff;"> case</span>了 37，38，39，40.然而却发现，在windows下，这样不可用。

按下相应按键后根本没有反应。

然后我想到了输出下<span style="color: #ff00ff;">getchar()</span>得到的值，结果令我大吃一惊，输出值如下：

[![C++_dectect_dir](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/10/C-_dectect_dir.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/10/C-_dectect_dir.png)

&nbsp;

我们可以看到，每次按下方向键的时候，实际上是读入了2个数据，比如 <span style="color: #ff00ff;">_224n75_</span>代表的是左方向键（←）。

所以有了以下这个方法：先判断第一个读入的数据，再用<span style="color: #ff00ff;">getchr()</span>得到一次，这次再用switch语句判断。代码如下：
<pre class="lang:c++ decode:true ">//by Kanch
else if(kbdown == 224)
		{
			//pri-core code here
			//determine which action to perform
			kbdown = getch();    //due to  up/down/left/right no ASCII code,it print out as 224n75
			switch (kbdown)
			{
			case VK_LEFT:   //← pressed
				cout &lt;&lt; "left pressed" &lt;&lt; endl;
				break;
			case VK_UP:   //↑ pressed
				cout &lt;&lt; "up pressed" &lt;&lt; endl;
				break;
			case VK_RIGHT:   //→ pressed
				cout &lt;&lt; "right pressed" &lt;&lt; endl;
				break;
			case VK_DOWN:   //↓ pressed
				cout &lt;&lt; "down pressed" &lt;&lt; endl;
				break;
			default:
				break;
			}
		}</pre>
&nbsp;

这样，我们便用C++实现了判断方向键是否被按下。

**&lt;转载请注明出处&gt;**