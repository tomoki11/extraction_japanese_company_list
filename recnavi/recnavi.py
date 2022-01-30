# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
import csv
import time
#
browser = webdriver.Chrome()
browser.implicitly_wait(10)
#
browser.get("https://job.rikunabi.com/2022/search/pre/company/result/?fw=&isc=r21rcna00257&toplink=search")
pages_remaining = True
#
while pages_remaining:
    try:
        company_elem = browser.find_elements_by_class_name("js-p-clickableCassetteList-item-link")
        list = [x.text.encode('utf-8')+','+x.get_attribute("href").encode('utf-8')+'\n' for x in company_elem]
        with open('recnavi.csv', 'a') as l:
            l.writelines(list)
        next_link = browser.find_element_by_partial_link_text("次の100社")
        next_link.click()
        time.sleep(1)
    except:
        browser.close()
