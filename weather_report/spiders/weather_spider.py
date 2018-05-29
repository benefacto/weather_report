from scrapy.spiders import Spider
from scrapy.selector import Selector
from weather_report.items import Weather

class Weather_Spider(Spider):
    name = "weather_spider"
    allowed_domains = ["blackdogandmagpie.net"]
    start_urls = [
        "http://blackdogandmagpie.net/weather/today.htm",
        "http://blackdogandmagpie.net/weather/yesterday.htm"
    ]

    def parse(self, response):
        item = Weather()
        item['day'] = 'today' if 'today' in response.url else 'yesterday'
        item['high_temp'] = self.extract(response, 'tr[2]/td[2]/text()', u'\xa0')
        item['low_temp'] = self.extract(response, 'tr[3]/td[2]/text()', u'\xa0')
        item['high_humidity'] = self.extract(response, 'tr[9]/td[2]/text()', u'\xa0%')
        item['low_humidity'] = self.extract(response, 'tr[10]/td[2]/text()', u'\xa0%')
        return item
        
    def extract(self, response, xpath, trail) :
        base_xpath = '//table/tbody/'
        ustring = response.selector.xpath(base_xpath + xpath).extract_first(
                default='not-found').split(trail)[0]
        return ustring
