import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        for h1_text in response.xpath('//h1/text()'):
            yield {'text': h1_text.extract()}