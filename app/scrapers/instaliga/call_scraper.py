from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

os.chdir('./app/scrapers/instaliga')

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('user')
process.start()