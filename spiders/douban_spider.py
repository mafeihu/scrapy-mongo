import scrapy
from douban.items import DoubanItem
class DoubanSpiderSpider(scrapy.Spider):
    # 名称
    name = 'douban_spider'
    # 允许访问域名
    allowed_domains = ['movie.douban.com']
    # 入口域名
    start_urls = ['https://movie.douban.com/cinema/later/taiyuan']

    def parse(self, response):
        movie_list = response.xpath("//div[@id='showing-soon']/div")
        for i_item in movie_list:
            douban_item = DoubanItem()
            # douban_item['title'] = i_item.xpath(".//h3/text()").extract_first()
            # douban_item['src'] = i_item.xpath(".//a/@href/text()").extract_first()
            # douban_item['img'] = i_item.xpath(".//img/@src/text()").extract_first()
            douban_item['num'] = i_item.xpath(".//ul/li[@class='dt last']/span/text()").extract_first()
            douban_item['play_date'] = i_item.xpath('.//ul/li[1]/text()').extract_first()
            yield douban_item









