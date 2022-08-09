# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from sqlalchemy import Column, String, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
import scrapy


class OutputItem(scrapy.Item):
    thedate = scrapy.Field()  # 获取商品时间
    goods_name = scrapy.Field()  # 商品名称
    goods_status = scrapy.Field()  # 商品状态 0:无 1:有 -1:未知错误
    goods_id = scrapy.Field()  # 商品在数据库的id
    goods_url = scrapy.Field()  # 商品链接


# 映射基类
Base = declarative_base()
# 具体映射类


class HaiwaikcscORM(Base):
    __tablename__ = 'crawl_haiwai_kc_sc'
    # __table_args__ = {"mysql_charset": "utf8"}
    # id = Column(Integer, primary_key=True, nullable=False)
    goods_id = Column(SmallInteger(), primary_key=True, nullable=False)
    thedate = Column(DateTime(), primary_key=True)
    goods_url = Column(String(255), nullable=False)
    goods_status = Column(SmallInteger(), nullable=False)
    goods_name = Column(String(255), nullable=False)


class HaiwaikcORM(Base):
    __tablename__ = 'crawl_haiwai_kc'
    # __table_args__ = {"mysql_charset": "utf8"}
    id = Column(SmallInteger(), primary_key=True, nullable=False)
    url = Column(String(255), nullable=False)
    platform = Column(String(255), nullable=False)
    frequency = Column(SmallInteger(), nullable=False)
