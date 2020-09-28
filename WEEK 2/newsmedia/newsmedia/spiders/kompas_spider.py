import scrapy
from ..items import PostList
from datetime import date

class KompasSpider(scrapy.Spider):
    name = "kompas"
    # today = date.today()
    # todayNews = today.strftime("%Y/%m/%d")    
    # print('HARI INIIIIIIIIIIIIIIIIIIIIIIII '+todayNews)
    time = ''
    categories = ''

    def start_requests(self):
        urls = [
            'https://indeks.kompas.com/?site=all&date=2020-09-28',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):

        for post in response.css('div.article__list'):

            title       = post.css("div.article__list__title a::text").extract_first()
            link_url    = post.css("div.article__list__title a::attr(href)").extract_first()
            time        = post.css("div.article__list__info div.article__date::text").extract_first()
            categories  = post.css("div.article__list__info div.article__subtitle::text").extract_first()

            # postList['title'] = title
            # postList['link_url'] = link_url
            # postList['time'] = time
            # postList['categories'] = categories

            self.time = time
            self.categories = categories

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
             postList['content']    = response.css("div.read__content p::text").extract()

             yield postList

            #with object
            # yield {
            #     'title'         : response.css("h1.read__title::text").extract(),
            #     'time'          : self.time,
            #     'categories'    : self.categories,
            #     'content'       : response.css("div.read__content p::text").extract(),
            # }

# SELECTOR   

#title
# response.css("div.article__list div a::text").extract_first()

#link_url
#response.css("div.article__list div a::attr(href)").extract_first()

# time
# response.css("div.article__list div.article__list__info div.article__date::text").extract()    

#categories
# response.css("div.article__list div.article__list__info div.article__subtitle::text").extract_first()

#nextbutton if available
# response.css("div.paging__item a.paging__link--next::attr(href)").get()
