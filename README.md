# library-eventextractor

A web scraper for New York Public Library's event calendar. This is the demo code for my PyOhio 2023 talk: [Web Scraping Crash Course! With Python and Scrapy](https://www.pyohio.org/2023/talks/web-scraping-crash-course-with-python-and-scrapy/).

APIs are a great way to consume publicly accessible data. But what do you do when there's no API? Enter web scraping: a way you can harvest data out of the same HTML documents you look at in your web browser.

This project demonstrates:

- How to scaffold out a [Scrapy](https://scrapy.org/) project
- How to isolate elements in a page to extract data from them
- How to follow next page links in paginated results
- How to modify `settings.py` to alter your scraper's behavior


