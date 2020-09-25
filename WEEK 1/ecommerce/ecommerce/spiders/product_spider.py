import scrapy

class ProductSpider(scrapy.Spider):
    name = "product"

    def start_requests(self):
        urls = [
            'https://mazipan.space',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        for post in response.css('article.post-card'):
            yield {
                'title' : post.css("header.post-card-header h2::text").extract_first(),
                'img'   : 'https://mazipan.space' + post.css("a div.post-card-image picture img::attr(src)").extract_first(),
            }


