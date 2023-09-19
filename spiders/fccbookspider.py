import scrapy


class FccbookspiderSpider(scrapy.Spider):
    name = "fccbookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
