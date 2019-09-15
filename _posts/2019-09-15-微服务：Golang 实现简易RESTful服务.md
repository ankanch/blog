---
title: 微服务：Golang 实现简易RESTful服务
id: 858
tags:
  - golang
  - Golang
  - RESTful
  - 微服务
  - go-restful
  - restful web services
categories:
  - 微服务 / golang / restful
date: '2019-09-15 17:48:55'
layout: posting
---

# 微服务：Golang 实现简易RESTful服务

之前实现简单的API服务都是通过Python flask实现，最近由于工作需要，尝试了使用go实现。

假设我们要实现一个带有定时任务的RESTful服务，它可能定时去某一地方查询数据，然后进行某种处理，将处理后的数据提供给接口调用者。  

我们主要会用到两个包

> go-restful  
> scheduler  



Posts Working in progress



完整源代码如下：

```go
package main

import (
	"log"
	"net/http"

	"github.com/carlescere/scheduler"
	"github.com/emicklei/go-restful"
)

func main() {

	scheduler.Every(3).Minutes().Run(scheduledJob)

	restful.Add(resetfulService())
	log.Fatal(http.ListenAndServe(":5000", nil))

}

func resetfulService() *restful.WebService {
	ws := new(restful.WebService)
	ws.Path("/postjob").
	   Consumes(restful.MIME_JSON).
	   Produces(restful.MIME_JSON)

	ws.Route(ws.POST("/").To(postJob))

	return ws
}

func scheduledJob() {
	// do something here
}

func postJob(req *restful.Request, resp *restful.Response){
	// do something with HTTP POST method
}

```

### 参考

* [Setting Up Docker for Windows and WSL to Work Flawlessly](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)


{% include post_footer.md %}