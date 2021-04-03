import scrapy
from ..items import ZimuItem


class ZimuSpiderSpider(scrapy.Spider):
    name = 'zimu_spider'
    allowed_domains = ['assrt.net/xml/list/sub']
    start_urls = []
    for i in range(1, 15):
        start_urls.append('http://assrt.net/xml/list/sub/?page=' + str(i))

    def parse(self, response):
        hrefs = response.selector.xpath('//div[@class="subitem"]//a[contains(@id,"downsubbtn")]/@onclick').extract()
        for url in hrefs:
            url_detail = "https://assrt.net"+url[33:-15]
            # dongt_filter必须设为true，不然无法爬取
            request = scrapy.Request(url=url_detail, callback=self.parse_url, dont_filter=True)

            yield request

    def parse_url(self, response):
        # 就是这个函数出错，下次直接从这里开始做
        body = response.body
        item = ZimuItem()
        url = response.url.split("?")[0]
        item["file_urls"] = url
        item["files"] = body

        return item




