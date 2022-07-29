# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import ScrapyDemo
import datetime
from ScrapyDemo.items import ScrapyBookUrlItem, ScrapyBookItem


class ScrapydemoPipeline:
    mysql=None
    coursor=None
    def open_spider(self,spider):
        self.mysql=pymysql.connect(host='localhost',user='root',password='123456',database='book')
        self.coursor=self.mysql.cursor()
        print("open_spider")

    def process_item(self, item, spider):
        table_name=item.table_name
        print(item.table_name)
        keys=list(item.keys())#['name','url']
        values=list(item.values())#['111','http://url.com']
        key_str=','.join('`%s`'%k for k in keys)
        print(key_str)#'`name`,`url`'
        values_str=','.join(["%s"] *len(values))
        print(values_str)#'%s,%s'
        update_str=','.join(["`{}`=%s".format(k) for k in keys])
        print(update_str)#"`name`=%s,`url=%s`"
        sql='insert into `{}`({}) values({}) on duplicate key update {}'.format(table_name,key_str,values_str,update_str)
        self.coursor.execute(sql,values*2)
        self.mysql.commit()
        #on duplicate key update 作用：
        #当向数据库插入新数据时：1.如果表中的主键或唯一约束对的值已经存在，则更新操作，否则就插入新数据，不更新。
        # insert=None
        # if type(item)==ScrapyBookUrlItem:
        #     insert = 'insert into bookurl(name,url,createtime) values("%s","%s","%s")' % (item['name'], item['url'],datetime.datetime.now())
        # elif type(item)==ScrapyBookItem:
        #     insert='insert into book(name,price,author,img_url,`desc`,createtime) values("%s","%d","%s","%s","%s","%s")'%(item['name'],item['price'],item['author'],item['img_url'],item['desc'],datetime.datetime.now())
        # print(insert)
        # if  insert is not None:
        #     self.coursor.execute(insert)
        #     self.mysql.commit()
        return item
    def close_spider(self,spider):
        self.coursor.close()
        self.mysql.close()