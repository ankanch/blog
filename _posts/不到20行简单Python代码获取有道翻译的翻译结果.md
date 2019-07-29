---
title: 不到20行简单Python代码获取有道翻译的翻译结果
tags:
  - python
  - ytohn
  - 有道翻译
  - 网页分析
  - 网页抓取
  - 翻译
  - 翻译软件
id: 507
categories:
  - Linux / Unix /虚拟主机 / VPS
  - Python
date: 2016-09-28 12:51:05
---

Python真是一个牛逼的脚本语言。

接下来我来谈谈这个小程序，一个不到20行核心代码的小程序，用户输入对应的英文字母，我们返回相应的中文翻译，当然，中文翻译来自有道翻译。

接下来进入正题。

简单的讲，获取翻译结果就是将目标网页下载下来，然后进行字符串匹配，从网页源代码中匹配出翻译结果就行。

如下图所示：

[![](http://115.159.197.66/wp-content/uploads/2016/09/QQ图片20160906154407-1-1024x576.png)](http://115.159.197.66/wp-content/uploads/2016/09/QQ图片20160906154407-1.png)

我们首先打开有道翻译，然后随便翻译点什么，然后，观察url的变化，因为之后我们需要通过这个url来构造我们的翻译查询url：
<pre class="lang:python decode:true">query_url="http://fanyi.youdao.com/translate?ue=utf-8&amp;keyfrom=baidu&amp;smartresult=dict&amp;type=EN2ZH_CN&amp;i=" + word    #word是要翻译的单词</pre>
然后，我们再看对应的网页源代码，我们可以看到，有道翻译的翻译结果是直接显示在网页源代码里面的，所以，接下来我们需要做的就是，观察翻译结果周围的字符串，看看有什么特点，这里指的是翻译结果周围的字符串应该足够奇葩，保证，网页源代码里面只有一个。

比如我可以看到，这串翻译结果，前面的字符串是 "tgt":" 后面的是"}]],，简直奇葩，可以保证只有一个。

所以，整个流程应该是：

构造翻译url -&gt; 下载对应的网页 -&gt; 从对应的网页里匹配出字符串

下载网页，我们可以通过urllib的urlopen和read实现。
<pre class="lang:python decode:true">page = urllib.request.urlopen(url,timeout=5)
html = page.read()
html = getHtml(url)
html = html.decode('utf-8','ignore')   #解码，一定要加上ignore标签，否则可能会出错</pre>
匹配字符串，我们只需要find对应首尾字符串，然后提取子串即可
<pre class="lang:python decode:true">head = "\"tgt\":\""
tail = "\"}]],"
start = html.find(head)
end = html.find(tail,start)
result1 = html[start+len(head):end]</pre>
所以最终代码下：

如果只提取一个中文意思，且不包括其它附加信息的话，核心代码就只有10行。

所以呢，python简直太6666
<pre class="lang:python decode:true">#coding=utf-8
import urllib.request
import urllib.parse
import re

query_url="http://fanyi.youdao.com/translate?ue=utf-8&amp;keyfrom=baidu&amp;smartresult=dict&amp;type=EN2ZH_CN&amp;i="

def getHtml(url):
    page = urllib.request.urlopen(url,timeout=5)
    html = page.read()
    return html

def getTranslate(word,query_url):
    #url = query_url + urllib.parse.urlparse(word)
    url = query_url + word
    html = getHtml(url)
    html = html.decode('utf-8','ignore')
    #寻找翻译结果
    head = "\"tgt\":\""
    tail = "\"}]],"
    start = html.find(head)
    end = html.find(tail,start)
    result1 = html[start+len(head):end]
    #寻找附加结果
    head ="[\"\",\""
    tail ="\"]}};"
    start = html.find(head)
    end = html.find(tail,start)
    result2 = html[start+len(head):end]
    print('\r\n\r\n',word,'\r\n',result1,'\r\n',result2,'\r\n\r\n\r\n')

word = "11111"
while(word != "EEXXIITT"):
    word = input("enter a word(ENGLISH -&gt; CHINESE) : _________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
    getTranslate(word,query_url)</pre>
运行结果：

[![img20160918211121](http://115.159.197.66/wp-content/uploads/2016/09/IMG20160918211121-1024x458.jpg)](http://115.159.197.66/wp-content/uploads/2016/09/IMG20160918211121.jpg)