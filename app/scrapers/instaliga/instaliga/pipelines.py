# -*- coding: utf-8 -*-
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from scrapy.exporters import CsvItemExporter, JsonItemExporter
import json


class InstaligaPipeline(object):
    def process_item(self, item, spider):
        return item


class CSVPipeline(object):

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


class JSONPipeline(object):

    def __init__(self):
        self.filename = 'output.json'

    def open_spider(self, spider):
        self.json = open(self.filename, 'wb')
        self.exporter = JsonItemExporter(self.json)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.json.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class JsonItemExporter(JsonItemExporter):

    def __init__(self, **kwargs):
        self._configure(kwargs)
        self.file = open('output.json', 'w+b')
        self.encoder = json.JSONEncoder(**kwargs)
        self.first_item = True

    def start_exporting(self):
        self.file.write("[")

    def finish_exporting(self):
        self.file.write("]")

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(',\n')
        itemdict = dict(self._get_serialized_fields(item))
        self.file.write(self.encoder.encode(itemdict))
