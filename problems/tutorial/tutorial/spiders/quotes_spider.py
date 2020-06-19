import scrapy

class QuotessSpider(scrapy.Spider):    
    name = 'quotes'
    start_urls = ['https://en.wikipedia.org/wiki/Letter_frequency',
    ]
    custom_settings = {
        'COOKIES_ENABLED': False
    }

    def parse(self, response):
        d = dict()
        for agent in response.css('tr')[1:27]:
            d[agent.css('td b::text').get()] = float((agent.css('td::text').getall()[0])[:-3])

        return d
