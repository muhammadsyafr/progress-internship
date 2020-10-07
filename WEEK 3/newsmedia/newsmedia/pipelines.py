from itemadapter import ItemAdapter
import mysql.connector

class NewsMediaPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'scrapy_kompas'
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tbl_news""")
        self.curr.execute("""create table tbl_news(
            id int,
            title text,
            time text,
            categories text,
            content text 
        )""")
          

    def process_item(self, item, spider):
        # print('WOIIIIIIIIIIIIIIIIIIIIIIIIi', type(item))
        # self.store_db(item)
        # self.store_db_detail(item)
        print(item)
        return item 
    
    def store_db(self, item):
        self.curr.execute("""insert into tbl_news values (%s, %s, %s, %s, %s)""", (
            12121 + 122, #diganti id unique
            item['title'][0],
            item['time'][0],
            item['categories'][0],
            item['content'][3],
        ))
        self.conn.commit()

    def store_db_detail(self, item):
        self.curr.execute("""insert into tbl_news_detail values (%s, %s, %s, %s, %s)""", (
            12121 + 122, #diganti id unique
            item['title'][0],
            item['time'][0],
            item['content'][0],
        ))
        self.conn.commit()

