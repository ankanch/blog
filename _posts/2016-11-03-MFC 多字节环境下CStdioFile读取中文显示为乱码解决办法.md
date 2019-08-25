---
title: MFC 多字节环境下CStdioFile读取中文显示为乱码解决办法
tags:
  - C++
  - CStdioFile
  - locale
  - MFC
  - setlocale
  - 中文乱码
  - 本地化
id: 593
categories:
  - C++ / Visual C++
date: '2016-11-03T10:25:12.000Z'
layout: posting
---

# MFC 多字节环境下CStdioFile读取中文显示为乱码解决办法

在MFC对话框工程中，如果选择了多字节工程，会导致`CStdioFile`读取文件内容的时候中文字符显示为乱码。而相同情况下`CFile`则不存在该问题。

在经过一番搜索后发现可以通过C++的本地化（[MSDN:setlocale](https://msdn.microsoft.com/en-us/library/x99tb11d.aspx)）来解决。方法如下：

在进行文件操作前先执行以下代码修改locale设置为中文：

```c++
char* old_locale = _strdup( setlocale(LC_CTYPE,NULL) ); setlocale( LC_CTYPE, "chs" );
setlocale( LC_CTYPE, old_locale ); 
free( old_locale );
//locale.h
```



{% include post_footer.md %}