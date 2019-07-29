---
title: Android Studio TextView添加滚动条，解决文字过多问题
tags:
  - android studio
  - Android开发
  - TextView
  - TextView滚动条
id: 95
categories:
  - Android开发 / Android Studio
date: '2015-07-21T17:43:26.000Z'
---

# Android Studio TextView添加滚动条，解决文字过多问题

在使用TextView的过程中，有时候会遇到文字过多，显示不全的问题。

下面的几行代码，可以给TextView加上滚动条。

首先，打开layout文件，在TextView标记中添加2个属性：

```
android:singleLine="false" //取消单行 android:scrollbars="vertical" //设置垂直滚动条
```

利用TextView对象设置样式

```
TextView textview=(TextView)findViewById(R.id.textview); textview.setMovementMethod(ScrollingMovementMethod.getInstance());
```

