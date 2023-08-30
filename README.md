# SCM ES Service

本服务负责提供所有 `SCM` 相关的Elastic Search搜索接口.

## 开始使用

1. 安装依赖:
   
   `$ pip -r requirement.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

2. 启动服务:
   
   `$ python manage.py run` 
   
    在8000端口启动
   
   `$ python manage.py run_worker es_scm_queue_0` 
   
    启动redis 队列


3. 构建数据:
   
   `$ python build_es_mapping` 
   
    构建 es 索引， -i 加索引名称build指定索引
    例如 python manage.py build_es_mapping -i requirement
   
   `$ python es_migrate` 
   
    构建 es 数据， -i 加参数 i构建指定索引数据 -s 起始时间 -e结束时间
    例如 python manage.py es_migrate -i requirement -s 2021-01-01 -e 2021-12-31


4. 使用服务:
   
   启动服务后本地直接登陆 http://127.0.0.1:8000 登陆swagger 调用接口数据 
   rq dashbroad:http://127.0.0.1:8000/rq 查看redis rq 内job情况

## 环境配置

1. 测试环境: http://39.100.109.203:8097
2. demo环境: http://39.100.109.203:6097
3. uat环境: http://39.100.109.203:7097
4. 生产环境: http://47.92.89.139:7097

## 单元测试

1. 测试前要连接vpn 保证能够访问 39.100.143.4:9200 ElasticSearch服务。

2. 启动redis:
   
   mac&linux `$ nohup redis-server &`
   
   windows `$ redis-server.exe redis.conf`   
   
2. 环境变量设置:
   
   `$ export RUNTIME_ENV=unittest`

2. 启动服务:

   `$ python manage.py run`

3. 开始测试:

    `$ make tests`
4. 查看结果:
   
    开始单元测试并检测 数据构建es功能，es数据增删改查当完成单元测试后检测是否有结果为 F并查看报错信息。当全部通过后会显示整体覆盖率，应尽可能根据
    实际业务情况构建测试数据提升覆盖率。