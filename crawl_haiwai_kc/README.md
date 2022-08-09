## 前期准备

### requirements

```sh
$ pipreqs ./ --encoding=utf-8
```


### test
```
source crawl_venv/bin/activate && cd crawl_haiwai_kc
scrapy crawl bandai
scrapy crawl yahoo
scrapy crawl rakuten
scrapy crawl yodobashi
```

|           | 本地库(response_received_count,scheduler/enqueued,second) | RDS库(url,second) |
| --------- | --------------------------------------------------------- | ----------------- |
| bandai    | (8,8,1)                                                   | (8,8,5) done      |
| yahoo     | (19,19,3)                                                 | done              |
| rakuten   | (16, 16,7)                                                | (16,16,76/17/3)   |
| yodobashi | (6,7,12)                                                  | done              |



### 虚拟环境

在 python3 中，虚拟环境由标准库中的 venv 包原生支持，创建venv虚拟环境的命令格式如下：
```python3 -m venv virtual-environment-name```
-m venv 选项的作用是以独立的脚本运行标准库中的 venv 包，后面的参数为虚拟环境的名称。
本例子为创建一个名为 venv 的虚拟环境，命令如下：
`python3 -m venv venv`

若想使用虚拟环境，要先将其“激活”，命令如下：
`source venv/bin/activate`

windows“激活”示例：
```
>cd venv\Scripts
>actives
```
为了提醒你已经激活了虚拟环境，激活虚拟环境的命令会修改命令提示符，加入环境名：
(venv) [root@localhost py]#
虚拟环境中的工作结束后，在命令提示符中输入 deactivate，还原当前终端会话的 PATH 环境变量，把命令提示符重置为最初的状态。 

## 部署

因为Rakuten、Yodobashi这两个平台不能使用日本网络访问，故部署在*window 环境*，使用VPN代理访问

其他平台放在*linux 环境*

### 设置定时

#### linux 环境

```
## haiwai mode:dev,freq_min 23
*/23 * * * crawl cd /home/crawl/crawl && source crawl_venv/bin/activate && cd crawl_haiwai_kc &&python run.py -mode MASTER -freq_min 23
```

#### window 环境

在部署服务器上：C:\Users\crawl\Documents\cmd 文件夹，新建bat

```
echo starting
cd C:\Users\crawl\Documents\code\crawl_haiwai_kc
python run.py -mode MASTER -freq_min 23	
```

函数解析：

run.py 为入口函数

mode 为环境，MASTER:生产环境，TEST：测试环境。

freq_min，频率/分钟:2，23，59，113。目前只支持以上4种频率。

### 追加数据

数据格式：必须按照crawl_haiwai_kc.xlsx文件的格式
platform/平台:bandai、rakuten、yahoo、yodobashi
frequency/分钟:2，23，59，113。目前只支持以上4种频率。

####  注意！！
不能随意更改crawl_haiwai_kc.xlsx文件名、excel表格里面的列名,并按照对应的字段名输入值。

路径：D:\海外在库侦察

##### 文件作用
crawl_haiwai_kc.xlsx 为需要侦测的列表，4个平台。

#####  操作流程
1. 在crawl_haiwai_kc.xlsx文件追加和删除对应的 id序号(唯一)、url链接、platform平台、frequency频率（分钟）

   **请确保url为有效并对应你想要的商品的url。**

   修改完成，保存。

2. 双击run.bat

   出现以下文字即可，请按任意键退出。

   ```sh
   执行中....
   =========================================
   host is pgm-7xvxqc0s20mkh7f92o.pg.rds.aliyuncs.com
   update successful !
   =========================================
   host is 172.18.210.138
   update successful !
   按任意键结束 run.bat
   请按任意键继续. . .
   ```

---
   
# 日期：2022年7月26日
经与老刘协商，由于windows机器到期问题，且Rakuten、Yodobashi这两个需要windows环境执行的检测平台一直没咋用，几乎只检测bandai。所以先暂时迁移到docker容器平台到linux机器里面运行。