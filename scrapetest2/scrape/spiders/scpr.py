import cmd
import scrapy
import sys

sys.path.append("/home/rc/Documents/scrapetest2")

from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrape import items
from scrape import FileRead
from scrape import settings


class scprSpider(scrapy.Spider):
    name = 'scpr'
    allowed_domains = ['propertywala.com']
    returl = FileRead.get_url()
    start_urls = {returl}
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['prop_title', 'prop_id', 'prop_price', 'prop_desc', 'prop_sqFeet', 'prop_bhk','prop_link', 'prop_img'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'feed-test.json'
    }

    def parse(self, response):
        print('parsing Started =======================-------------------------------=======================')
        print(response.request.url)
        item = items.ScrapeItem()
        Xpath_list = FileRead.Read_File()

        title_path, id_path, price_path, desc_price, area_path,img_path, ref_path = [Xpath_list[i] for i in range(0, len(Xpath_list))]

        title_main = response.xpath(title_path)
        propid = response.xpath(id_path)
        property_price = response.xpath(price_path)
        prop_desc = response.xpath(desc_price)
        prop_feat = response.xpath(area_path)
        prop_img = response.xpath(img_path)
        ref_link = ref_path

        for crawl, crawl1, crawl2, crawl3, crawl4, crawl5 in zip(title_main, property_price, propid, prop_desc, prop_feat, prop_img):
            title = crawl.xpath('text()').extract()
            prop_id = crawl2.xpath('@href').extract()
            prop_price = crawl1.xpath('text()').extract()
            link = ref_link + prop_id[0]
            propdesc = crawl3.xpath('text()').extract()
            propfeat = crawl4.xpath('text()').extract()
            bhk = crawl.xpath('text()').extract()
            propimg = crawl5.xpath('@src').extract()
            item['prop_title'] = title
            item['prop_id'] = prop_id
            item['prop_price'] = prop_price
            item['prop_desc'] = propdesc
            item['prop_sqFeet'] = propfeat
            item['prop_bhk'] = bhk
            item['prop_img'] = propimg
            item['prop_link'] = link
            print("yielding items")
            yield item
        print('parsing ended =======================-------------------------------=======================')


class scprSpider1(scrapy.Spider):
    name = 'scpr1'
    allowed_domains = ['magicbricks.com']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['prop_title', 'prop_id', 'prop_price', 'prop_desc', 'prop_sqFeet', 'prop_bhk', 'prop_link', 'prop_img'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'feed-test.json'
    }
    returl = FileRead.get_url1()
    start_urls = {returl}

    def parse(self, response):
        print('parsing Started =======================-------------------------------=======================')
        print(response.request.url)
        item = items.ScrapeItem()
        title_main = response.xpath("//meta[@itemprop = 'name']")
        Bhk_main = response.xpath("//div[@class = 'flex relative clearfix m-srp-card__container']//span[@class = "
                                  "'m-srp-card__title__bhk']")
        propid = response.xpath("//meta[@itemprop = 'url']")
        property_price = response.xpath("//div[@class = 'flex relative clearfix m-srp-card__container']//div[@class = "
                                        "'m-srp-card__price'] ")
        prop_desc = response.xpath("//meta[@itemprop = 'description']")
        prop_feat = response.xpath("//div[@class = 'flex relative clearfix m-srp-card__container']//span[@class = "
                                   "'font-type-3']")
        prop_img = response.xpath("//div[@class = 'm-photo']//img[@class = 'm-photo__img lazy']")
        ref_link = "https://www.magicbricks.com"
        # print(title_main)

        for crawl, crawl2, crawl3, crawl4, crawl5, crawl6, crawl7 in zip(title_main, Bhk_main, prop_feat, property_price, prop_desc, propid, prop_img):
            title = crawl.xpath('@content').extract()
            bhk = crawl2.xpath('text()').extract()
            propfeat = crawl3.xpath('text()').extract()
            prop_price = crawl4.xpath('text()').extract()
            propdesc = crawl5.xpath('@content').extract()
            prop_id = crawl6.xpath('@content').extract()
            link = ref_link + prop_id[0]
            propimg = crawl7.xpath('@data-src').extract()
            item['prop_title'] = title
            item['prop_id'] = prop_id
            item['prop_price'] = prop_price
            item['prop_desc'] = propdesc
            item['prop_sqFeet'] = propfeat
            item['prop_bhk'] = bhk
            item['prop_img'] = propimg
            item['prop_link'] = link
            print("yielding items")
            yield item
        print('parsing ended =======================-------------------------------=======================')
