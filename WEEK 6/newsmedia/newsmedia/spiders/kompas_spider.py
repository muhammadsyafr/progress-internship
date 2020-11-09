import scrapy
from ..items import PostList
from datetime import date

class KompasSpider(scrapy.Spider):
    name = "kompas"
    time = ''
    categories = ''
    link_url = ''

    def start_requests(self):
        today = date.today()
        todayNews = today.strftime("%Y-%m-%d")    
        urls = [
            'https://indeks.kompas.com/?site=all&date='+ todayNews,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        for post in response.css('div.article__list'):

            title       = post.css("div.article__list__title a::text").extract_first()
            link_url    = post.css("div.article__list__title a::attr(href)").extract_first()
            time        = post.css("div.article__list__info div.article__date::text").extract_first()
            categories  = post.css("div.article__list__info div.article__subtitle::text").extract()

            # postList['title'] = title
            # postList['link_url'] = link_url
            # postList['time'] = time
            # postList['categories'] = categories

            self.time = time
            self.categories = "".join(categories)
            self.link_url = link_url

            yield scrapy.Request(url=link_url+'?page=all#page2', callback=self.parse_detail)

        next_page = response.css("div.paging__item a.paging__link--next::attr(href)")[-1].extract()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
            #with items
             postList = PostList()
             postList['title']      = response.css("h1.read__title::text").extract()
             postList['time']       = self.time
             postList['categories'] = self.categories
             postList['link_url']   = self.link_url
             postList['content']    = "".join(response.css("div.read__content p::text").extract())
             postList['tags']       = ", ".join(response.css('.tag__article__wrap li a::text').extract())
             postList['img']        = ",".join(response.css("div.js-read-article .photo img::attr(src)").extract())

             yield postList

            #with object
            # yield {
            #     'title'         : response.css("h1.read__title::text").extract(),
            #     'link_url'      : self.link_url,
            #     'time'          : self.time,
            #     'categories'    : self.categories,
            #     'content'       : response.css("div.read__content p::text").extract(),
            # }

