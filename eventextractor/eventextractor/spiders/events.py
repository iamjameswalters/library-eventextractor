import scrapy


class EventsSpider(scrapy.Spider):
    name = "events"
    allowed_domains = ["nypl.org"]
    # The backslashes "\" in the URL escape the line breaks that have been
    # added to comply with PEP 8.
    # https://peps.python.org/pep-0008/#maximum-line-length
    start_urls = [
        "https://www.nypl.org/events/calendar?keyword=\
        &target%5B%5D=ad&city%5B%5D=man&date_op=GREATER_EQUAL\
        &date1=11%2F18%2F2023&location=&type=4320&topic=&audience=\
        &series="
    ]

    def parse(self, response):
        table = response.css("table.views-table")  # use a css selector
        events = table.css("tbody").css("tr")  # these can be chained
        # For every row in our table, make a dict containing our event data
        for event in events:
            yield {
                "name": event.css(".event-name > a::text").get(),
                "datetime": "".join(event.css(".event-time::text").getall()),
                "location": "".join(event.css(".event-location::text").getall()),
                "description": event.css(".description::text").get(),
            }
        # Find the "next page" link. If there is one, follow it and scrape
        # that page. In this case, we need an xpath and not just a CSS
        # selector.
        next_link = response.css(".pager").xpath('.//a[text()="Next"]/@href').get()
        if next_link is not None:
            next_page = response.urljoin(next_link)
            yield scrapy.Request(next_page, callback=self.parse)
