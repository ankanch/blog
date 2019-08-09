---
title: Windows MFC C++ socket与Linux Python Socket交互接收乱码问题
tags:
  - C++
  - Linux
  - MFC
  - python
  - socket
  - utf-8
  - Windows
  - 乱码
  - 编码
id: 580
categories:
  - C++ / Visual C++
  - Linux / Unix /虚拟主机 / VPS
  - Python
date: '2016-10-27T20:33:19.000Z'
---

# Windows MFC C++ socket与Linux Python Socket交互接收乱码问题

最近在写一个爬虫项目，要用到Ubuntu服务器上运行的Python服务器与Windows上的管理端交互。

正常的来说，都是简单的几句socket send/recv实现，编码问题理论上讲应该是不用担心的。

但在Python脚本端的send里面，我编码成了utf-8编码，而windows默认为UNICODE，结果导致了无论是中文还是英文，Python 服务器端接收正常但windows端却一直是乱码。

解决方法主要是利用\[MultiByteToWideChar\]\([https://msdn.microsoft.com/en-us/library/windows/desktop/dd319072\(v=vs.85\).aspx\)（点击可跳转到MSDN）函数，将UTF-8转换成UNICODE](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319072%28v=vs.85%29.aspx%29（点击可跳转到MSDN）函数，将UTF-8转换成UNICODE)

封装后的函数如下：

```
//这段代码在MFC环境中正常 wchar_t * UTF8ToUnicode( const char* str ) { int textlen = 0; wchar_t * result; textlen = MultiByteToWideChar( CP_UTF8, 0, str,-1, NULL,0 );  
result = (wchar_t *)malloc((textlen+1)*sizeof(wchar_t));  
memset(result,0,(textlen+1)*sizeof(wchar_t));  
MultiByteToWideChar(CP_UTF8, 0,str,-1,(LPWSTR)result,textlen );  
return result;  
}
```

同理，下面的函数实现了UNICODE到UTF-8的转换：

```
char * CKCCDlg::UnicodeToUTF8(const wchar_t *str) { char * result; int textlen = 0; // wide char to multi char textlen = WideCharToMultiByte(CP_UTF8, 0, str, -1, NULL, 0, NULL, NULL); result = (char *)malloc((textlen + 1) * sizeof(char)); memset(result, 0, sizeof(char) * (textlen + 1)); WideCharToMultiByte(CP_UTF8, 0, str, -1, result, textlen, NULL, NULL); return result; }
```

