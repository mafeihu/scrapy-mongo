# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymongo
import pymysql
from douban.settings import mongo_host, mongo_port, mongo_dbname, mongo_db_collection, mysql_host, mysql_port, mysql_dbname, mysql_username, mysql_password
class DoubanPipeline:
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_dbname
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

class DoubanMysqlPipeline:
    def __init__(self):
        host = mysql_host
        port = mysql_port
        dbname = mysql_dbname
        username = mysql_username
        password = mysql_password
        self.db_conn = pymysql.connect(host=host, port=port, db=dbname, user=username, passwd=password, charset='utf8')
        self.db_cur = self.db_conn.cursor()
    def process_item(self, item, spider):
        sql = """insert into douban_movie(serial_number, movie_name, introduce, star, evaluate, des) VALUES (%s, %s, %s, %s, %s, %s)"""
        lis = (item['serial_number'], item['movie_name'], item['introduce'], item['star'], item['evaluate'], item['describe'])

        self.db_cur.execute(sql, lis)

        try:
            print(sql)
            self.db_cur.execute(sql, lis)
        except Exception as e:

            var = "Insert error:", e
            print(var)
            self.db_conn.rollback()
        else:
            self.db_conn.commit()
            gi
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.db_cur.close()
        self.db_conn.close()





