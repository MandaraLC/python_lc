'''
1.scrapy框架
（1）Scrapy Engine（引擎）：负责Spider、Item Pipeline、Downloader、Scheduler之间的通讯，包括信号和数据的传递等。

（2）Scheduler（调度器）：负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列和入队，当引擎需要时，交还给引擎。

（3）Downloader（下载器）：负责下载Scrapy Engine（引擎）发送的所有Requests（请求），并将其获取到的Responses（响应）交还给Scrapy Engine（引擎），由引擎交给Spider来处理。

（4）Spiders（爬虫）：负责处理所有Responses，从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler（调度器）。

（5）Item Pipeline（管道）：负责处理Spiders中获取到的Item数据，并进行后期处理（详细分析、过滤、存储等）。

（6）Downloader Middlewares（下载中间件）：是一个可以自定义扩展下载功能的组件。

（7）Spider Middlewares（Spider中间件）：是一个可以自定义扩展Scrapy Engine和Spiders中间通信的功能组件（比如进入Spiders的Responses和从Spiders出去的Requests）。


'''