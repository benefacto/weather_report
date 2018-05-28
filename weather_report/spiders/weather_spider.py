import pprint
from scrapy.spiders import Spider
from weather_report.items import Day

class Weather_Spider(Spider):
    name = "weather"
    allowed_domains = ["blackdogandmagpie.net"]
    start_urls = [
        "http://blackdogandmagpie.net/weather/today.htm",
        "http://blackdogandmagpie.net/weather/yesterday.htm"
    ]

    def parse(self, response):
        item = Day()
        item['name'] = 'today' if 'today' in response.url else 'yesterday'
        item['high_temp'] = self.extract('tr[2]/td[2]/text()', response.selector)
        item['low_temp'] = self.extract('tr[3]/td[2]/text()', response.selector)
        item['high_humidity'] = self.extract('tr[3]/td[2]/text()', response.selector)
        item['low_humidity'] = self.extract('tr[3]/td[2]/text()', response.selector)
        return item
        
    def extract(self, xpath, selector) :
        base_xpath = '//table/tbody/'
        degrees = u'\xa0'
        ustring = selector.xpath(base_xpath + xpath).extract_first(
                default='not-found').split(degrees)[0]
        return ustring
