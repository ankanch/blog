---
title: JavaScript实现HTML Input标签的智能提示框
tags:
  - HTML
  - input
  - JavaScript
  - 智能提示
id: 576
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 网站制作相关
date: '2016-10-22T23:32:07.000Z'
---

# JavaScript实现HTML Input标签的智能提示框

实现智能提示编辑框。

当用户在输入的时候，根据用户输入内容，自动补全可能内容。效果如下图：

[![111](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/111.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/111.png)

主要通过JavaScript来获取服务器更新，然后通过JavaScript向input对应的一个&lt;datalist&gt;&lt;/datalist&gt;添加&lt;options&gt;&lt;/options&gt;元素实现。（需要input响应oninput），input以及对应的datalist代码如下：

```
<input class="form-control" id="focusedInput_name" type="text" onkeydown="javascript:keydown();" oninput="javascript:showautofill()" list="word"> <datalist id="word"> <!--智能k提示--> </datalist>
```

&lt;script type="text/javascript"&gt; function showautofill\(\){ var commentsbaseurl = "/autofill/" var qord = document.getElementById\('focusedInput\_name'\).value; commentsbaseurl = commentsbaseurl + qord; $.get\(commentsbaseurl, function\(data\) { if \(data != "NULL"\) { document.getElementById\("word"\).innerHTML = data; } }\); }

&lt;/script&gt;&lt;/pre&gt; 在上面代码中，我们通过commentsbaseurl来获取提示数据。

注意，这里的提示数据是由我服务器直接返回的一大串 &lt;options&gt;&lt;/options&gt;数据。然后直接插入到word div标签的。





---
`© kanch` → [zl AT kanchz DOT com](kanchisme@gmail.com) → _posted at {{page.date}}_

_last updated on 2019-08-12 16:12:03.805005_