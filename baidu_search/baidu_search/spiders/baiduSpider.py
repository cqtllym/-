import scrapy
from w3lib.html import remove_tags

class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'baiduSpider'  # 一定要存在
    # 允许爬虫的范围
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=机器学习']

    # def parse(self, response):
    #     # 抓取后写入result中
    #     filename = "../result/result.html"
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        # 获取包含"c-container"的div
        containers = response.selector.xpath('//div[contains(@class, "c-container")]')
        for container in containers:
            # 获取href，返回为list，只存在空或非空的两种情况
            href = container.xpath('h3/a/@href').extract()
            href_detail = ""
            # 如果不为空，则取出其中的信息
            if len(href) > 0:
                href_detail = href[0]

            # 获取该结果的标题，此时包含着多余标签信息，返回为list，只存在空或非空的两种情况
            title = container.xpath('h3/a').extract()
            title_detail = ""
            # 如果不为空的进行除去标签处理
            if len(title) > 0:
                title_detail = remove_tags(title[0])

            # 获取该结果简介，此时包含着多余标签信息，返回为list，只存在空或非空的两种情况
            c_abstract = container.xpath('div/div/div[contains(@class, "c-abstract")]').extract()
            abstract = ""
            if len(c_abstract) > 0:
                abstract = remove_tags(c_abstract[0])

            # 通过Request传进去，通过Request的请求结果response取出来，取出方法与字典一样
            # 因为request返回是以url为键，所以，此时应该除去url为空的数据，仅返回有用数据
            if len(href_detail) > 0:
                request = scrapy.Request(url=href_detail, callback=self.parse_url)
                # Request中有个meta参数，用来传递信息，传递信息的格式必须是一个字典类型
                request.meta['title'] = title_detail
                request.meta['abstract'] = abstract
                yield request

    def parse_url(self, response):
        print("url:", response.url)
        print("title:", response.meta['title'])
        print("abstract:", response.meta['abstract'])
        content = remove_tags(response.selector.xpath('//body').extract()[0])
        print("content_len:", len(content))
