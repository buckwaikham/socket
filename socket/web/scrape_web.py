# scrape webpage
import scrapy
from scrapy.crawler import CrawlerProcess
# text cleaning
import re

class QuotesToCsv(scrapy.Spider):
    """scrape first line of  quotes from `wikiquote` by 
    Maynard James Keenan and save to json file"""
    #name = "MJKQuotesToCsv"
    name = "AEQuotesToCsv"
    start_urls = [
        #'https://en.wikiquote.org/wiki/Maynard_James_Keenan',
        'https://en.wikiquote.org/wiki/Albert_Einstein',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            '__main__.ExtractFirstLine': 1
        },
        'FEEDS': {
            'AEquotes.csv': {
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

