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
date: 2016-11-03 10:25:12
---

在MFC对话框工程中，如果选择了多字节工程，会导致CStdioFile读取文件内容的时候中文字符显示为乱码。而相同情况下CFile则不存在该问题。

在经过一番搜索后发现可以通过C++的本地化（[MSDN:setlocale](https://msdn.microsoft.com/en-us/library/x99tb11d.aspx)）来解决。方法如下：

在进行文件操作前先执行以下代码修改locale设置为中文：
<pre class="lang:c++ decode:true">char* old_locale = _strdup( setlocale(LC_CTYPE,NULL) );
setlocale( LC_CTYPE, "chs" );</pre>
在文件操作完毕后，再执行以下代码恢复locale设置：
<pre class="lang:c++ decode:true ">setlocale( LC_CTYPE, old_locale );
free( old_locale );</pre>
**注意**，你需要引用以下头文件：
<pre class="">locale.h</pre>
详细请参考[MSDN：https://msdn.microsoft.com/en-us/library/x99tb11d.aspx](https://msdn.microsoft.com/en-us/library/x99tb11d.aspx)