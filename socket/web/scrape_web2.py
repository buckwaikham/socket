# scrape webpage
import scrapy
from scrapy.crawler import CrawlerRunner
# text cleaning
import re
# Reactor restart
from crochet import setup, wait_for
setup()

class QuotesToCsv(scrapy.Spider):
    """scrape first line of  quotes from `wikiquote` by 
    Maynard James Keenan and save to json file"""
    name = "MJKQuotesToCsv"
    start_urls = [
        'https://en.wikiquote.org/wiki/Maynard_James_Keenan',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            '__main__.ExtractFirstLine': 1
        },
        'FEEDS': {
            'quotes.csv': {
                'format': 'csv',
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        """parse data from urls"""
        for quote in response.css('div.mw-parser-output > ul > li'):
            yield {'quote': quote.extract()}


class ExtractFirstLine(object):
    def process_item(self, item, spider):
        """text processing"""
        lines = dict(item)["quote"].splitlines()
        first_line = self.__remove_html_tags__(lines[0])

        return {'quote': first_line}

    def __remove_html_tags__(self, text):
        """remove html tags from string"""
        html_tags = re.compile('<.*?>')
        return re.sub(html_tags, '', text)

@wait_for(10)
def run_spider():
    """run spider with MJKQuotesToCsv"""
    crawler = CrawlerRunner()
    d = crawler.crawl(QuotesToCsv)
    return d