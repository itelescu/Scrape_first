from urllib.parse import urlencode
from os import strerror
import scrapy

'''Starting the spider will be done following next steps:
    1.Change directory where spider is located
    2.Access following command 'scrapy crawl autovit_scrap' '''

try:
    with open('parser_link.txt') as file:
        link = file.read()
except Exception as exep:
    print('Ocurred error: ', strerror(exep.errno))
        
# Number of pages you want to scrap
number_of_pages = 1


class AutovitSpider(scrapy.Spider):

    name = "autovit_scrape"
    allowed_domains = ['autovit.ro']

    custom_settings = {
        'FEEDS': {'file.jsonl': {'format': 'jsonlines', 'overwrite': True}}
    }

    def start_requests(self):
        global link
        yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        global link
        global number_of_pages

        # Select name, date of publication and link for each care on first page
        for item in response.css('.ooa-1mxnix4.e1b25f6f15'):
            yield {
                'name_auto': item.css('div.ooa-1mxnix4.e1b25f6f15>h2>a::text').get(),
                'publish_day': item.css('div.ooa-1mxnix4.e1b25f6f15>ul>li::text').get(),
                'link_auto': item.css('div.ooa-1mxnix4.e1b25f6f15>h2>a::attr(href)').get(),
                }

        for item in range(2, number_of_pages):
            next_page = f'{link}?page={item}'

            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

