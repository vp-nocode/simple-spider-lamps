import scrapy
from lamps.items import LampsItem


class SpiderLampsSpider(scrapy.Spider):
    name = "spider-lamps"
    allowed_domains = ["atlantsnab.ru"]
    start_urls = ["https://atlantsnab.ru/catalog/istochniki-sveta/"]

    def parse(self, response):
        lamps = response.css('div.product-text-wrap.d-flex.flex-column')
        for lamp in lamps:
            # yield {
            #    'name': lamp.css('a.description.w-100.itempropname').attrib['title'],
            #    # 'name' : lamp.css('a.description.w-100.itempropname::text').get().strip()
            #    'price': lamp.css('div.pt-3.w-100 span::text').get().strip(),
            #    'article': lamp.css('a.sku::text').get().strip(),
            #    'url': lamp.css('a.description.w-100.itempropname').attrib['href']
            # }
            item = LampsItem()
            item['name'] = lamp.css('a.description.w-100.itempropname').attrib['title']
            item['price'] = lamp.css('div.pt-3.w-100 span::text').get().strip()
            item['article'] = lamp.css('a.sku::text').get().strip()
            item['url'] = lamp.css('a.description.w-100.itempropname').attrib['href']
            yield item
