---
title: Word文档丢失找回
tags:
  - word
  - word文档
  - word断电恢复
  - 计算机
id: 37
categories:
  - C++ / Visual C++
date: 2015-06-16 22:25:45
---

当遇到突然停电，电脑的文档还没有保存，怎么办?

其实在你编辑的时候，系统会将编辑中的文档暂时放在“<span style="color: #ff00ff;">C:\Documents and settingsAdministratorApplication DataMicrosoftWord</span>"当中，（**其中Administrator是指你的用户名**），你只要将那些扩展名为<span style="color: #ff00ff;">.asd</span>的文件用Word逐一打开，就能够找到刚才写的文档了。

同时你也可以将Word文档的自动保存时间缩短，打开“Word选项”，将“保存自动回复信息时间间隔”改为很短的时间,比如1分钟，这样能够将损失降到最小。