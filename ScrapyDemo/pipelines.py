# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import ScrapyDemo
import datetime
from ScrapyDemo.items import ScrapyItem, ScrapydemoItem


class ScrapydemoPipeline:
    mysql=None
    coursor=None
    def open_spider(self,spider):
        self.mysql=pymysql.connect(host='localhost',user='root',password='123456',database='book')
        self.coursor=self.mysql.cursor()
        print("open_spider")

    def process_item(self, item, spider):
        print(item)
        insert=None
        if type(item)==ScrapyItem:
            print(item['name'])
        elif type(item)==ScrapydemoItem:
            insert='insert into book(name,price,author,img_url,`desc`,createtime) values("%s","%d","%s","%s","%s","%s")'%(item['name'],item['price'],item['author'],item['img_url'],item['desc'],datetime.datetime.now())
        print(insert)
        if  insert is not None:
            self.coursor.execute(insert)
            self.mysql.commit()
        return item
    def close_spider(self,spider):
        self.coursor.close()
        self.mysql.close()