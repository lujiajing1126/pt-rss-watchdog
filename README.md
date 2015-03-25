# pt-rss-watchdog

> 项目主要有两部分组成，爬虫部分和网站部分，爬虫部分是由python写的，以守护进程方式启动；网站部分是Rails，主要是Api接口和网页，以及客户端推送

## Install

### python

```
$ cd services
$ pip install -r requirements.txt
```

### ruby

> 推荐RVM或者rbenv方式安装ruby
> 
> 以及，你应该正确安装mongodb和redis
> 
> Python 服务同时也依赖redis和rails的api

```
$ cd ptrss
$ ruby -v
ruby 2.1.2p95 (2014-05-08 revision 45877) [x86_64-darwin13.0]
$ bundle install
```

## Start

For rails

```
$ (sudo) mongodb --dbpath=/data/mongdb
$ nohup redis-server&
$ rails s
```

For python service

```
python server.py start
```

在Service目录下有service.log日志文件用于排查错误和其他debug信息

## Develop

### Debug

For rails, use `pry-nav`

在代码中加入

```
binding.pry
```
可以自动卡断点调试

### Doc

For rails ,use `swagger` to show docs

```
http://localhost:3000/doc
```

## TODO

[] api接口在收到新的torrent的时候异步发出消息
[] 用户系统
[] HTML-Mobile页面
[] 集成Sidekiq和消息推送
[] 自定义过滤器

## Contribution

**MUST** Ref to `Git-Flow` Branching Model before you plan to contibute sth

### Warning

- Please use `CoffeeScript` and `SCSS`
- Please use `slim` template engine