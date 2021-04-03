# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class ZimuPipeline(FilesPipeline):

    # def file_path(self, request, response=None, info=None):
    #
    #     file_name = request.url.replace('/', '_').replace(':', '_')
    #     folder_name = "../result/download/files/"
    #     return folder_name + file_name

    def process_item(self, item, spider):
        url = item['file_urls']
        file_name = url.replace('/', '_').replace(':', '_')
        # print(file_name)
        fp = open('../result/download/files/' + file_name, 'wb')
        fp.write(item["files"])
        fp.close()
        return item



