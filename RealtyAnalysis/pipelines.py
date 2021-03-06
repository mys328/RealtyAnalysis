# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class RealtyanalysisPipeline(object):
    def process_item(self, item, spider):
        return item


class XiaozhuPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.test = self.client['realty']
        self.testData = self.test['xiaozhu']

    def process_item(self, item, spider):
        data = {
            'latlng': item['latlng'],
            'title': item['title'],
            'price': item['price'],
            'single': item['single'],
            'bed': item['bed'],
            'people': item['people'],
            'score': item['score'],
            'comment': item['comment']
        }
        self.testData.insert_one(data)
        return item

    def close_spider(self, spider):
        pass

class LianjiaPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['realty']
        self.data = self.db['lianjia']

    def process_item(self, item, spider):
        data = {
            'title_main': item['title_main'],
            'title_sub': item['title_sub'],
            'price_total': item['price_total'],
            'price_unit': item['price_unit'],
            'tips': item['tips'],
            'area': item['area'],
            'house_type': item['house_type'],
            'storey': item['storey'],
            'direction': item['direction'],
            'court': item['court'],
            'location': item['location'],
        }
        self.data.insert_one(data)
        return item

    def close_spider(self, spider):
        pass
