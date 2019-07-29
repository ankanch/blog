---
title: 在Ubuntu 16.04上使用 Nginx 和 Gunicorn 托管 Python Flask网站
tags:
  - flask
  - Gunicorn
  - Nginx
  - python
  - Systemd
  - Ubuntu
  - upstart
  - 反向代理
id: 833
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 网站制作相关
  - 翻译
  - 转载
date: 2017-09-16 16:02:40
---

<div class="important-comment" style="background: #334455; color: gray; padding: 10px; border-radius: 25px; margin-top: 8px; margin-bottom: 25px;">翻译至：<span style="color: #ff6600;">[How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) </span></div>

## 引言

通过这个教程我们将会学习到如何利用Gunicorn 结合 Nginx 使 Flask 应用程序运行在Ubuntu 16.04上。本文的大部分内容将介绍如何设置Gunicorn应用程序服务器以启动应用程序，并将Nginx用作前端反向代理。

## 教程开始之前...

你需要一个可以执行 sudo 命令的用户账户，系统上应该确保安装了systemd （注意，不是upstart）。如果有[WSGI的相关知识](https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04#definitions-and-concepts)那就更好不过了，不过没有也不影响。

## 安装相关组件

这一步我们将会安装 Python 包管理程序 pip 和 Nginx。

如果你的版本为 Python 2.x，使用以下命令安装：
<pre class="lang:sh decode:true">sudo apt-get update
sudo apt-get install python-pip python-dev nginx</pre>
如果你的版本是Python 3.x， 使用以下命令：
<pre class="lang:sh decode:true ">sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx</pre>

## 创建虚拟环境

略

## 设置 Flask 应用程序

首先我们需要安装Flask 和 Gunicorn，通过以下命令进行安装：
<pre class="lang:sh decode:true ">pip install gunicorn flask</pre>
如果你使用的Python 3，请使用以下命令：
<pre class="lang:sh decode:true ">pip3 install gunicorn flask</pre>
接下来我们创建 flask 应用程序，我们取名为 myproject.py，其代码如下：
<pre class="lang:python decode:true">from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "&lt;h1 style='color:blue'&gt;Hello There!&lt;/h1&gt;"

if __name__ == "__main__":
    app.run(host='0.0.0.0')</pre>
上面的代码定义了一个非常简单的页面，并将其绑定到本地根域名。

为了访问我们的flask应用程序，首先，我们需要打开 5000端口。通过以下命令打开5000端口：
<pre class="lang:sh decode:true ">sudo ufw allow 5000</pre>
紧接着，我们开始运行我们的 flask 应用程序：
<pre class="lang:sh decode:true ">python myproject.py</pre>
然后我们通过主机名或者我们服务器的IP地址来访问该程序，再浏览器中输入以下地址：
<pre class="lang:sh decode:true ">http://server_domain_or_IP:5000</pre>
一切正常的话，你的应该看起来和下图一样:

![Flask sample app](https://assets.digitalocean.com/articles/nginx_uwsgi_wsgi_1404/test_app.png)

这里配置完毕后，我们通过再控制台按 Ctrl + C命令来结束我们的flask应用程序。

## 创建WSGI入口脚本

接下来，我们将创建一个脚本文件，作为我们应用程序的入口点。这个脚本将告诉我们的Gunicorn服务器应该如何与应用程序进行交互。

我们将文件命名为 wsgi.py，创建文件:
<pre class="lang:sh decode:true ">nano ~/myproject/wsgi.py</pre>
文件内容如下，只是简单的导入我们flask应用程序的app模块：
<pre class="lang:python decode:true ">from myproject import app

if __name__ == "__main__":
    app.run()</pre>
文件写好后保存并推出，接下来我们进行下一步。

## 测试 Gunicorn 能否正常托管我们的flask应用程序

接下来我们测试 Gunicorn是否正常工作。

我们可以通过简单的讲WSGI入口名称传递给Gunicorn，测试是否正常运行。WSGI入口名字通常由以下部分组成：
<pre class="lang:c++ decode:true ">WSGI入口名称 = 模块名称 + 应用程序中可调用名称</pre>
模块名称即WSGI脚本名称（不含文件扩展名），应用程序中可调用名称即 flask 中的 app = Flask(__name__)。在我们的例子中，WSGI入口名称为 wsgi:app 。

在运行Gunicorn的过程中我们同时需要指定 IP地址和端口来确保可以正常访问。
<pre class="lang:sh decode:true ">cd ~/myproject
gunicorn --bind 0.0.0.0:5000 wsgi:app</pre>
还是和刚刚直接测试 flask 脚本相同，请在浏览器输入以下地址进行访问：
<pre class="lang:sh decode:true ">http://server_domain_or_IP:5000</pre>
如果出现下图，即表示可以正常运行。

![Flask sample app](https://assets.digitalocean.com/articles/nginx_uwsgi_wsgi_1404/test_app.png)

## 创建 Systemd 单元文件

接下来我们需要创建一个systemd 系统服务文件。该文件将允许Ubuntu在开机的时候自动启动Gunicorn，并为我们的Flask应用程序提供服务。通过这个文件，我们的 flask应用程序已经成为系统的一个服务，可以通过 service 命令来启动/关闭以及重新启动。

创建文件：
<pre class="lang:sh decode:true ">sudo nano /etc/systemd/system/myproject.service</pre>
在这个文件里面，我们将从[Unit]部分开始，该部分用于指定元数据和依赖关系。我们将在这里描述我们的服务，并告诉init系统只有在达到网络目标后才能启动它（联网?）。
<pre class="lang:sh decode:true ">[Unit]
Description=Gunicorn instance to serve myproject
After=network.target</pre>
接下来，我们编写 [Service] 部分，我们将会指定该服务使用何种用户账户运行。由于flask程序拥有所有必不可少的运行文件，因此我们会给予其常规的用户帐户所有权。我们将会赋予它为 www-data 用户组，这样Nginx和它数据交换更加容易。

然后我们设置工作路径和 PATH 环境变量，这样 初始化系统 就知道Gunicorn可执行程序在哪里。 Systemd 要求我们以完整路径名指定可执行程序。如果你不知道完整路径，可以尝试：
<pre class="lang:sh decode:true">locate [name]</pre>
或者
<pre class="lang:sh decode:true ">which name</pre>
我们将会设置 Gunicorn开启3个工作线程（根据您的需求更改）。我们同时会令 Gunicorn 绑定一个 命名为 myproject.socket 位于我们工作目录的Unix 套接字文件。设置套接字文件的 umask为 007这样该文件仅能被和myproject服务相同的用户组访问。最后，我们需要将WSGI入口名称传递给Gunicorn，截至目前，myproject.service内容如下:
<pre class="lang:sh decode:true ">[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app</pre>
最后，我们会需要添加[Install]块，这可以让 systemd 知道应该在哪种系统启动模式时启动服务。我们希望让这个服务在正常启动系统时随系统启动：
<pre class="lang:sh decode:true ">[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target</pre>
至此，我们的 systemd服务文件已经完成。

我们现在可以启动该服务，并令其在系统开机时自动启动：
<pre class="lang:sh decode:true ">sudo systemctl start myproject
sudo systemctl enable myproject</pre>

## 配置Nginx

我们的Gunicorn程序目前应该可以正常运行了。接下来我们要配置Nginx来传递网络请求到刚刚创建的套接字文件，这样才能够访问到我们的flask应用程序。

我们可以在Niginx的sites-available文件夹下新增配置文件，避免修改默认配置文件。

我们将我们的配置文件命名为 myproject：
<pre class="lang:sh decode:true ">sudo nano /etc/nginx/sites-available/myproject</pre>
在文件里面下入以下内容：
<pre class="lang:sh decode:true">server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}</pre>
我们需要修改上述文件内容中的 server_domain_or_IP，server_domain_or_IP设置为你的域名或者IP地址。 如果你没有使用套接字文件，而是绑定IP端口的形式，请修改 proxy_pass后面的内容到您flask应用程序绑定的对应IP和端口。

保存文件，接下来我们需要让这个配置文件生效，将该文件链接到Nginx的`sites-enabled`文件目录：
<pre class="lang:sh decode:true ">sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled</pre>
接下来我们测试Nginx配置文件是否有错误：
<pre class="lang:sh decode:true ">sudo nginx -t</pre>
如果该命令没有输出任何错误信息，我们就可以重启我们的nginx服务器，使配置文件生效：
<pre class="lang:sh decode:true ">sudo systemctl restart nginx</pre>
如果你启用了防火墙，接下来我们就可以关闭5000端口的访问，开启Nginx的外网访问：
<pre class="lang:sh decode:true ">sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'</pre>
你现在应该可以通过服务器域名或者IP地址从外网访问您的flask应用程序了。
<pre class="lang:sh decode:true ">http://server_domain_or_IP</pre>
它应该看起来如下：

## ![Flask sample app](https://assets.digitalocean.com/articles/nginx_uwsgi_wsgi_1404/test_app.png)总结

我们创立了一个建议flask应用程序，同时我们创建了 WSGI 入口点，这样任何支持 WSGI的服务程序都可以支持我们的flask应用（我们使用的Gunicorn完成这一功能）。

然后我们创建了systemd系统服务文件来让我们的flask应用程序开机自动启动。我们还配置了Nginx来反向代理我们的服务器。