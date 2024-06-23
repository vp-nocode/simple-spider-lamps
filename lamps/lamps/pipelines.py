# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class LampsPipeline:
    def open_spider(self, spider):
        self.file = open('lamps.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name', 'price', 'article', 'url'])


    def process_item(self, item, spider):
        self.writer.writerow([item['name'], item['price'], item['article'], item['url']])
        return item

    def close_spider(self, spider):
        self.file.close()
