# 引用sqlalchemy模块
from sqlalchemy import exc
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from 万代监测库存.items import HaiwaikcORM, HaiwaikcscORM

import traceback
import sys


class SqlalchemyPipeline(object):
    """
        使用Sqlalchemy 模块 读写数据库
        自适应数据库：Mysql,Postgresql
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        方法为类方法，通过初始化crawler对象返回Pipeline实例，我们可以通过crawler返回所有scrapy核心组件。
        : crawler : crawl配置
        # """
        print('now is SqlalchemyPipeline --- from_crawl')

        # _db_type = 'PG'
        _db_type = crawler.settings.get('DB_TYPE', 'PG')
        _db_config = crawler.settings.get(
            '%s_CONFIG' % (crawler.spider.mode))['%s_CONFIG' % (_db_type)]
        return cls(_db_type, _db_config)

    def __init__(self, _db_type, _db_config):
        """
        @description  :
         初始化函数
        @param  :
            _db_config: 数据库配置参数
        @Returns  :
            None
        """
        print('now is SqlalchemyPipeline --- __init__')
        _db_config['drivername'] = self._choose_db_dialect_driver(_db_type)
        dsn = URL(**_db_config)
        self.db_engine = create_engine(dsn)

    def open_spider(self, spider):
        """
        爬虫开始运行时，将会在这个方法中执行一些初始化工作，例如打开数据库、打开文件等。
        :param spider : 正在打开的spider
        :return
        """
        spider.logger.debug('Spider:%s className: %s, function: %s' % (
            spider.name, self.__class__.__name__, 'open_spider'))
        # spider.logger.debug(
        #     'param spider have attr {spider}'.format(spider=dir(spider)))
        # 测试数据是否能链接
        try:
            tmp = self.db_engine.connect()
            tmp.close()
        except Exception as error:
            # print(dir(spider.logger))
            spider.logger.critical(
                'engine:{engine} have some woring'.format(engine=self.db_engine))
            # 什么错误
            # error = e
            # 错误类型
            etype = sys.exc_info()[0:2]
            spider.logger.critical(
                'etype:{etype}, error:{error}'.format(etype=etype, error=error))
            spider.exception_message.add(error)
            # exit(1)

        self.db_SessionFactory = sessionmaker(bind=self.db_engine)
        # spider.logger.debug(
        #     'param self.db_SessionFactory have attr {spider}'.format(spider=dir(self.db_SessionFactory)))

        # 创建 一个指定的 Session 类实例
        self.SqlalchemyPipeline_session = self.db_SessionFactory()
        spider.logger.debug('SqlalchemyPipeline_session id is %s' %
                            id(self.SqlalchemyPipeline_session))

        # self.cache = self.SqlalchemyPipeline_session.query(
        #     HaiwaikcscORM.goods_status).group_by(HaiwaikcscORM.goods_id)
        # spider.logger.debug('SqlalchemyPipeline_session have attr %s' %
        #                     dir(self.SqlalchemyPipeline_session))

        # 最新状态的数据
        # select goods_id,max(thedate),goods_status from crawl_haiwai_kc_sc group by goods_id,goods_status ORDER BY goods_id DESC;
        self.cache = self.SqlalchemyPipeline_session.query(HaiwaikcscORM.goods_id, func.max(
            HaiwaikcscORM.thedate), HaiwaikcscORM.goods_status).group_by(HaiwaikcscORM.goods_id, HaiwaikcscORM.goods_status)

        # self.SqlalchemyPipeline_session.commit()
        # 将成功的统一的数据库连接池 发送到spider外面
        spider.db_SessionFactory = self.db_SessionFactory

    def process_item(self, item, spider):
        """
        该方法必须实现，处理数据的工作都在这个方法中进行，方法返回 dict 、Item 、 Twisted Deferred 或者是 DropItem 异常。
        :param item : 被爬取的 Item ；
        :param spider : 爬取 Item 时所使用的 Spider 。
        :return item
        Tip : 如果在 process_item 方法中丢弃了 Item ，那么这个 Item 将不会向后续 Pipeline 传递这个 Item 。
        """
        # print(item)
        # # 查询最近一条数据的状态
        # goodsid, thedate, p_status = self.cache.filter(
        #     HaiwaikcscORM.goods_id == item['goods_id']).first()
        tmp = self.cache.filter(
            HaiwaikcscORM.goods_id == item['goods_id']).all()
        # p_status = self.SqlalchemyPipeline_session.query(
        #     HaiwaikcscORM.goods_status).filter(HaiwaikcscORM.goods_id == item['goods_id']).order_by(HaiwaikcscORM.thedate.desc()).first()
        if tmp:
            p_status = max(tmp)[2]
        else:
            # 初始状态 -2
            p_status = -2

        # # 对比前后瞬态
        if item["goods_status"] == p_status:
            spider.logger.info('商品id:{goods_id}, 前{p_status}, 后:{t_status},状态码没变，不用发送通知'.format(goods_id=item['goods_id'],
                                                                                                p_status=p_status, t_status=item["goods_status"]))
        else:
            if p_status == -1 and item["goods_status"] == 0:
                state = '已修正，加入侦测队列中,现无货'
            elif p_status == -1 and item["goods_status"] == 1:
                state = '已修正，加入侦测队列中,现有货'
            elif p_status == 0 and item["goods_status"] == -1:
                state = 'Error,url:{url}'.format(url=item['goods_url'])
                spider.invalid_num += 1
            elif p_status == 0 and item["goods_status"] == 1:
                state = '有货'
            elif p_status == 1 and item["goods_status"] == -1:
                state = 'Error,url:{url}'.format(url=item['goods_url'])
                spider.invalid_num += 1
            elif p_status == 1 and item["goods_status"] == 0:
                state = '没货'
            elif item["goods_status"] == 0:
                state = '第一次加入侦测队列中，现没货'
                pass
            elif item["goods_status"] == 1:
                state = '第一次加入侦测队列中，现有货'
                pass
            elif item["goods_status"] == -1:
                state = 'Error,url:{url}'.format(url=item['goods_url'])
                spider.invalid_num += 1
                pass
            else:
                state = 'p_status 值为：{} ，不属于之前定义的值，请检查流程和定义，做出修正'.format(
                    p_status)
            spider.exchage_num += 1
            message = '- 商品名: {goods_name}\n#### [状态:{state}]({url})\n###### 时间：{str_time}\n'.format(
                goods_name=item['goods_name'], state=state, str_time=item["thedate"], url=item['goods_url'])
            # spider.cache_message = spider.cache_message.join(message)
            spider.cache_message = spider.cache_message + message

        # 追加到新的数据上
        tmp = HaiwaikcscORM(**item)
        try:
            self.SqlalchemyPipeline_session.add(tmp)
            self.SqlalchemyPipeline_session.commit()
            spider.logger.debug('插入1个')
        except exc.SQLAlchemyError as error:
            spider.exception_message.add(error.args[0])
            self.SqlalchemyPipeline_session.rollback()
            spider.logger.critical(
                'SqlalchemyPipeline_session rollback, its commit error:{error}'.format(error=error))

        return item

    def _choose_db_dialect_driver(self, _db_type):
        """
        @description  :
            一个标准的链接URL是这样的：dialect+driver://username:password@host:port/database
            dialect，是数据库类型，大概包括：sqlite, mysql, postgresql, oracle, or mssql.
            driver，是使用的数据库API，驱动，连接包，随便叫什么吧。
        @param  :
            str: _db_type : 数据库类型
        @Returns  :
            str：dialect+driver
        """
        built_in_db_dialect_driver = {
            'PG': 'postgresql+psycopg2',
            'MYSQL': 'mysql+pymysql',
        }
        return built_in_db_dialect_driver.get(_db_type)

    def close_spider(self, spider):
        """
        爬虫关闭时，将会在这个方法执行一些后续工作，比如关闭数据库、关闭文件等。
        :param spider : 当前使用的spider
        : return
        """
        spider.logger.debug('Spider:%s className: %s, function: %s' % (
            spider.name, self.__class__.__name__, 'close_spider'))
        # spider.logger.debug(
        #     'param spider have attr {spider}'.format(spider=dir(spider)))

        self.SqlalchemyPipeline_session.close()
        spider.logger.info('SqlalchemyPipeline_session close')
