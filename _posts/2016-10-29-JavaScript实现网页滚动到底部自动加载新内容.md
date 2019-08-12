---
title: JavaScript实现网页滚动到底部自动加载新内容
tags:
  - HTML
  - JavaScript
  - 加载新内容
  - 局部刷新
id: 584
categories:
  - 网站制作相关
date: '2016-10-29T14:45:07.000Z'
---

# JavaScript实现网页滚动到底部自动加载新内容

实现效果如图[![QQ&#x622A;&#x56FE;20161029143852](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/QQ截图20161029143852.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2016/10/QQ截图20161029143852.png)

当网页滚动到底部的时候，自动加载更多评论。

JavaScript的实现逻辑非常简单，就是判断滚动条的滚动长度是否和网页长度一样了。

其JS代码如下：

var p = 1; var page\_num = 2;

```text
                function loadComments() {
                    var tid = document.getElementById("tid").innerHTML;
                    var commentsbaseurl = "/getcomments/"
                    commentsbaseurl = commentsbaseurl + tid + "/" + p + "/";
                    p += 5
                    $.get(commentsbaseurl, function(data) {
                        if (data != "NULL") {
                            document.getElementById("commentslist").innerHTML = document.getElementById("commentslist").innerHTML + data;
                        } else {
                            $.snackbar({
                                content: "评论已经全部拉取完毕！如果你刚刚提交了评论，请不要着急，评论刷新存在延迟。"
                            });
                        }
                    });
                }
                $(document).ready(function() {
                    $(window).scroll(function() {
                        if ($(document).scrollTop() &gt;= $(document).height() - $(window).height()) {
                            var div1tem = $('#container').height()

                            loadComments()
                        }
                    })
                })</pre>
```

你们只需要自定义loadComments\(）函数即可实现，当网页滚动到底部的时候加载更多内容。

即通过JavaScript获取新内容放到以个&lt;div&gt;&lt;/div&gt;里即可。

已知bug：

如果用户的分辨率太大，浏览器没有滚动条出现，那么此方法就会失效。

一个可能的解决办法是，再加一个按钮，来实现手动加载。



`© kanch` → [zl AT kanchz DOT com](kanchisme@gmail.com) → _posted at {{page.date}}_
_last updated on 2019-08-12 16:02:21.020573_