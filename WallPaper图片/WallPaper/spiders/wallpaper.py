# -*- coding: utf-8 -*-
import scrapy
from WallPaper.items import WallpaperItem
import json


# http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000003/vertical?limit=30&skip=30&adult=false&first=0&order=new
# http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000003/vertical?limit=30&skip=30&adult=false&first=0&order=hot

class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper'
    allowed_domains = ['service.picasso.adesk.com']

    front_url = 'http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000003/vertical?limit=30&skip='
    page = 0
    after_url = '&adult=false&first=0&order=hot'
    start_urls = [front_url + str(page) + after_url]

    def parse(self, response):
        data = json.loads(response.text)['res']['vertical']
        for each in data:
            item = WallpaperItem()
            item['imgcode'] = each['ncos']
            item['imglink'] = each['wp']
            yield item

        self.page += 30
        yield scrapy.Request(self.front_url + str(self.page) + self.after_url,callback=self.parse)























