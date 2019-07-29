---
title: Google App Enigne Python文件读写
tags:
  - appspot
  - GAE
  - GAE文件操作
  - Google App Enigne
  - Google Cloud Storage
  - GoogleAppEngineCloudStorageClient
  - python
id: 638
categories:
  - Linux / Unix /虚拟主机 / VPS
  - Python
  - 网站制作相关
date: 2016-12-04 11:05:43
---

&nbsp;

**&lt;转载请注明来源&gt;**

之前在google app enigne上面搭建了一个用来抓取学校新闻的网站（[各种学术讲座预告新闻](https://forcuit-151103.appspot.com/news_xueshu)），还可以通过邮件提醒学校新闻的更新。

因为要记录增量更新的新闻，所以需要将新闻缓存在文件里面（数据库也可以，但考虑到GAE免费版只支持python2，所以还是用文件缓存吧）

当时学python的时候（点我[30分钟快速入门](http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html)）直接学的python3的语法，python2和python3有许多的不同([点我参考不同之处](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html))

当然python3写的程序，也可以方便的通过[**3to2**](https://pypi.python.org/pypi/3to2/1.1.1)转换得到相应的python2版本。

通过以下命令，3to2可以将指定python3文件或路径里的所有python3文件转换为python2的语法：
<pre class="lang:python decode:true ">#
#file 为文件或者文件夹
python3 3to2.py -w [file]
</pre>
当时以为只需要简单的将文件操作转换为python2的即可，结果部署到GAE后发现，并不能写入，更别说读取了。

后面在GAE的控制台看错误信息，发现并没有相关错误提示。故Google之([google app engine python read file](https://www.google.com.hk/search?newwindow=1&amp;safe=strict&amp;q=google+app+engine+python+read+file&amp;oq=Google+App+Engine+&amp;gs_l=serp.3.0.35i39k1j0l9.199.3152.0.4575.12.12.0.0.0.0.344.1898.0j6j2j1.9.0....0...1c.1.64.serp..3.9.1898...0i20k1.cSDLSUneB4s))...

* * *

&nbsp;

后面找到了这个：[Reading and Writing to Google Cloud Storage](https://cloud.google.com/appengine/docs/python/googlecloudstorageclient/read-write-to-cloud-storage)

再搜索了一下Google Cloud Storage，发现GAE的应用如果要使用文件都需要在这个上面进行。
于是以为只需要简单的通过 pip install cloudstorage 即可，因为谷歌给出的示例代码是直接 import cloudstorage 的。

结果事实证明并不行。接下来当然又要借助万能的谷歌了，搜索how toinstall python google cloud storage 。最后得到了这个：[install python google cloud storage client on Ubuntu 14.04](http://stackoverflow.com/questions/25100031/install-python-google-cloud-storage-client-on-ubuntu-14-04)

虽然是Ubuntu的，但还是凑合着用吧。通过那个网站我们知道Google Cloud Storage的正确的包名为：

**GoogleAppEngineCloudStorageClient**

接下来就简单了，直接pip安装，不过还要[结合之前那篇文章的方法](http://akakanch.com/archives/634)，将那货安装到应用的lib目录，否则，部署到GAE后会提示找不到module！
<pre class="lang:sh decode:true ">#
#假设该命令运行目录为你应用的根目录（即可见lib文件夹的目录）

pip install GoogleAppEngineCloudStorageClient -t lib

#
#如果你同时安装了python2和python3，请使用以下命令：

py -2 -m pip install GoogleAppEngineCloudStorageClient -t lib</pre>
到这里，我们已经完成了必要模块的安装，接下来开始敲代码了。

还是参考google的文档：[Reading and Writing to Google Cloud Storage](https://cloud.google.com/appengine/docs/python/googlecloudstorageclient/read-write-to-cloud-storage)

首先import一些必要库：
<pre class="lang:python decode:true ">#
#
import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity</pre>
google在文档中说明，所有的文件操作都在一个叫做bucket的东西里面进行的，bucket是可以扩充的，当然，免费版只有5GB而且是所有你账户下免费GAE应用共享的，不过对于部署GAE应用来说，足够了（毕竟google通过GAE赚不了什么钱。）

所以，bucket这里我们直接使用默认的即可，通过以下代码获取默认bucket路径，所有的文件都会存放在这个路径下：
<pre class="lang:python decode:true">#
#RetryParams是说明文件读写超时时间，这里直接使用了google默认的
#cachepath即为我们要存放文件的路径，直接cachepath+filename即可
bucket_name = os.environ.get('BUCKET_NAME',app_identity.get_default_gcs_bucket_name())
write_retry_params = gcs.RetryParams(backoff_factor=1.1)
cachepath = '/' + bucket_name +'/'</pre>
接下来讲读写文件操作：

文件读写同样主要用到open(),read(),write(),不过，这些函数是cloudstorage里面的。

详细的函数说明可以参考google官方文档：[**Google Cloud Storage Client Library Functions**](https://cloud.google.com/appengine/docs/python/googlecloudstorageclient/functions#open)

下面是一个写文件的例子：
<pre class="lang:python decode:true">#
#写文件操作主要在try块里面，google的代码没有try块，不过为了防止操作失败，建议还是加上
def refreshCache(data,cachefilename):
    try:
        gcs_file = gcs.open(cachepath+cachefilename,     #文件名（要加上路径，否则会出错）
                      'w',                               #要执行的操作类型，这里是写操作，默认为读操作
                      content_type='text/plain',         #指定要以何种方式写入文件（仅在操作类型为w的时候有效）
                                                         #默认是以二进制方式写入，这里我们使用纯文本
                      retry_params=write_retry_params)   #超时设置
        gcs_file.write(data)
        gcs_file.close()
    except Exception as e:
        return "CACHE ERROR：refresh &lt;br/&gt;please contact kanch@akakanch.com&lt;hr/&gt;"
    return "OK&lt;hr/&gt;"</pre>
上面的注释已经简要的说明了各个必要参数的意思。

接下来是一个读取文件的例子：
<pre class="lang:python decode:true ">#
#同样的读取文件的代码主要在try块里面
def checkNewNews(newsdata,cachefilename):
    sourcedata = ""
    newslist = newsdata
    try:
        gcs_file = gcs.open(cachepath+cachefilename,
                      retry_params=write_retry_params)
        sourcedata = gcs_file.read()
        gcs_file.close()
    except Exception as e:
        return "CACHE ERROR：check &lt;br/&gt;please contact kanch@akakanch.com&lt;hr/&gt;"
    return newupdate</pre>
可以看到，我们没有指定打开模式，所以函数使用了默认打开方式，即读取文件模式。

最后就是简单的read()出来进行处理了。

* * *

再来简单的说下Google App Engine吧，每个google帐号可以有10个免费GAE资源。不过中文资料太难找，部署起来还是算比较麻烦的，不过免费的，大家都喜欢。。。

GAE允许的每个响应的最长响应时间为60秒，如果60秒操作还没结束，就会被GAE管理杀掉，然后报错。。。。所以大家千万不要执行一些耗时长的操作，否则~~~~~

GAE对于一些小的应用来说足够了，唯一的缺点是python只支持python2，支持python3的为Flexiable版（收费）。

GAE在国内是无法访问的，不过国内有牛人做了一个反向代理，只需要简单的改变下GAE App的地址即可：

比如，源地址：[https://forcuit-151103.appspot.com/](https://forcuit-151103.appspot.com/)

改为：[ https://forcuit-151103.appsp0t.com/ ](https://forcuit-151103.appsp0t.com/)即可在国内正常访问。（只是把appsopt改为了appsp0t哈哈哈哈）。另外，大家也可以通过反向代理的方式来让国内可访问GAE。

&nbsp;

**&lt;转载请注明来源&gt;**