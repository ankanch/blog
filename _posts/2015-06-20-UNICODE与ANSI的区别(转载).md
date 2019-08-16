---
title: UNICODE与ANSI的区别(转载)
tags:
  - _T("")
  - ANSI
  - C++
  - Unicode
id: 66
categories:
  - C++ / Visual C++
  - 转载
date: '2015-06-20T13:19:28.000Z'
layout: posting
---

# UNICODE与ANSI的区别(转载)

**VC6.0下默认的是ANSI编码方式，而vs2005及以上版本中默认的是**[**Unicode**](https://zh.wikipedia.org/wiki/Unicode)**编码方式。**这里简单解释下这两种编码方式。

ANSI本来是美国的国家标准，后来渐渐通行于世。**标准的ANSI字符一共有128个，后来扩充到255个，而ANSI使用8位（1个字节）标识每个字符，最多也只能表示255个字符。C++中的char类型就是用来储存ANSI编码的字符的。**char类型有signed char 和unsigned char两种，默认的char是有符号的signed char ，可以表示的字符编码范围是-128~127，无符号的unsigned char可以表示0~255. 也就是说，ANSI只能表示最多256个字符（即ASCII值为0-255之间的字符），每个字符用一个字节的空间来存储，对于英文，的确足够，可是对于亚洲地区的复杂语言，这是远远不够的。因此，为了统一一个全世界都可以使用的字符编码，[Unicode](https://zh.wikipedia.org/wiki/Unicode)产生了。

[**UNICODE**](https://zh.wikipedia.org/wiki/Unicode)**可以表示65,536(2的16次方)个字符，囊括了世界上所有的字符，每一个字符都有一个单一的**[**UNICODE**](https://zh.wikipedia.org/wiki/Unicode)**值，当然也包括ANSI码表示的字符**.

**在VC中定义了** **_T("") 宏来表示UNICODE字符串，但在ANSI模式下 _T("") 不起任何作用。**

不同的是：

ANSI字符只占用一个字节，UNICODE会自动在ANSI值后加入一个值为0的字节。 简单的来说，通常Unicode使用两个字节表示每个字符，即每个字符为16位二进制长度。而ANSI编码使用一个字节表示每个字符，即8个二进制位。 **在Windows的API函数中，每一个涉及到了字符串传递的函数，如最基本的MessageBox（用来显示一个消息框），都有两个版本**,MessageBoxA和MessageBoxW，前者是ANSI版本，后者是宽字符版本，通常就是UNICODE。 **C++中的char是对应ANSI字符的，C++中还有一个基本类型wchar_t就是对应UNICODE字符的。** 编程的时候应该首先决定使用更加通用的宽字符UNICODE，还是占用空间较少的ANSI，个人认为应用软件可以使用UNICODE好一些。



{% include post_footer.md %}