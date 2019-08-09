---
title: Windows10下安装Ubuntu双系统之最简单的方法与部分引导修复
tags:
  - Ubuntu
  - Windows
  - Windows10
  - Windows下安装Ubuntu
  - 双系统
  - 系统安装
id: 348
categories:
  - Linux / Unix /虚拟主机 / VPS
date: '2016-01-18T20:41:12.000Z'
---

# Windows10下安装Ubuntu双系统之最简单的方法与部分引导修复

前段时间突然想起安装Ubuntu与Windows双系统，于是果断利用U盘安装了

结果，结果安装完毕后，悲剧的事情发生了：进不去Windows10了

然后网上各种方法试，都不管用，在无奈之下，只有备份硬盘数据，然后，把整个硬盘格式化了哈哈

今天突然又想安装Ubuntu与Widnwos双系统，不过幸好这次没手贱，安装成功了。当然，除了中间的一点小差错之外。

下面进入正题：

先说一下，我的电脑是 戴尔灵越7447（Dell Inspiron 14 7447）

首先我们要有一个U盘，4GB足以，然后呢，就是Ubuntu镜像了，建议14.10或者15，不要选14.04.1 LTS版本，会出错的。

接下里，我们把Ubuntu 14.10写入U盘中，具体教程请参考：

[如何在Windows下创建Ubuntu的启动U盘](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows)

如果你是Windows8/8.1/10的话，在开始正式安装之前，我们首先要关闭快速启动

控制面板-&gt;硬件和声音-&gt;电源选项 选择左边栏的【选择电源按钮功能】，然后关闭快速启动。

[![Ubuntu-0](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-0.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-0.png)

再利用Windows的磁盘管理分个分区出来，空闲分区，不！要！格！式!化!分区教程请参考：

[如何在 Windows 中对硬盘进行分区](https://support.microsoft.com/zh-cn/kb/944248)

然后，我们重新启动电脑，进入BIOS，设置从U盘启动。

注意：先**关闭Secure Boot**，再从U盘启动！其它的什么UEFI什么什么的都别管！这里我们只需要关闭Secure Boot即可！

![Ubuntu-33](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-33.png)

然后我们从U盘启动，你会看到这个画面：

![Ubuntu-12](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-12.png)

选择第一项，Try Ubuntu without Installing，_好吧，其实选第二个也是可以的。_

选择第一项后，看到的是如下画面，我们已经进入到ubuntu系统：

![Ubuntu-13](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-13.png)

接着，我们双击桌面上的 Install Ubuntu 14.10

在稍微的等待之后弹出以下窗口：当然，选择中文

![Ubuntu-14](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-14.png)

然后我们继续，接下来，你看到的画面可能是这样的：

**注意第一项**，如果是安装Ubuntu，与其它系统共存，恭喜你，请接着按照本教程做。

[![Ubuntu-2](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-2.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-2.png)

或者是这样的：

好吧，如果是下图所示的话，你还是选择其它选项吧，这个教程不适合你，你需要自己分区。。。。

[![Ubuntu-10](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-10.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-10.png)

后面的你就懂了吧，一直下一步，直到安装完成提示重新启动，好的，我们重新启动计算机。

## 如果你发现，你重新启动后直接进入了Windows，请继续向下阅读

这里就有一个小插曲了，原以为安装完成后重新启动就会弹出系统选单，看来，真的是我想多了

卧槽，直接进入了Windows，然而我们通过磁盘管理工具查看之前我们分出来的分区却发现，分区已经有数据了。

说明我们安装成功，但是，系统引导是个问题。

这里我也尝试了网上说的说明用EasyBCD自己添加grub的entry，我试过后不行，grub2也试过

sda0到sda11每个分区都挂了一遍，都不行。

不过好在后面琢磨出了方法：

接下来，我们重新启动系统，进入BIOS，别忘了拔出U盘

![Ubuntu-38](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-38.png)

上面是我修改后的BIOS设置，注意Secure Boot是关闭的！

接下来，我们选择File Browser Add Boot Option，会弹出下面这个东西，那是我的硬盘

![Ubuntu-34](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-34.png)

我们选择硬盘，接下来你会看到有个EFI文件夹，我们进入这个文件夹

[![Ubuntu-35](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-35.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-35.png)

接着，我们选择ubuntu这个文件夹

[![Ubuntu-36](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-36.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-36.png)

选择第二个，grubx64.efi，选择它后,BIOS应该会弹出个框框让你输入名字，你顺便输入个容易辨别的名字就行，比如grub

[![Ubuntu-37](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-37.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-37.png)接着，我们需要做的就是，把刚刚添加进去的那个东西设置为第一启动项，也就是如下图所示，把Grub移动到Boot Option \#1即可

![Ubuntu-38](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-38.png)

接下来我们保存对BIOS的修改，然后重新启动系统，卧槽，看见什么了------&gt;

Grub引导，反正我觉得比Windows Boot Manager好看。我们选择第一项，Ubuntu，看看可不可以进入系统

![Ubuntu-30](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-30.png)

果然进去了，好吧。让我们再重新启动，又回到上一张图片，如果你要切换回Windows的话，可以选择第三项，Windows Boot Manager，然后，你会得到最后一张图所示内容，

![Ubuntu-31](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-31.png)

这个就够熟悉了吧，我就不多说了。

![Ubuntu-11](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/01/Ubuntu-11.png)

双系统，在我看来，我现在还没有解决掉的**缺点**：在Ubuntu下，它把我Windows的所有分区，包括EFI分区，恢复分区都挂载上去了，目前我还没找到如何解决的方法。网上提到说，修改etc/fstab，我看别人的fstab里面的内容都有一大堆，我的fstab里面就3行，3行恰好包含完我给Ubuntu分的分区。。。。。

**&lt;转载请注明来源&gt;**

