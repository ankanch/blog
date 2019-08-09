---
title: Visual Studio2015 MFC连接Access数据库
tags:
  - Access
  - MFC
  - MFC数据库
  - MFC连接Access数据库
  - Visual C++
  - Visual Studio
  - VS2015数据库
  - 数据库
id: 416
categories:
  - C++ / Visual C++
date: '2016-05-05T23:25:02.000Z'
---

# Visual Studio2015 MFC连接Access数据库

我选的工程实践题目要求用数据库。在网上查了查MFC使用数据库，发现大多数都是在VC6.0的情况下使用，用的也是Access2010或者之前的版本。而我的环境是VS2015 + Access 2013。所以写下这篇文章备用。

我们讨论的是连接到已经存在的Access 2013数据库。

首先我们需要在MFC对话框的stdafx.h头文件中包含afxdb.h文件，该文件提供了数据库操作

//下面这句代码要加在\#include &lt;afxcontrolbars.h&gt; // 功能区和控件条的 MFC 支持之下 //添加数据库支持

## include &lt;afxdb.h&gt; //新加入头文件，用于CDatabase类&lt;/pre&gt;

然后，我们需要导入msado15.dll，该文件与数据库参数有关，未ADO组件，用于连接数据库

//msado15.dll我是复制到了项目文件夹下 //它的默认路径应该是C:\Program Files\Common Files\System\ado

## import "msado15.dll"  no\_namespace  rename\("EOF","adoEOF"\)&lt;/pre&gt;

接下来就是连接数据库了。

我们先声明 2个变量，一个是\_ConnectionPtr类型，另外一个是\_RecordsetPtr类型。

\_ConnectionPtr是用来connection对象，主要用于数据库的连接，SQL命令执行相关操作

\_RecordsetPtr是用来是用来对返回的记录集进行操作的

```
_ConnectionPtr m_pConnection;//连接access数据库的链接对象 _RecordsetPtr m_pRecordset;//记录集对象
//连接数据库 try { CoInitialize(NULL); m_pConnection = _ConnectionPtr(__uuidof(Connection)); m_pConnection->ConnectionString = _T("Provider=Microsoft.ACE.OLEDB.12.0;\ Data Source=X:\\MetroData\\StationData.accdb;");//这里照着老版的书上写Provider=Microsoft.Jet.OLEDB.4.0;Data //Source= MyAccess.mdb是不对的，这样写只适合2007版以前的access，且路径里面的\必须改成 m_pConnection->Open("", "", "", adConnectUnspecified); } catch (_com_error e) { AfxMessageBox(_T("数据库连接失败！")); return FALSE; }
```

### **注意：**

如果提示 【_'Microsoft.ACE.OLEDB.12.0'提供者未注册】_ 错误，请[下载Microsoft Access Database Engine 2010 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=13255)

如果连接失败，你可能需要在MFC对话框的App类的构造函数CXXX::CXXXApp\(\)中添加AfxOleInit\(\);用于初始化。

