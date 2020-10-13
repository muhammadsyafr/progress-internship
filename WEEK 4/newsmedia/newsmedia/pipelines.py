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
            id INT(99),
            title varchar(255),
            url text,
            tanggal text
        )""")

        self.curr.execute("""DROP TABLE IF EXISTS tbl_news_detail""")
        self.curr.execute("""create table tbl_news_detail(
            id int,
            title text,
            img_url text,
            time text,
            categories text,
            tags text,
            content text
        )""")
          
    def process_item(self, item, spider):
        # print('WOIIIIIIIIIIIIIIIIIIIIIIIIi', type(item))
        self.store_db(item)
        return item 
    
    def store_db(self, item):
        self.curr.execute("""insert into tbl_news values (%s, %s, %s, %s)""", (
            12121 + 122, #diganti id unique
            item['title'][0],
            item['link_url'],
            item['time'],
        ))

        self.curr.execute("""insert into tbl_news_detail values (%s, %s, %s, %s, %s, %s, %s)""", (
            12121 + 122, #diganti id unique
            item['title'][0],
            item['img'],
            item['time'],
            item['categories'],
            item['tags'],
            item['content'],
        ))
        self.conn.commit()




