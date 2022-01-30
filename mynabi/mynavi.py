# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
import csv
import time
#
browser = webdriver.Chrome()
browser.implicitly_wait(10)
#
browser.get("https://job.mynavi.jp/22/pc/search/query.html?HR:1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,99")
pages_remaining = True
#

list = []
while pages_remaining:
    try:
        for id in range(100):
            id_name = 'corpNameLink[' + str(id) + ']'
            company_elem = browser.find_element_by_id(id_name)
            company_name = company_elem.text.encode('utf-8')
            url = company_elem.get_attribute("href").encode('utf-8')
            list.append(company_name)
            list.append(',')
            list.append(url)
            list.append('\n')

        next_link = browser.find_element_by_partial_link_text("次の100社")
        next_link.click()
        time.sleep(1)

    except:
        with open('mynavi.csv', 'w') as l:
            l.writelines(list)

        browser.close()
