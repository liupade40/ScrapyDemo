from scrapy.cmdline import execute
#excute 执行scrapy命令
import os  # 用来设置路径
import sys   # 调用系统环境，就如同cmd中执行命令一样
execute(["scrapy", "crawl", "books"])