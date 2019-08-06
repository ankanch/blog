---
title: Kanch.blog
date: '2018-03-12T17:12:39.000Z'
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

`Last Modified: Aug. 6 2019`

### Posts List
　　　　{% for post in site.posts %}
　　　　　　[{{ post.date | date_to_string }} - {{ post.title }}]({{ site.baseurl }}{{ post.url }})

　　　　{% endfor %}


`© kanch`