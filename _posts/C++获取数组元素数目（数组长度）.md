---
title: C++获取数组元素数目（数组长度）
tags:
  - C++
  - C++数组
  - VC++
  - 数组
  - 数组长度获取
id: 180
categories:
  - C++ / Visual C++
date: 2015-10-04 21:16:42
---

C++不像Java和C#，C++语言没有提供获得数组长度的函数，但是对于字符串，提供了strlen用来获取字

符串字符数目。但是对于其它类型的数组我们如何获取长度呢？

我们以一个整形数组为例：

int ia[10];

<span style="color: #ff00ff;">**int len = sizeof(ia)/ia[0];**</span>

len即为该int数组ia的元素个数。

原因嘛是因为，sizeof(ia)是一个数组总共的字节数，而sizeof(ia[0])是一个元素占的字节数。所以相

除就是元素个数。

对此，我们可以利用c++的模版特性，写一个函数，可以用来获取任意类型数组的数组长度。代码如下：
<pre class="lang:c++ decode:true ">template&lt;class T&gt;
int GetArrayLength(T &amp; array)
{
    return ( sizeof(array)/sizeof(array[0]) );
}</pre>
注意：如果数组是new出来的，以上方法是无法使用的！需要这样：

<span style="color: #ff00ff;">**_msize(array)/sizeof(array[0]);**</span>

[有关_msize,请访问MSDN查阅](https://msdn.microsoft.com/en-us/library/aa298504?f=255&amp;MSPPError=-2147217396)