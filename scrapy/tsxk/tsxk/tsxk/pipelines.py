# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class TsxkPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user='root', password='zjr', db="novelweb",
                                    charset="utf8")
        self.cursor = self.conn.cursor()
        self.cursor.execute("truncate table novelweb_tsxk")

    def process_item(self, item, spider):
        try:
            sql = 'insert into novelweb_tsxk (title,content,link) values ("%s","%s","%s")' % (
                item["title"], item["content"], item["link"])
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.conn.close()

