**Minggu ke-4**

1. query insert by item #self.curr.execute("""INSERT into tbl_news(title, url, tanggal) VALUES(%s, %s, %s)""")
2. set primary key and make auto increment ALTER TABLE `#` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`);
3. set FK in table detail