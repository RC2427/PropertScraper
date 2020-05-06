# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import types


class ScrapePipeline(object):

    def process_item(self, item, spider):
        field_list = ['prop_title', 'prop_id', 'prop_price', 'prop_desc', 'prop_sqFeet', 'prop_bhk', 'prop_img']
        print('==============Pipeline===================')
        for x in range(0, 7):
            item[field_list[x]] = [it.replace('\r', '') for it in item[field_list[x]]]
            item[field_list[x]] = [it.replace('\n', '') for it in item[field_list[x]]]
            item[field_list[x]] = [it.replace('\t', '') for it in item[field_list[x]]]
            item[field_list[x]] = [it.replace('  ', '') for it in item[field_list[x]]]
            item[field_list[x]] = [it.replace('₹', '') for it in item[field_list[x]]]

            while '' in item[field_list[x]]:
                item[field_list[x]] = list(filter(None, item[field_list[x]]))

            while '' in item[field_list[x]]:
                item[field_list[x]] = list(filter(None, item[field_list[x]]))

            while '\n' in item[field_list[x]]:
                item[field_list[x]] = list(filter(None, item[field_list[x]]))

            if field_list[x] == 'prop_sqFeet':
                flag = 0
                if 'SqMeters' in item[field_list[x]][0]:
                    flag = 1
                print(item[field_list[x]][0])
                trim = re.compile(r'[^\d.]+')
                item[field_list[x]] = float(trim.sub('', item[field_list[x]][0]))

                if flag == 1:
                    print("sq_feet conversion")
                    item[field_list[x]] = float("{:.2f}".format(item[field_list[x]] * 10.73))
                    flag = 0

            if field_list[x] == 'prop_price':
                trim = re.compile(r'[^\d.]+')
                item[field_list[x]] = int(trim.sub('', item[field_list[x]][0]))

            if field_list[x] == 'prop_bhk':
                trim = re.compile(r'[^\d.]+')
                item[field_list[x]] = int(trim.sub('', item[field_list[x]][0])[0])

            if type(item[field_list[x]]) is list:
                item[field_list[x]] = str(item[field_list[x]])
                item[field_list[x]] = item[field_list[x]].replace('[', '')
                item[field_list[x]] = item[field_list[x]].replace(']', '')
                item[field_list[x]] = item[field_list[x]].replace("'", '')

        if item['prop_img'] is list:
            print("img link process")
            item['prop_img'] = str(item['prop_img'])
            item['prop_img'] = item['prop_img'].replace('[', '')
            item['prop_img'] = item['prop_img'].replace(']', '')
            item['prop_img'] = item['prop_img'].replace("'", '')

        return item
