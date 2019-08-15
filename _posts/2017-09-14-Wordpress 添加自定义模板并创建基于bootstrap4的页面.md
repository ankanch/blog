---
title: Wordpress 添加自定义模板并创建基于bootstrap4的页面
tags:
  - PHP
  - wordpress
  - wordpress模板
  - 样式表
  - 模板
  - 网站搭建
id: 827
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 网站制作相关
date: '2017-09-14T23:03:05.000Z'
---

# Wordpress 添加自定义模板并创建基于bootstrap4的页面

最近我写了一个博客系统（[myblog](https://github.com/ankanch/myblog)），原本打算替换掉wordpress的，但是后面发现wordpress可以自定义模板，故将myblog的部分样式应用到自定义页面模板上，本来以为只需要简单的创建模板，然后导入css和js即可，结果发现导入后界面完全乱了，甚至还影响了属于wordpress的部分（footer和header）。

由于我的myblog需要bootstrap 4的支持，所以需要额外导入bootstrap 4的样式表，但是由于我使用的主题使用了低版本的样式表，如果直接在模板页面导入会照成我导入的覆盖掉主题默认使用的，导致界面混乱。在经过一番搜索后，找到了如下几个解决方案：

1. 使用iframe
2. 手动添加 容器ID来限定每个样式的作用域
3. 使用第三方插件如：[Simon Madine's jQuery Scoped CSS plugin](https://github.com/thingsinjars/jQuery-Scoped-CSS-plugin).

   我首先尝试了方法二，写了个python脚本帮助实现，但是对于 @media之类的，就无能为力了，故放弃。

然后尝试方法一，有效的方法。如下：

首先我们要创建一个自定义模板，以myblog\_theme\_page.php为例，其代码如下：

myblog\_theme\_page.php:

&lt;?php / _Template Name: myblog\_theme_ / get\_header\(\); ?&gt;

&lt;div id="primary" class="site-content-fullwidth" style="background:white;"&gt; &lt;div id="content" role="main" style="background:white;"&gt; &lt;div id="myblog\_style\_page" style="margin-left:45px;margin-right:45px;"&gt; &lt;link rel='stylesheet' href='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/bootstrap4alpha.css](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/bootstrap4alpha.css)' type='text/css' /&gt; &lt;script type='text/javascript' src='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/js/jquery-3.2.1.min.js'&gt;&lt;/script&gt](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/js/jquery-3.2.1.min.js'></script&gt); &lt;link rel='stylesheet' href='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/xstyle.css](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/xstyle.css)' type='text/css' /&gt; &lt;div class="container"&gt; &lt;?php / _Start the Loop_ / ?&gt; &lt;?php while\(have\_posts\(\)\) : the\_post\(\); ?&gt; &lt;?php the\_content\(\);?&gt; &lt;?php endwhile; ?&gt;

&lt;/div&gt; &lt;/div&gt; &lt;iframe id="result" frameBorder="0" style="overflow:hidden;"&gt; &lt;/iframe&gt; &lt;/div&gt;&lt;!-- \#content --&gt; &lt;/div&gt;&lt;!-- \#primary --&gt; &lt;script&gt; function resizeIframe\(obj\) { obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px'; } $\(document\).ready\(function \(\) { var iframe = document.getElementById\('result'\), iframedoc = iframe.contentDocument \|\| iframe.contentWindow.document; var father = document.getElementById\('myblog\_style\_page'\); iframedoc.body.innerHTML = iframedoc.body.innerHTML + father.innerHTML ; resizeIframe\(iframe\); father.innerHTML = "";

```text
});
```

&lt;/script&gt; &lt;?php get\_footer\(\); ?&gt;&lt;/pre&gt; 关于模板的详细说明，请参照 wordpress官方文档（[中文](https://codex.wordpress.org/zh-cn:页面)，[英文](https://developer.wordpress.org/themes/template-files-section/page-template-files/)）。这里我只说明重要的部分：

下面这段代码是用来加载用户在wordpress编辑器中输入的内容的，也就是新建页面，套用我们上面那个模板，用户在wordpress编辑器中输入的内容将会由以下代码段获取：

```
<?php /* Start the Loop */ ?> <?php while(have_posts()) : the_post(); ?> <?php the_content();?> <?php endwhile; ?>
```

&lt;div id="myblog\_style\_page" style="margin-left:45px;margin-right:45px;"&gt; &lt;link rel='stylesheet' href='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/bootstrap4alpha.css](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/bootstrap4alpha.css)' type='text/css' /&gt; &lt;script type='text/javascript' src='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/js/jquery-3.2.1.min.js'&gt;&lt;/script&gt](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/js/jquery-3.2.1.min.js'></script&gt); &lt;link rel='stylesheet' href='[https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/xstyle.css](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/themes/nisarg/css/xstyle.css)' type='text/css' /&gt;

&lt;div class="container"&gt;

&lt;?php / _Start the Loop_ / ?&gt; &lt;?php while\(have\_posts\(\)\) : the\_post\(\); ?&gt; &lt;?php the\_content\(\);?&gt; &lt;?php endwhile; ?&gt;

&lt;/div&gt; &lt;/div&gt;&lt;/pre&gt; 在class为container的div里，我们将会加载用户输入的页面内容，然后在外层div我们会引入我们需要的样式表文件和jquery文件。外层div是有id属性的，因为待会我们需要获取这个div里面的内容。

接下来，我们在紧接着上面的代码定义了一个iframe，并设置没有边框和隐藏滚动条。这样它看起来会更像页面的一部分。iframe代码如下：

```
<iframe id="result" frameBorder="0" style="overflow:hidden;"> </iframe>
```

&lt;script&gt; function resizeIframe\(obj\) { obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px'; } $\(document\).ready\(function \(\) { var iframe = document.getElementById\('result'\), iframedoc = iframe.contentDocument \|\| iframe.contentWindow.document; var father = document.getElementById\('myblog\_style\_page'\); iframedoc.body.innerHTML = iframedoc.body.innerHTML + father.innerHTML ; resizeIframe\(iframe\); father.innerHTML = "";

```text
});
```

&lt;/script&gt;&lt;/pre&gt; resizeIframe\(obj\)函数用来将iframe的高度设置为和页面高度一致。 在$\(document\).ready\(\)函数中，我们获取了id为myblog\_style\_page的div的内部HTML然后将其复制到iframe里面，再清空myblog\_style\_page的值。到这里，页面应该已经可以正常显示原有样式了（参照本站的[关于页面](https://raw.githubusercontent.com/ankanch/blog/master/images/about/)和我的[项目页面](https://raw.githubusercontent.com/ankanch/blog/master/images/myprojects/)）。

接下来我们要上传这个模板和相应的css，js文件到相应的位置。

首先要找到你正在使用的wordpress主题，wordpress主题目录如下：

> /usr/share/nginx/html/wp-content/themes 我使用的nisarg，相应的目录为/usr/share/nginx/html/wp-content/themes/nisarg，打开上面目录后我们可以看到下图中的文件：

[![](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2017/09/addasdasda-300x160.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2017/09/addasdasda.png)

接下来，我们只需要将相应的css，js和刚刚创建的模板上传到相应的文件夹即可。最后创建页面，在右侧选择相应的页面模板，编辑完页面内容后发布页面，就可以正常显示了。

_\*\*已知缺点：由于我们直接把模板文件和样式表放在主题目录里面的，在更新主题后，这些东西将会消失！_



{% include post_footer.md %}