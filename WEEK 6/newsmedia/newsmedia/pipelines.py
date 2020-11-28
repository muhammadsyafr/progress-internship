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
            database = 'scrapy_kompas1'
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tbl_news""")
        self.curr.execute("""create table tbl_news(
            id int,
            title text,
            url text,
            tanggal text
        )""")
        self.curr.execute("""ALTER TABLE `tbl_news` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`)""")

        self.curr.execute("""DROP TABLE IF EXISTS tbl_news_detail""")
        self.curr.execute("""create table tbl_news_detail(
            id int,
            id_detail_news int,
            title text,
            img_url text,
            time text,
            categories text,
            tags text,
            content text
        )""")
        self.curr.execute("""ALTER TABLE `tbl_news_detail` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`)""")
        # self.curr.execute("""ALTER TABLE `tbl_news` ADD CONSTRAINT `relation_news` FOREIGN KEY (`id`) REFERENCES `tbl_news_detail`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT""")
          
    def process_item(self, item, spider):
        self.store_db(item)
        return item 
    
    def store_db(self, item):
        # self.curr.execute("""insert into tbl_news values (%s, %s, %s, %s)""", (
        self.curr.execute("""INSERT into tbl_news(title, url, tanggal) VALUES(%s, %s, %s)""", (
            item['title'][0],
            item['link_url'],
            item['time'],
        ))

        # self.curr.execute("""insert into tbl_news_detail values (%s, %s, %s, %s, %s, %s, %s)""", (
        self.curr.execute("""INSERT into tbl_news_detail(title, img_url, time, categories, tags, content) VALUES(%s, %s, %s, %s, %s, %s)""", (
            item['title'][0],
            item['img'],
            item['time'],
            item['categories'],
            item['tags'],
            item['content'],
        ))
        self.conn.commit()



# SQL TO CREATE FOREIGN KEY TBL NEWS DETAIL
# ALTER TABLE `tbl_news` ADD CONSTRAINT `relation_news` FOREIGN KEY (`id`) REFERENCES `tbl_news_detail`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT



