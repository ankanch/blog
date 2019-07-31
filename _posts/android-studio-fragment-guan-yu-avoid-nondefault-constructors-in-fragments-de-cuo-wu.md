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
date: '2015-09-04T17:52:47.000Z'
---

# Android Studio Fragment关于Avoid non-default constructors in fragments的错误

在android开发中，如果写了一个继承Fragment的类，那么在重载构造函数时，会提

示“_Avoid non-default constructors in fragments: use a default constructor plus_

_Fragment\#setArguments\(Bundle\) instead_”的错误。

这时。需要在类的前面加上**@SuppressLint\("ValidFragment"\)**才能解决错误。

## SuppressLint说明

指示编译器（？）应忽略的注释元素（即@SuppressLint（“”））指定的警告。

[官方文档：点击这里](http://developer.android.com/intl/zh-cn/reference/android/annotation/SuppressLint.html)

