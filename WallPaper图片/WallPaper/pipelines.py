# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

class WallpaperPipeline(ImagesPipeline):
    #获取settings里的变量
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imglink'])

    def item_completed(self, results, item, info):
        print results
        image_path = [x['path'] for ok,x in results if ok]
        os.rename(self.IMAGES_STORE + image_path[0],
                  self.IMAGES_STORE + 'full/' +str(item['imgcode']) + '.jpg')
        # item['imgpath'] = self.IMAGES_STORE + item['imgcode']
# [1,{path:,url:,}]
        return item













































