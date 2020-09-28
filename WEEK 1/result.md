
**Hari 1 - 5 Belajar Scrapy ( 21 Sept - 25 Sept 2020 )**

## SYNTAX SCRAPY
    scrapy shell 'http://quotes.toscrape.com/page/1/' 

> untuk membuka scrapy shell dengan url quotes.toscrape.com/page/1

**using css**
`response.css('title::text').getall()` 

> mengambill title dengan hanya text nya saja bisa juga dengan `response.css('title::text')[0].get() / response.css('title::text').get() or jika ingin menggunakan regex bisa juga pakai `response.css('title::text').re(r'Q\w+')` / `response.css('title::text').re(r'(\w+) to (\w+)')

***using xpath***
`response.xpath('//title/text()').get()`

> mengambil title dengan hanya textnya saja
> 

**Storing the scraped data**

    scrapy crawl quotes -o quotes.json ==> output json

**Following links ( get data next page )**
contoh tag untuk tombol next page / halaman

    <ul class="pager">
        <li class="next">
            <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
        </li>
    </ul>

menggunakan shell untuk mendapatkan value dari a href yg mana digunakan untuk next halaman => `response.css('li.next a').get() / response.css('li.next a::attr(href)').get()` == ambil attribut hrefnya saja yaitu /page/2

**Scraping a web page**
berhasil mengscraping beberapa konten blog di website https://mazipan.space dan http://quotes.toscrape.com/

**Belajar OOP Python**


