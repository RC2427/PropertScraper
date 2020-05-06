import csv
import fileinput
import re
import sys
import os
import json
import operator
from operator import attrgetter
import pandas as pd
import numpy as nupy
import pprint

def Read_File():
    Xpath_File = open('/home/rc/Documents/scrapetest2/scrape/xpath.txt', 'r+')
    criteria_list = Xpath_File.readlines()[2:]
    criteria_list = [x.strip('\n') for x in criteria_list]
    criteria_list = [x.strip('"\"') for x in criteria_list]
    return criteria_list


def form_reader():
    form_data = open('/home/rc/Documents/scrapetest2/scrape/formdata.txt', 'r+')
    input_list = form_data.readlines()
    input_list = [x.strip('\n') for x in input_list]
    input_list = [x.strip('"\"') for x in input_list]
    return input_list


def find_city(key):
    reader = csv.DictReader(open('/home/rc/Documents/scrapetest2/scrape/items.csv'))

    for row in reader:
        if row['prop_key'] == key:
            return row['prop_value']


def find_price(key):
    trim = re.compile(r'[^\d.]+')
    key = int(trim.sub('', key))

    reader = csv.DictReader(open('/home/rc/Documents/scrapetest2/scrape/price.csv'))

    for row in reader:
        print(key, row['prop_key'])
        if key <= int(row['prop_key']):
            print(row['prop_value'])
            return row['prop_value']


def get_url():
    reader = open('/home/rc/Documents/scrapetest2/scrape/url.txt', 'r+')
    url = reader.readline()
    return url


def ref_json():
    for line in fileinput.FileInput("/home/rc/Documents/scrapetest2/scrape/feed-test.json", inplace=True):
        print(line.replace("][", ""))

    reader = open("feed-test.json", "r")
    lines = reader.readlines()
    reader.close()
    lines = filter(lambda x: not x.isspace(), lines)
    reader = open("/home/rc/Documents/scrapetest2/scrape/feed-test.json", "w")
    reader.write("".join(lines))
    reader.close()


def sort_json():
    json_dict = {}
    with open("/home/rc/Documents/scrapetest2/scrape/feed-test.json", "r+") as file:
        json_dict = json.load(file)
    dataframe = pd.DataFrame(json_dict)

    dataframe = dataframe.sort_values(by=['prop_price', 'prop_sqFeet'])
    dataframe.to_json('items.json', indent=4)


sort_json()