---
title: Windows WSL + Docker 开发环境搭建
id: 857
tags:
  - Windows WSL
  - Docker
  - 开发环境搭建
  - Ubuntu
categories:
  - Docker / WSL
date: '2019-08-30 17:03:00'
tags: null
layout: posting
---

# Windows WSL + Docker 开发环境搭建

由于工作中需要使用docker，之前我都是在hyper-v里面安装ubuntu server然后在虚拟机里面进行程序的编译，测试。  

然而我开发还是使用的Windows系统。这造成了一定的不便，每次开发都需要跑个ubuntu虚拟机然后再windows下进行编码，再转到虚拟机中运行。   

为此，如果能够使用windows内置的WSL（Windows Subsystem for Linux） ，则可以令程序从编码到运行到测试都在Windows下进行，减少了资源消耗。  

下面进入正题。  

## 启用相关功能

为了在windows下使用WSL与Docker我们需要先启用WSL与Container可选功能。   

打开`控制面板`，点击左侧的`启用或关闭windows功能`，在列表里面找到以下两项：

> Containers （容器服务）  
> Windows Subsystem for Linux （Linux子系统）

把它们打勾，然后保存，重启电脑。  

![启用容器服务](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2019/08/enable-containers.png)![启用WSL服务](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2019/08/enable-wsl.png)   

重启完毕后，打开windows应用商店，搜索ubuntu，选择ubuntu18.04进行下载。下载完成，就可以在开始菜单里找到它并启动，第一次启动它会让你设置用户名与密码。   

![windows应用商店找到ubuntu18.04](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2019/08/ubuntu-wsl-install.png)

## 安装Docker

在以下地址注册登陆后便可下载安装docker：  
> [Docker Hub](https://hub.docker.com/)   

docker安装完毕后，在任务栏托盘找到docker图标，右键菜单进入settings界面。  

在Gneral页面，勾选暴露端口，如下图：   
![暴露docker daemon](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2019/08/expose-docker-daemon.png)

至此windows下docker部分我们已经设置完毕，接下来进行ubuntu里的docker设置。  

## WSL Ubuntu 18.04 Docker设置

### 安装Docker

首先，我们需要在Ubuntu里安装Docker。     
安装Docker包依赖：
```sh
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

下载Docker官方PGP密钥：  
```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

验证密钥签名：  
```sh
sudo apt-key fingerprint 0EBFCD88
```

将Docker “stable”分支加入apt中：  
```sh
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

更新apt包列表：
```sh
sudo apt-get update -y
```

安装Docker CE:
```sh
sudo apt-get install -y docker-ce
```

设置允许非root用户访问（如果不设置则在执行脚本时可能会遇到权限错误）：
```sh
sudo usermod -aG docker $USER
```

### 设置WSL Docker连接至Win10下的Docker

由于WSL里无法运行Docker Daemon，所以我们出去的策略是连接至windows下的docker进行镜像的运行。这样实际上程序的编码，运行，测试都可以在windows下完成。  

我们通过以下命令将WSL Docker连接至Windows下的Docker Dameon：
```sh
echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc && source ~/.bashrc
```

### 验证是否配置成功

通过在WSL命令行中执行以下命令验证是否成功配置：
```sh
docker info
```

![成功显示dockersinfo截图](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2019/08/docker-info-success.png)

### 配置WSL磁盘挂载

这一步非常必要！！！因为这一步没有设置或设置错误会导致运行中的docker 镜像无法正确的解析文件目录。  

Docker for Windows的期望目录结构为（以C盘为例）： 
> /c/Users/kanch/dev/application`  

然而实际上，WSL给解析的路径为：
> /mnt/c/Users/kanch/dev/application

为了解决这个问题，我们需要做出一定的的修改：  

#### 针对Win10 1803或者更新的版本

在WSL里以下路径创建`wsl.conf`文件：
```sh
sudo vim /etc/wsl.conf
```

写入文件内容如下：
```ini
[automount]
root = /
options = "metadata"
```

在上面的配置文件中，我们将root设置为了`/`，这样便可令c盘挂载于`/c`而不是`/mnt/c`。  

然后`options=metadate`则帮助我们避免WSL挂载的磁盘例得所有文件权限都是``777`。  

最后，重启电脑，问题已解决。

#### 1709及以前的版本

你需要通过以下命令，手动挂载：
```sh
sudo mkdir /c
sudo mount --bind /mnt/c /c
```
它的缺点是重启后需要重新挂载。所以建议你将其写入开机脚本里。

### 参考

* [Setting Up Docker for Windows and WSL to Work Flawlessly](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)


