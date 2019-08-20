---
title: Kanch.blog
date: '2018-03-12T17:12:39.000Z'
layout: global
---

# About Kanch.blog

* Name: Long Zhang
* Location: ~~Chengdu~~→Suzhou China
* Email: [kanch is me AT gmail DOT com](kanchisme@gmail.com)
* Github:[https://github.com/ankanch](https://github.com/ankanch)
* [Resume Download](http://d.akakanch.com/BlogResourceShare/Resume%20of%20Long%20Zhang%20March%202018%20-formal-reversion%201.pdf)

Computer Science Major 2015 @ Chengdu University of Information Technology : Graduated

Feel free to contact me if you have any ideas.

## Site Updates:

_最近我将我的博客从腾讯云迁移到了Github Pages,正在慢慢打理中。_

`Last Modified: Aug. 17 2019`

### Posts List

完整文章列表请访问：[/posts](/posts) , 下面显示了最近的5篇文章：

{% for post in site.posts limit:5 %}
[{{ post.date | date_to_string }} - {{ post.title }}]({{ site.baseurl }}{{ post.url }})  
{% endfor %}


`© kanch`