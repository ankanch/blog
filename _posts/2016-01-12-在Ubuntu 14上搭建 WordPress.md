---
title: 在Ubuntu 14上搭建 WordPress
tags:
  - PHP
  - Ubuntu
  - VPS搭建博客
  - wordpress
  - 博客搭建
  - 搭建WordPress
id: 343
categories:
  - Linux / Unix /虚拟主机 / VPS
  - 网站制作相关
date: '2016-01-12T00:04:57.000Z'
---

# 在Ubuntu 14上搭建 WordPress

先说下我的服务器配置，Ubuntu14.04，单核1G内存。我这个博客就是从GoDaddy的托管服务器上转过来，转到阿里ECS服务器的，不过，说实话，配置真麻烦。

接着我们进入正题，如何搭建。

## 首先要安装相关支持软件

更新一下所有软件包，用下面这个命令：

```text
apt-get update
apt-get upgrade
```

 接着，我们安装我们搭建WordPress所需要的一些必须软件包：

```text
apt-get install nginx postfix php5-fpm mariadb-server memcached
apt-get install php-pear php5-mysql php5-curl php5-gd php5-mcrypt php5-memcache
apt-get install python make screen git wget zip unzip iftop vim curl htop iptraf nethogs
```

 上面这些命令主要安装了以下软件包， Web 服务器，SMTP 服务器，类 MySQL 数据库以及PHP相关的东西。 \#\# 接下来安装WordPress 先新建一个普通用户，然后切换到该用户：

```text
adduser wordpress
su wordpress
cd ~
```

 接着我们用以下命令下载WordPress，注意命令中给出的WordPress版本为\_简中4.4.1\_（更新时间2016-1-11）。 你们可以到这里找到最新版本的WordPress：\[https://cn.wordpress.org/\]\(https://cn.wordpress.org/\)

```text
wget https://cn.wordpress.org/wordpress-4.4.1-zh_CN.tar.gz
```

 接着我们解压刚刚下载好的文件：

```text
unzip wordpress-*.zip
```

 然后设置该文件权限：

```text
chmod -R 750 wordpress
```

 然后呢，这里有一个可选步骤，删除安装包，看你们咯，觉得占用空间的话，你们就删除吧：

```text
rm wordpress-*.zip
```

 然后我们再用exit命令回到root：

```text
exit
```

 接着，我们来配置 PHP-FPM 先为 WordPress 创建一个进程池：

```text
vi /etc/php5/fpm/pool.d/wordpress.conf
```

 在新文件里面写入以下内容：

```text
[wordpress]

user = wordpress
group = wordpress

listen = /home/wordpress/phpfpm.sock

listen.owner = wordpress
listen.group = wordpress
listen.mode = 0660

pm = dynamic
pm.max_children = 10
pm.min_spare_servers = 3
pm.max_spare_servers = 5

slowlog = /home/wordpress/phpfpm.slowlog
request_slowlog_timeout = 5s
request_terminate_timeout = 15s

php_admin_value[error_log] = /home/wordpress/phpfpm_error.log
php_admin_flag[log_errors] = On
```

 然后我们来配置 Nginx 先删掉 Nginx 的默认站点：

```text
rm /etc/nginx/sites-enabled/default
```

 再新建一个站点：

```text
vi /etc/nginx/sites-enabled/wordpress
```

 写入以下内容（这份配置文件已将请求重写到 index.php, 可以直接在 WordPress 中使用「固定链接」功能：）：

```text
server {
  listen 80;
  server_name jysperm.me;

  root /home/wordpress/wordpress;
  index index.html index.php;
  autoindex off;

  location / {
    try_files $uri $uri/ /index.php;
  } 

  location ~ \.php$ { 
    fastcgi_pass unix:///home/wordpress/phpfpm.sock;
    include fastcgi_params;
    fastcgi_index index.php;
  }
}
```

 然后我们需要修正 Nginx 和 PHP-FPM 配合的一个 Bug: 先打开以下文件

```text
vi /etc/nginx/fastcgi_params
```

 然后将文件中fastcgi\_param SCRIPT\_FILENAME 开头的行改为：

```text
fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
```

 接着，我们为 Nginx 添加读取 WordPress 文件的权限：

```text
usermod -G wordpress -a www-data
```

## 最后，我们来配置MySQL

先用以下命令进入MySQL控制台：

```
mysql -p
```

完毕后我们创建数据库：

    CREATE DATABASE `wordpress`;
    CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON `wordpress` . * TO 'wordpress'@'localhost';
    QUIT
    reboot

