**Minggu ke-3**

 
. Scraping https://indeks.kompas.com/ dengan mengambil jumlah berita per hari / dengan detail berita setiap page 
. store data berita ke database
  
todo : 

 - nambahain id unique per object sebelum insert ke database
 - mengganti tanggal supaya dinamis dgn datetime 
 - formating output di ke database

note :
 - karena memakai pipeline datanya blm bagus, jadi ada alternatif untuk output ke csv setelah di convert ke sql (https://www.convertcsv.com/csv-to-sql.htm)
 - untuk membuat 2 tabel berbeda yg nantinya akan output csv diperlukan juga 2 spider (kemungkinan soalnya blm dicoba)
 - https://stackabuse.com/converting-strings-to-datetime-in-python/
 - https://www.tutorialspoint.com/scrapy/scrapy_item_pipeline.htm
 - https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t [url scrapy tutorial]
