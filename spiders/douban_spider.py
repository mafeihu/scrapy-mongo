import scrapy
from douban.items import DoubanItem
class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    #默认解析方法
    def parse(self, response):
        # 循环电影条目
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            # item文件导进来
            douban_item = DoubanItem()
            # 写详细的xpath,进行数据的解析
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath("./div/div[2]/div[1]/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            # 数据的处理
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//div[@class='bd']/p[@class='quote']/span/text()").extract_first()
            # 需要将数据yield到pipelines里面去
            yield douban_item
        #解析下一页规则,取后一页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)

















