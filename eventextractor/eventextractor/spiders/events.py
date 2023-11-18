import scrapy


class EventsSpider(scrapy.Spider):
    name = "events"
    allowed_domains = ["nypl.org"]
    start_urls = ["https://nypl.org"]

    def parse(self, response):
        pass
