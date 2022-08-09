# Scrapy settings for crawl_haiwai_kc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawl_haiwai_kc'

SPIDER_MODULES = ['crawl_haiwai_kc.spiders']
NEWSPIDER_MODULE = 'crawl_haiwai_kc.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'crawl_haiwai_kc (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 3

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'crawl_haiwai_kc.middlewares.CrawlHaiwaiKcSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'crawl_haiwai_kc.middlewares.CrawlHaiwaiKcDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'crawl_haiwai_kc.pipelines.CrawlHaiwaiKcPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


DEV_CONFIG = {
    'PG_CONFIG': {
        'host': 'pgm-7xvxqc0s20mkh7f92o.pg.rds.aliyuncs.com',  # 地址  # 生产环境
        'username': 'crawl_haiwai_kc',  # 用户名
        'password': 'Crawl_Haiwai_KC@#123',  # 密码
        'port': '1921',  # 端口号
        'database': 'crawl_haiwai',  # 数据库名
        # 'query': {'options': '-c search_path=ingram_test'} # 模式
    },
    'DINGTALK_BIS_WEBHOOK': 'https://oapi.dingtalk.com/robot/send?access_token=68eebf3cfb451c5a2e396776b0b0f562209e2f71ee9e27fd49db6b0be7be5d3c',
    'DINGTALK_BIS_SECRET': 'SECc5cf0c86fb713bf0e7e6f644a788a8b09c60aec1ed73e120723ce4a3619bc5cf',
    'BIS_AT_MOBILES': ['13450495046'],

    #将错误推送到报错群
    'DINGTALK_DEVER_WEBHOOK': 'https://oapi.dingtalk.com/robot/send?access_token=48e527a6f883d558cd6a41e39589ddf6037f757c2032ffb8aa7ca0ded6fd3662',
    'DINGTALK_DEVER_SECRET': 'SEC45ac3158f2f0a6cc0f7e9c17b20edfa07a93c72a4bc5220fb698089fe341db6e',
    'DEVER_AT_MOBILES': ['15112476096'],
}


MASTER_CONFIG = {
    'PG_CONFIG': {
        'host': 'pgm-7xvxqc0s20mkh7f92o.pg.rds.aliyuncs.com',  # 地址  # 生产环境
        'username': 'crawl_haiwai_kc',  # 用户名
        'password': 'Crawl_Haiwai_KC@#123',  # 密码
        'port': '1921',  # 端口号
        'database': 'crawl_haiwai',  # 数据库名
        # 'query': {'options': '-c search_path=ingram_test'} # 模式
    },
    'DINGTALK_BIS_WEBHOOK': 'https://oapi.dingtalk.com/robot/send?access_token=68eebf3cfb451c5a2e396776b0b0f562209e2f71ee9e27fd49db6b0be7be5d3c',
    'DINGTALK_BIS_SECRET': 'SECc5cf0c86fb713bf0e7e6f644a788a8b09c60aec1ed73e120723ce4a3619bc5cf',
    'BIS_AT_MOBILES': ['13450495046'],

    #将错误推送到报错群
    'DINGTALK_DEVER_WEBHOOK': 'https://oapi.dingtalk.com/robot/send?access_token=48e527a6f883d558cd6a41e39589ddf6037f757c2032ffb8aa7ca0ded6fd3662',
    'DINGTALK_DEVER_SECRET': 'SEC45ac3158f2f0a6cc0f7e9c17b20edfa07a93c72a4bc5220fb698089fe341db6e',
    'DEVER_AT_MOBILES': ['15112476096'],
}
