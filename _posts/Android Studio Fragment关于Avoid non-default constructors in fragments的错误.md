---
title: 'Android Studio Fragment:关于Avoid non-default constructors in fragments的错误'
tags:
  - android studio
  - Android开发
  - android构造函数错误
  - fragment
  - non-default constructors
id: 135
categories:
  - Android开发 / Android Studio
date: 2015-09-04 17:52:47
---

在android开发中，如果写了一个继承Fragment的类，那么在重载构造函数时，会提

示“<span style="color: #808000;">_Avoid non-default constructors in fragments: use a default constructor plus_</span>

<span style="color: #808000;">_Fragment#setArguments(Bundle) instead_</span>”的错误。

这时。需要在类的前面加上<span style="color: #ff00ff;">**@SuppressLint("ValidFragment")**</span>才能解决错误。

&nbsp;

# SuppressLint说明

指示编译器（？）应忽略的注释元素（即@SuppressLint（“”））指定的警告。

[官方文档：点击这里](http://developer.android.com/intl/zh-cn/reference/android/annotation/SuppressLint.html)

&nbsp;