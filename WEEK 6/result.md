**Minggu ke-6**

1. query insert by item #self.curr.execute("""INSERT into tbl_news(title, url, tanggal) VALUES(%s, %s, %s)""")
2. set primary key and make auto increment ALTER TABLE `#` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`);
3. set FK in tbl_news at id_news_detail
4. with beautifulsoup4 success get RSS Feed https://www.harianjogja.com/rss export to csv with pandas
5. try to use feedparser to get content rss

// UPDATE `tbl_news_detail` SET `id_detail_news`= id WHERE 1