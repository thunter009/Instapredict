# -*- coding: utf-8 -*-
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from scrapy.exporters import CsvItemExporter


class InstaligaPipeline(object):
    def process_item(self, item, spider):
        return item


class BeerPipeline(object):

        def __init__(self):
            self.filename = 'output.csv'

        def open_spider(self, spider):
            self.csvfile = open(self.filename, 'wb')
            self.exporter = CsvItemExporter(self.csvfile)
            self.exporter.start_exporting()

        def close_spider(self, spider):
            self.exporter.finish_exporting()
            self.csvfile.close()

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item
