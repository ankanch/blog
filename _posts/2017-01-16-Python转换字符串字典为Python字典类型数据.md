---
title: Python转换字符串字典为Python字典类型数据
tags:
  - ast.literal_eval
  - eval
  - literal_eval
  - python
  - 字典
  - 字典字符串
  - 字典类型转换
id: 655
categories:
  - Python
date: '2017-01-16T22:48:25.000Z'
layout: posting
---

# Python转换字符串字典为Python字典类型数据

假设我们有一下字符串：

```
stra = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
```

大家知道可以通过 eval 函数转换，但是有一种更加安全的方法，那就是literal_eval

如下：

```
import ast stra = "{'muffin' : 'lolz', 'foo' : 'kitty'}" ast.literal_eval(stra) 
```

>>> help(ast.literal_eval) Help on function literal_eval in module ast:

literal_eval(node_or_string) Safely evaluate an expression node or a string containing a Python expression. The string or node provided may only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.</pre> 给出使用eval和 literal_eval转换时候的出错比较：

```
>>> eval("shutil.rmtree('mongo')") Traceback (most recent call last): File "<stdin>", line 1, in <module> File "<string>", line 1, in <module> File "/opt/Python-2.6.1/lib/python2.6/shutil.py", line 208, in rmtree onerror(os.listdir, path, sys.exc_info()) File "/opt/Python-2.6.1/lib/python2.6/shutil.py", line 206, in rmtree names = os.listdir(path) OSError: [Errno 2] No such file or directory: 'mongo' >>> ast.literal_eval("shutil.rmtree('mongo')") Traceback (most recent call last): File "<stdin>", line 1, in <module> File "/opt/Python-2.6.1/lib/python2.6/ast.py", line 68, in literal_eval return _convert(node_or_string) File "/opt/Python-2.6.1/lib/python2.6/ast.py", line 67, in _convert raise ValueError('malformed string') ValueError: malformed string
```



{% include post_footer.md %}