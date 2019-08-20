---
title: VC++中Unicode下CString转char*
tags:
  - C++类型转换
  - MFC
  - MFC数据库
  - Visual C++
  - Visual Studio
id: 423
categories:
  - C++ / Visual C++
date: '2016-05-11T22:12:46.000Z'
layout: posting
---

# VC++中Unicode下CString转char

在进行数据库编程的过程中，需要把`variant_t`类型转换成`char`尝试了各种方法，最后发现把它转换成`CString`，再由`CString`转换成`char`比较简单。

这里我们说的利用宏T2A和W2A进行转换。

顾名思义，T2A是从wchar_t_到char_的转换；W2A是由宽字符到ANSI字符之间的转换。

转换方式如下，首先需要声明标识符：`USES_CONVERSION`，然后我们在利用这2个宏进行数据类型转换

代码如下：

```c++
//UNICODE下的CString转char* USES_CONVERSION; 
strcpy_s(tsc.staname,W2A((LPCTSTR)vname.lVal)); 
strcpy_s(tsc.parentline, W2A((LPCTSTR)vparent.lVal));
W2A((LPCTSTR)vname.lVal);

USES_CONVERSION;
CString cstr = _T("12345"); 
char _pbuffer = T2A(cstr);  
char_ pbuf = W2A(cstr);
```



{% include post_footer.md %}