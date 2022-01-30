# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
import csv
import time
import re
import pandas as pd
#
browser = webdriver.Chrome()
browser.implicitly_wait(10)
#

本社所在地　本部所在地（＆本社所在地）　本社
大阪本社所在地（＆東京本社所在地）
本社　所在地


代表者
設立
資本金
従業員
売上高



df = pd.read_csv('mynavi_sample.csv')
for num in range(len(df)):
    url = df.iloc[num,1]
    browser.get(url)
    table_elem =browser.find_element_by_class_name("ts-p-mod-dataTable02")
    trs = table_elem.find_elements_by_tag_name("tr")
    for i in range(len(trs)):
        th = trs[i].find_element_by_tag_name("th")
        if th.text == "代表者":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,2] = td.text
        elif th.text == "事業所" or th.text == "本社所在地":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,3]= td.text
        elif th.text == "資本金":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,4] = td.text
        elif th.text == "従業員数":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,5] = td.text
        elif th.text == "売上高":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,6] = td.text
        elif th.text == "設立":
            td = trs[i].find_element_by_tag_name("td")
            df.iloc[num,7] = td.text
        else:
            pass
    time.sleep(1)

df.to_csv('recnavi_ext.csv')

browser.close()
