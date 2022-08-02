### 1.查看所有容器（包括未运行的）
```
docker ps -a
```

### 2.例子
```
[root@localhost liucheng]# docker run -it -p 8760:8760 --rm --name docker_yl_maersk_cosco -v "/home/liucheng/code/:/data" --shm-size="2g" -d yl_cosco_maersk:1.0.2 sh start.sh
命令解读：
                     docker run ==> 创建并运行一个容器
                            -it ==> 交互模式
                   -p 8760:8760 ==> 端口映射，宿主机端口:容器端口
   -name docker_yl_maersk_cosco ==> 容器名称
-v "/home/liucheng/code/:/data" ==> 将容器内指定文件挂载到了宿主机对应位置，宿主机文件存储位置:容器内文件位置
                --shm-size="2g" ==> 修改docker的共享内存大小
                             -d ==> 守护进程启动方式
          yl_cosco_maersk:1.0.2 ==> 这是镜像，仓库名:tag
                    sh start.sh ==> 进入容器后执行的shell脚本
```
```
其他参数：
--restart=always：该容器随docker服务启动而自动启动
```

### 3.容器的启动、停止、重启
```
docker start/top 容器名或容器ID
```

### 4.进入容器
```
docker exec -it 容器名或容器ID /bin/bash
docker exec -it 容器名或容器ID sh
```

### 5.查看自己服务器中docker镜像列表
```
docker images
```

### 6.创建镜像
```
docker build
--tag, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。

docker build -t runoob/ubuntu:v1 .  #使用当前目录的 Dockerfile 创建镜像，标签为 runoob/ubuntu:v1
docker build -f /path/to/a/Dockerfile .   #-f 指定Dockerfile的路径
```

### 7.拉取镜像
```
docker pull 镜像名 
docker pull 镜像名:tag
```

### 8.删除镜像
```
#删除一个
docker rmi -f 镜像名/镜像ID

#删除多个 其镜像ID或镜像用用空格隔开即可 
docker rmi -f 镜像名/镜像ID 镜像名/镜像ID 镜像名/镜像ID

#删除全部镜像  -a 意思为显示全部, -q 意思为只显示ID
docker rmi -f $(docker images -aq)
```

### 9.上传镜像docker hub
```
1.docker ps -a #查看容器 得到container id

2.docker login #登录docker 输入账号密码

3.docker commit -m "提交信息" -a "作者" 容器id 仓库名称:标签
docker commit -m "python爬虫_船运公司订舱" -a "liucheng" 6ba61940c039 liuchengelse/prokect:python_spider_boat

4.docker push liuchengelse/project:v1.0.0
```

### 10.dockerfile
```
8.Dockerfile #Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。
例子：
FROM nginx
RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html

说明：
FROM：定制的镜像都是基于 FROM 的镜像，这里的 nginx 就是定制需要的基础镜像。后续的操作都是基于 nginx。
RUN：用于执行后面跟着的命令行命令，有以下俩种格式：
(1)shell 格式:
RUN <命令行命令>  #<命令行命令> 等同于，在终端操作的 shell 命令。
(2)exec 格式:
RUN ["可执行文件", "参数1", "参数2"]  #RUN ["./test.php", "dev", "offline"] 等价于 RUN ./test.php dev offline

指令详解：
COPY #复制指令，从上下文目录中复制文件或者目录到容器里指定路径
COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
<源路径>：源文件或者源目录，这里可以是通配符表达式，其通配符规则要满足 Go 的 filepath.Match 规则
<目标路径>：容器内的指定路径，该路径不用事先建好，路径不存在的话，会自动创建

ADD 指令和 COPY 的使用格类似（同样需求下，官方推荐使用 COPY）

CMD 
类似于 RUN 指令，用于运行程序，但二者运行的时间点不同:
CMD 在docker run 时运行。
RUN 是在 docker build。
```
