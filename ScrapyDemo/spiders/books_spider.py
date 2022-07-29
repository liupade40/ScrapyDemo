import scrapy

from ScrapyDemo.items import ScrapyBookItem,ScrapyBookUrlItem
import datetime

class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            'https://book.douban.com/latest?tag=%E5%8E%86%E5%8F%B2%E6%96%87%E5%8C%96',
            'https://book.douban.com/latest?subcat=%E5%8E%86%E5%8F%B2%E6%96%87%E5%8C%96&p=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(1,20):
            url=response.xpath('//*[@id="content"]/div/div[1]/ul/li[' + str(i) + ']/div[2]/h2/a/@href').extract()[0]
            name=response.xpath('//*[@id="content"]/div/div[1]/ul/li[' + str(i) + ']/div[2]/h2/a/text()').extract()[0]
            yield scrapy.Request(url=url,callback=self.detailparse)
            item = ScrapyBookUrlItem()
            item['name']=name
            item['url']=url
            item['createtime']=datetime.datetime.now()
            yield item

    def detailparse(self,response):
        item= ScrapyBookItem()
        item['name']=response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0]
        item['author']=response.xpath('//*[@id="info"]/span[1]/a/text()').extract()[0]
        item['price']=0
        item['img_url']=response.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
        item['desc']='暂无'
        item['createtime'] = datetime.datetime.now()
        yield item
