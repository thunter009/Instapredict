from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import sys

os.chdir('./app/scrapers/instaliga')
settings = get_project_settings()
# settings.set('ITEM_PIPELINES', 'instaliga.pipelines.BeerPipeline', priority=1)
process = CrawlerProcess(settings)
process.crawl('user', user=sys.argv[1])
process.start()
