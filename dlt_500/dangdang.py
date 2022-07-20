from lxml import etree
import requests

url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1"
def join_list(item):
    """处理列表到字符串"""
    return "".join(item)

# HTML数据的实例化
response = requests.get(url=url, timeout=5)
html = etree.HTML(response.text)
items = html.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li")
print(items)

result_list = []
for item in items:
    # 图书的名称
    title = item.xpath(".//div[@class='name']/a/text()")
    # 图书评论
    comment = item.xpath(".//div[@class='star']/a/text()")
    # 推荐信息
    recommend = item.xpath(".//div[@class='star']/span[@class='tuijian']/text()")
    # 作者信息
    author = item.xpath(".//div[@class='publisher_info'][1]/a[1]/@title")
    # 出版时间
    publication_time = item.xpath(".//div[@class='publisher_info'][2]/span/text()")
    # 出版社
    press = item.xpath(".//div[@class='publisher_info'][2]/a/text()")
    # 五星评分
    score = item.xpath(".//div[@class='biaosheng']//text()")
    # 价格
    price = item.xpath(".//div[@class='price']/p[1]/span[1]/text()")
    # 折扣
    discount = item.xpath(".//div[@class='price']/p/span[@class='price_s']/text()")
    # 电子书价格
    e_book = item.xpath(".//div[@class='price']/p[@class='price_e']/span[@class='price_n']/text()")
    result_list.append(
        {
            "title": join_list(title),
            "comment": join_list(comment),
            "recommend": join_list(recommend),
            "author": join_list(author),
            "publication_time": join_list(publication_time),
            "press": join_list(press),
            "score": join_list(score),
            "price": join_list(price),
            "discount": join_list(discount),
            "e_booke": join_list(e_book)
        }
    )
print(result_list)

