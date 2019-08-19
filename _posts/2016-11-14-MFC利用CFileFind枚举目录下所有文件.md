---
title: MFC利用CFileFind枚举目录下所有文件
tags:
  - C++
  - CFileFind
  - MFC
  - VC++
  - 列举文件
  - 枚举文件
id: 606
categories:
  - C++ / Visual C++
date: '2016-11-14T18:32:47.000Z'
layout: posting
---

# MFC利用CFileFind枚举目录下所有文件

最近在写[贴吧分布式爬虫系统（https://github.com/ankanch/tieba-zhuaqu）](https://github.com/ankanch/tieba-zhuaqu)的用户管理端程序。为了保证高度可扩展性，在该程序的数据分析部分，引入了插件机制。这样日后需要拓展功能的时候只需要不断的增加插件（由于插件是python写的，所以我们只需要用C++调用cmd执行python插件就行。如果需要UI，也可以使用python自带的Tkinter实现。）

这样，便通过C++与python结合的方式，完成了用户管理端程序。

该程序所引入的插件机制非常简单，因为插件是用python脚本完成的，所以我们只需要让我们的C++程序找到python脚本，并且执行即可。

这样就涉及到一个问题，那就是如何令MFC程序列举出当前一个子目录下的所有文件。一旦实现这个，我们基本也就完成了插件的加载功能。

还是上网查，查如何解决，在试了一系列的方法后，找到了一个叫做[CFileFind类](https://msdn.microsoft.com/library/9990068c-b023-4114-9580-a50182d15240.aspx#cfilefind__findfile)。然后去MSDN查这个类的用法，我们可以发现，MSDN指出：

```
执行本地文件搜索和是 CGopherFileFind 和 CFtpFileFind的基类，执行Internet文件搜索。
```

接下来我们讲讲如何使用这个类，从MSDN查询我们可以发现，我们主要需要以下几个函数：

CFileFind::Close

关闭搜索请求。

CFileFind::FindFile

搜索一个目录一个指定的文件名。

CFileFind::FindNextFile

继续以前的文件搜索调用 FindFile。

 </tr>

CFileFind::GetFileName

获取名称，包括扩展，找到的文件

CFileFind::IsDirectory

确定找到的文件是否为内容。

CFileFind::IsDots

确定找到的文件的名称是否具有名称“”。或者“。”，指示实际上是内容。

 </tr> </tbody> </table> [（内容来源：MSDN：https://msdn.microsoft.com/library/9990068c-b023-4114-9580-a50182d15240.aspx#cfilefind__findfile）](https://msdn.microsoft.com/library/9990068c-b023-4114-9580-a50182d15240.aspx#cfilefind__findfile)

那么如何搜索呢？

根据MSDN上的例子，我们在第一次查找的时候，首先需要给其传入一个路径，指明在哪里查找该文件。

```
//下面的代码传入当前exe文件同目录下的plugins文件夹路径->kanch CFileFind finder; BOOL bWorking = finder.FindFile(_T(".\\plugins\*.*"));
```

代码像下面这样：

```
while (bWorking) { bWorking = finder.FindNextFile(); if (finder.IsDots()) continue; //跳过.. CString foldername = (LPCTSTR)finder.GetFileName(); //得到文件名 //MessageBox(foldername); if (finder.IsDirectory()) { //如果是路径 } else { //如果是文件 } }
```

以上代码在Visual Studio 2015中编译通过。

参考：[MSDN CFileFind类：https://msdn.microsoft.com/library/9990068c-b023-4114-9580-a50182d15240.aspx#cfilefind__findfile](https://msdn.microsoft.com/library/9990068c-b023-4114-9580-a50182d15240.aspx#cfilefind__findfile)



{% include post_footer.md %}