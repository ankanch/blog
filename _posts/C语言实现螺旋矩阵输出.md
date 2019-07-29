---
title: C语言实现螺旋矩阵输出
tags:
  - C语言
  - C语言输出螺旋矩阵
  - 编程
  - 螺旋矩阵
id: 227
categories:
  - C++ / Visual C++
date: 2015-11-16 22:57:20
---

上周的C语言实验课，有一道选做题，叫我们输出n*n（n&lt;15）的<span style="color: #ff6600;">螺旋矩阵</span>，就像这样矩阵：

一个5*5的螺旋矩阵：

[![sm_print_1](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_1.png)](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_1.png)

<span style="color: #ff6600;">这里的讨论的矩阵比较特殊，因为是n*n的而不是n*j的</span>。初看这个题觉得挺简单的，但实际上做的时候还是费了些时间。

* * *

这里先讨论第一种方法吧，第二种方法在未来我会补上。

* * *

&nbsp;

## 法一：

第一种方法基本思路是：<span style="color: #993300;">在一个大的循环里分别用4个内嵌循环控制矩阵顶部行，右侧列，底部行，左侧列的输出。</span>

同时，我们要意识到，<span style="color: #993300;">在输出n为偶数或者n为奇数的对应螺旋矩阵的时候，最后一点会有些不同</span>，具体请看下面2张图：

（左侧为n=4，右侧为n=5）

[![sm_print_2](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_2.png)](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_2.png)[![sm_print_1](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_1.png)](http://139.129.6.122/wp-content/uploads/2015/11/sm_print_1.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

不难发现，在n为偶数的时候，最后一点循环那里，会把4个方向（顶部，底部，左边，右边）都循环一边。而当n为奇数的时候，最后一点那里，只有最中间一个数字了。所以针对这种情况，我们的解决方案是：当n为偶数的时候，最外层循环循环<span style="color: #ff6600;">n*n</span>次，当n为奇数的时候，最外层循环循环<span style="color: #ff6600;">n*n-1</span>次，并在最后，将最中间的那个数字（坐标为<span style="color: #ff6600;">x=y=(n-1)/2</span>）赋值为n*n。
<pre class="lang:c++ decode:true">        //用来根据n是偶数还是奇数来决定最外层循环次数
        if (n % 2 == 0)
	{
		loops = n*n;
	}
	else if (n % 2 != 0)
	{
		loops = n*n - 1;
	}
	//now start to fill the arrary
        .....此处代码省略.....
	//如果n为奇数，我们就单独设置最中间的值
	if (n % 2 != 0)
	{
		spi[(n - 1) / 2][(n - 1) / 2] = n*n;
	}</pre>
最主要，也是最关键的地方在于我们如何保证这里在顶部行输出后切换到右侧列，然后底部行，左侧列，再顶部行。对此，我用了一种比较笨的方法，（更棒的方法在未来会贴出，是用状态机），在一个循环n*n次或者n*n-1次的大循环里面，写4个小循环，分别来控制顶部行，右侧列，底部行，左侧列的输出。

循环输出螺旋矩阵的核心代码大概是这样的：
<pre class="lang:c++ decode:true ">       //now start to fill the arrary
       //rtop当前顶部行的位置，cright当前右侧列的位置，其它的我想我不用解释了
	for ( i = 1; i &lt;= loops; )
	{
		posp--;   //这个变量针对底部行，左侧列的输出控制
		//for the top-like raw
		rtop++;
		for ( j = rtop; j &lt; (xp+rtop); j++)   
		{
			spi[rtop][j] = i;
			i++;
			//printf("%d ", spi[rtop][j]);
		}

		//printf("n");
		if (i &gt; loops)
		{
			break;
		}

		//for the right-like column
		cright--;
		for ( j = rtop; j &lt; (xp+rtop); j++)   
		{
			spi[j][cright] = i;
			i++;
			//printf("%d ", spi[j][cright]);
		}

		//printf("n");
		if (i &gt; loops)
		{
			break;
		}

		//for the buttom-like raw
		rbuttom--;
		pb = posp;
		for (j = xp; j &gt;0; j--)
		{
			spi[rbuttom][pb] = i;
			i++;
			pb--;
			//printf("%d ", spi[rbuttom][j]);
		}

		//printf("n");
		if (i &gt; loops)
		{
			break;
		}

		//for the left-like raw
		cleft++;
		pb = posp;
		for (j =xp; j &gt;0; j--)
		{
			spi[pb][cleft] = i;
			i++;
			pb--;
			//printf("%d ", spi[j][cleft]);
		}

		//printf("n");
		if (i &gt; loops)
		{
			break;
		}

		//back-all processions
		xp -= 2;   //这个是记录每次输出多少个数字的
	}</pre>
&nbsp;

* * *

&nbsp;

这里就留给将来更新第二种方法----使用向量机的方式。最近学业繁重，恐怕是没时间了:(

* * *

&lt;kanch@11/16/2015@CUIT&gt;

&nbsp;