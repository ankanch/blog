---
title: 加速Android Studio的Gradle构建速度
tags:
  - android
  - android studio
  - Android开发
  - Gradle
  - 加快Gradle
  - 加快Gradle构建
id: 138
categories:
  - Android开发 / Android Studio
date: '2015-09-06T20:43:24.000Z'
layout: posting
---

# 加速Android Studio的Gradle构建速度

在利用Android Studio做项目时，发现随着项目内资源的逐渐增多（或者项目创建时间太过久远，而又未经常打开），Android Studio的build速度也越来越慢。（P.S.在做我的CSGO StatTrak的时候，基本要12分钟，才能build完成，在此期间，一直显示Gradle运行中....）

在互联网上一番搜索后，发现通过以下方法可以加快Gradle的构建速度。

在以下Gradle目录创建gradle.properties文件

*     `C:Users<username>.gradle` 

  并在文件中增加以下数据，然后保存。

  org.gradle.daemon=true

  org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8

  org.gradle.parallel=true

  org.gradle.configureondemand=true&lt;/pre&gt;

  ![speedup\_gradle\_3](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/09/speedup_gradle_3.png)

注意，因为这样配置是对于此计算机的Android Studio用户，所以对于所有项目都有效。

不过最好把Android Studio的配置也改改，打开Android Studio，选择菜单项 File-&gt;Settings。

切换到下面的视图：

把 Offline Work打上勾。

[![speedup\_gradle\_1](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/09/speedup_gradle_1.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/09/speedup_gradle_1.png)

再切换到如下视图：

把下图黄色箭头指出的选项弄成一样

[![speedup\_gradle\_2](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/09/speedup_gradle_2.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/09/speedup_gradle_2.png)

最后，保存，并重新打开Android Studio.

不出意外，前面操作都正确的话，你现在Gradle应该有了很大的提升。

我在怎样修改后，每次Gradle构建，只要40秒左右，比以前的12分钟，快多了。



{% include post_footer.md %}