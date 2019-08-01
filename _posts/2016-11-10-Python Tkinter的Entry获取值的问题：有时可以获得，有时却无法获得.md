---
title: Python Tkinter的Entry获取值的问题：有时可以获得，有时却无法获得。
tags:
  - Entry控件
  - python
  - Python GUI
  - Python编辑框
  - StringVar()
  - Tkinter
id: 599
categories:
  - Python
date: '2016-11-10T11:47:26.000Z'
---

# Python Tkinter的Entry获取值的问题：有时可以获得，有时却无法获得

最近再写一个数据分析模块，由于命令行界面太难看，所以需要GUI，于是采用了Python自带的[Tkinter（官方文档）](https://wiki.python.org/moin/TkInter/)。界面上的话，还是挺好看的，而且可移植性强。

由于这个模块需要输入，故我们需要一个编辑框，上网查了下，Tkinter中的编辑框叫做Entry。

[Entry简要说明：http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Entry.html](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Entry.html)

现在有了Entry，接下来，我们就是要获取Entry里面的数据了。

简单的在网上查了下，大家可以发现，几乎全都是一个方法：

关联一个StringVar，然后通过这个StringVar来获取/修改值。

如下：

def btnclick\(\): root.update\(\) word = data.get\(\) \#获取Entry的值

data = StringVar\(root\) Label\(root,text="请输入要分析的词语（仅一个）:",width=25,height=2\).pack\(\) Entry\(root,text="请输入内容",width=25,textvariable=data\).pack\(ipadx=4,ipady=4\) Button\(root, text="获取edit内容", width=15,relief=GROOVE,command=btnclick\).pack\(pady=16,ipadx=8,ipady=8\)&lt;/pre&gt; 当时发现居然这么简单，然后赶紧就照着网上的代码做了。做了之后发现，这个代码，有些时候可以正确获得值，有些时候又不能正确获得，StringVar的get返回空字符串。

这个问题，，，简直 -\_- ....想在网上查都不知道应该搜索什么。迷醉。

不过在经过我大力的搜索，与排查问题后，还是找到了解决方案，如下：

简单地讲，就是直接调用Entry的get方法，而不是通过与entry关联的StringVar\(\)来获取值。

如下：

def btnclick\(\): root.update\(\) word = wordentry.get\(\) \#调用Entry的get方法获得数据

Label\(root,text="KCC数据分析模块 - 基本分析套件\n该模块用于显示指定词语的时间频率关系图",width=35,height=5\).pack\(\) Label\(root,text="请输入要分析的词语（仅一个）:",width=25,height=2\).pack\(\) wordentry = Entry\(root,text="请输入内容",width=25,textvariable=data\) \#给entry来个名字 wordentry.pack\(ipadx=4,ipady=4\) Button\(root, text="获取edit内容", width=15,relief=GROOVE,command=btnclick\).pack\(pady=16,ipadx=8,ipady=8\)&lt;/pre&gt; 通过调用Entry的get方法来获取变量，经过测试：这种方法每一次均可正确获得。

[参考资料：NMT Tkinter教程 http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)

[参考2：StackOverFlow](http://stackoverflow.com/questions/10727131/why-is-tkinter-entrys-get-function-returning-nothing)

