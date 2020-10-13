import scrapy

class MazipanSpider(scrapy.Spider):
    name = "mazipanblog"
    domain = "https://mazipan.space"

    def start_requests(self):
        urls = [
            'https://mazipan.space',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        for post in response.css('article.post-card'):
            yield {
                'title'         : post.css("header.post-card-header h2::text").extract_first(),
                'detail_post'   : self.domain + post.css("a::attr(href)").extract_first(),
                'img'           : self.domain + post.css("a div.post-card-image picture img::attr(src)").extract_first(),
            }

        next_page = self.domain + response.css("nav.css-1y9ytta div a::attr(href)")[-1].extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    #next url response.css("nav.css-1y9ytta div a::attr(href)")[-1].extract()


# posts = response.css("div.css-10xnjik") 

#get detailpost
# post = posts.css("article.post-card a::attr(href)").extract_first()

#get img
#posts.css("article.post-card a div.post-card-image picture source::attr(srcset)").extract_first() 

#get title
# posts.css("header.post-card-header h2::text").extract_first()  