---
title: Python Flask Google App Engine允许Access-Control-Allow-Origin跨域访问
tags:
  - Access-Control-Allow-Origin
  - flask
  - flask访问控制
  - flask跨域
  - python
  - Python Flask
  - python flask跨域请求
  - XMLHttpRequest cannot load
id: 644
categories:
  - C++ / Visual C++
  - Linux / Unix /虚拟主机 / VPS
  - Python
  - 网站制作相关
date: '2016-12-06T10:32:35.000Z'
layout: posting
---

# Python Flask Google App Engine允许Access-Control-Allow-Origin跨域访问

最近在做一个纯API接口，部署到Google App Engine上面（为了利用GAE的负载均衡，减少服务器压力）。

最后在另外一台服务器上调用的时候，却无法正确获取数据，提示错误如下：

**XMLHttpRequest cannot load '&lt;some-url&gt;'. No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin '&lt;my-url&gt;' is therefore not allowed access.**

经过搜索发现是因为跨域调用问题（即从一个域名请求另外一个域名下的信息，至少在Chrome中是禁止的）

解决该问题的方法如错误提示信息所示，在服务器端的response加入Access-Control-Allow-Origin即可。

网上查出来的很多方法都是通过在GAE的app.yaml文件里面添加来实现的，后面我尝试后发现不管用。

于是经过一番搜索，搜索出了这个：[Decorator for the HTTP Access Control](http://flask.pocoo.org/snippets/56/)

为Flask写一个访问修饰器，然后，通过在要控制Access-Control的路由函数前面添加@crossdomain\(origin='\*'\)来实现发送Access-Control-Allow-Origin头。

首先，我们定义一个如下函数（这个函数内部还有函数哦）：

from datetime import timedelta from flask import make\_response, request, current\_app from functools import update\_wrapper

def crossdomain\(origin=None, methods=None, headers=None, max\_age=21600, attach\_to\_all=True, automatic\_options=True\): if methods is not None: methods = ', '.join\(sorted\(x.upper\(\) for x in methods\)\) if headers is not None and not isinstance\(headers, basestring\): headers = ', '.join\(x.upper\(\) for x in headers\) if not isinstance\(origin, basestring\): origin = ', '.join\(origin\) if isinstance\(max\_age, timedelta\): max\_age = max\_age.total\_seconds\(\)

```text
def get_methods():
    if methods is not None:
        return methods

    options_resp = current_app.make_default_options_response()
    return options_resp.headers['allow']

def decorator(f):
    def wrapped_function(*args, **kwargs):
        if automatic_options and request.method == 'OPTIONS':
            resp = current_app.make_default_options_response()
        else:
            resp = make_response(f(*args, **kwargs))
        if not attach_to_all and request.method != 'OPTIONS':
            return resp

        h = resp.headers

        h['Access-Control-Allow-Origin'] = origin
        h['Access-Control-Allow-Methods'] = get_methods()
        h['Access-Control-Max-Age'] = str(max_age)
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers
        return resp

    f.provide_automatic_options = False
    return update_wrapper(wrapped_function, f)
return decorator</pre>
```

接着，我们只需要在我们要加入Access-Control-Allow-Origin头的位置添加下面这一句即可：

\#

@crossdomain\(origin='_'\) \# &lt;-添加这句，可以把_改为想要允许的域名

@app.route\('/my\_service'\) @crossdomain\(origin='\*'\) \#这货的添加位置应该在路由之后 def my\_service\(\):

```text
#do something</pre>
```

然后，我们再次调用API，就会发现，没有报这个错误了。



{% include post_footer.md %}