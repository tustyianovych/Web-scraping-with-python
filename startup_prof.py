import scrapy
import json
from scrapy.crawler import CrawlerProcess


class Startups(scrapy.Spider):
    name = 'startup'
    base_url = 'https://e27.co/startups/load_startups_ajax?all&per_page={}'
    start_urls =[startup_urls]
    for i in range(1,100):
        all_urls = base_url.format(i)
        start_urls.append(all_urls)
    
    def parse(self, response):
        json_data = json.loads(response.body.decode())
        selector = scrapy.Selector(text=json_data['pagecontent'])
        urls = selector.xpath('//div[@class="col-xs-12 col-sm-12 col-md-4 col-lg-4"]/a/@href').extract()
        for i in urls:
            yield {
                'url' : i,
                }