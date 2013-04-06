from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from metacritic.items import MetacriticItem

class DmozSpider(BaseSpider):
    name = "mc"
    allowed_domains = ["metacritic.com"]
    start_urls = [
                 "http://www.metacritic.com/game/xbox-360/bioshock-infinite"
                 ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//span[@class='score_value']")

        items = []

        for site in sites:
            item = MetacriticItem()
            item['Score'] = site.select('text()').extract()
            items.append(item)
        return items
