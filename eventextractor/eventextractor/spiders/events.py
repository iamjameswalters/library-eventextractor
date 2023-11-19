import scrapy


class EventsSpider(scrapy.Spider):
    name = "events"
    allowed_domains = ["nypl.org"]
    start_urls = ["https://www.nypl.org/events/calendar?keyword=&target%5B%5D=ad&city%5B%5D=man&date_op=GREATER_EQUAL&date1=11%2F18%2F2023&location=&type=4320&topic=&audience=&series="]

    def parse(self, response):
        table = response.css('table.views-table')
        events = table.css('tbody').css('tr')
        for event in events:
            yield {
                "name": event.css('.event-name > a::text').get(),
                "datetime": "".join(event.css('.event-time::text').getall()),
                "location": event.css('.event-location::text').get(),
                "description": event.css('.description::text').get(),
            }
        next_link = response.css('.pager').xpath('.//a[text()="Next"]/@href').get()
        if next_link is not None:
            next_page = response.urljoin(next_link)
            yield scrapy.Request(next_page, callback=self.parse)
