# -*- coding:utf-8 -*-
# -*- author:cyd -*-
from pdb import line_prefix
import re
import json
from datetime import datetime
from random import choice
from urllib.parse import urljoin
import time
from threading import Thread
##################################################################################################
import pandas as pd
import pymongo
from torch import div
import whois
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
##################################################################################################
from settings import WEB_HEADERS_POOL, PROXY, ENABLE_HEADLESS, ENABLE_LINUX
from settings import DB_IP_ADDRESS
from settings import get_chrome_option
from cyd_log import logger # logger.debug(f"")
##################################################################################################

driver = ''
myclient = ''
mycol = ''
count = 1


def open_browser():
    global driver
    # logger.debug(f"")
    
    # 打开浏览器
    chrome_options = get_chrome_option()
    if ENABLE_LINUX:
        driver = webdriver.Chrome(options=chrome_options)
    else:
        chrome_path = r"C:/Program Files/Google/Chrome/Application/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    # logger.debug('open driver ok')



def does_this_table_already_exist_in_the_database(start_url):
    global myclient
    # logger.debug(f"")

    mydb = myclient["woman_clothing"]
    collection_list = mydb.list_collection_names()
    # collection_name = re.sub('^.*/zgbs/(.*?)/(.*?)(/.*)?$', '\\1_\\2', start_url)
    collection_name = 'button_down_shirts'

    if collection_name in collection_list:
        logger.debug("collection_name in collection_list")
        myclient.close()
        return True
    else:
        return False


def wait_for_the_page_to_load():
    global driver
    # logger.debug(f"")

    driver_page_source = driver.page_source
    for i in range(3):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        

        time.sleep(2)
        if driver_page_source == driver.page_source:
            break
        else:
            driver_page_source = driver.page_source

# Step4
def main(start_url, topid):
    global driver, mycol
    # logger.debug(f"")

    item = {}
    open_browser()
    driver.get(start_url)
    wait_for_the_page_to_load()
    # image(img/src)
    elements = driver.find_elements_by_xpath('//*[@id="imgTagWrapperId"]')
    # elements = driver.find_elements_by_xpath('//*[@class="imgTagWrapper"]')
    
    item['topid'] = topid

    if elements:
        element = elements[0]
        element_img = element.find_element_by_xpath('./img')
        image_url = element_img.get_attribute('src')
        item['image'] = image_url
        # print("Image_url-------\n", item['image'])

    # feature(ul/li/span)
    li_features = []
    elements = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/ul')
    if elements:
        element = elements[0]
        element_li = element.find_elements_by_xpath('li')
        for i in range(len(element_li)):
           li_features.append(element_li[i].text) 
        # when have "show more"
        elements_more = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/div/div/ul')
        if elements_more:
            show_more = driver.find_element_by_xpath('//*[@id="feature-bullets"]/div/a')
            ActionChains(driver).move_to_element_with_offset(show_more, 5, 5).click().perform()
            elements_more = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/div/div/ul')
            element = elements_more[0]
            element_li = element.find_elements_by_xpath('li')
            for i in range(len(element_li)):
                li_features.append(element_li[i].text)
        item['features'] = li_features 
        # print("Features-------\n", item['features'])

    # review(div/div)
    div_reviews = []
    elements = driver.find_elements_by_xpath('//*[@id="cm-cr-dp-review-list"]')
    if elements:
        element = elements[0]
        element_div = element.find_elements_by_xpath('div')
        div_reviews = [[]for i in range(len(element_div))]
        print("Reviews-------\n")  
        for i in range(len(element_div)):
            div_reviews[i].append(element_div[i].text)
        item['reviews'] = div_reviews 
        # print(item['reviews'], '\n')
    # insert in sql
    mycol.insert_one(item)
        

# Step3
def save_mogoDB(start_url, topid, clotype):

    global driver, myclient, mycol
    # logger.debug(f"")

    # 连接数据库
    myclient = pymongo.MongoClient(f"mongodb://admin:123456@{DB_IP_ADDRESS}:27017")
    mydb = myclient["woman_top_clothings"]
    # collection_name = re.sub('^.*/zgbs/(.*?)/(.*?)(/.*)?$', '\\1_\\2', start_url)
    collection_name = clotype
    mycol = mydb[collection_name]

    # # 判断商品是否已存在
    # if does_this_table_already_exist_in_the_database(start_url):
    #     return

    main(start_url, topid)

def get_amazon_best_sellers(start_url, clotype):
    global driver
    logger.debug(f"")

    # 访问首页
    driver.get(start_url)
    wait_for_the_page_to_load()
    elements = driver.find_elements_by_xpath('//*[@id="gridItemRoot"]')
    if len(elements) != 0:
        main_get_product_info1(start_url, clotype)   # gridItemRoot
    else:
        main_get_product_info2(start_url, clotype)   # zg-ordered-list


# Step2
def main_get_product_info1(start_url, clotype):
    global driver, count

    open_browser()
    driver.get(start_url)
    wait_for_the_page_to_load()
    # get clothing url
    while count!=101:
        elements = driver.find_elements_by_xpath('//*[@id="gridItemRoot"]/div')
        next_page = driver.find_elements_by_xpath('//*[@class="a-last"]/a')
        if elements:
            for i in range(len(elements)):
                if elements[i]:
                    href = elements[i].find_element_by_xpath('./div[2]/div/a[1]').get_attribute('href')
                    topid = elements[i].find_element_by_xpath('./div[1]/div[1]/span').text
                    # print(i, ":", href, "\n")
                    logger.debug('sellers ' + str(i) + ":" + str(href))
                    save_mogoDB(href, topid, clotype)
                    count += 1
                    # print(count, '\n')
                    logger.debug('count = ' + str(count))
        # next page——>        
        if next_page:
            print("next page\n")
            get_amazon_best_sellers(next_page[0].get_attribute('href'), clotype)
        else:
            break
    # driver.quit()

def main_get_product_info2(start_url, clotype):
    global driver, count

    open_browser()
    driver.get(start_url)
    wait_for_the_page_to_load()
    # get clothing url
    while True:
        # 两种情况：***********
        elements = driver.find_elements_by_xpath('//*[@id="gridItemRoot"]/div/div[2]/div/a[1]')
        next_page = driver.find_elements_by_xpath('//*[@class="a-last"]/a')
        if elements:
            for i in range(len(elements)):
                if elements[i]:
                    href = elements[i].get_attribute('href')
                    # print(i, ":", href, "\n")
                    logger.debug('sellers ' + str(i) + ":" + str(href))
                    save_mogoDB(href, clotype)
                    count += 1
                    # print(count, '\n')
                    logger.debug('count = ' + str(count))
        # next page——>
        if next_page:
            print("next page\n")
            get_amazon_best_sellers(next_page[0].get_attribute('href'), clotype)
        else:
            break
    # driver.quit()



# Step1            
def get_amazon_best_sellers_categories(start_url):
    global driver
    global categories
    # logger.debug(f"")

    open_browser()
    driver.get(start_url)
    wait_for_the_page_to_load()
    categories = driver.find_elements_by_xpath('//*[@role="group"]/div')
    clotype = ['blouses', 'polos', 't_shirts', 'tanks', 'tunics', 'vests']
    threads = []
    if categories:
        for i in range(3, len(categories)):
            href = categories[i].find_element_by_xpath('./a').get_attribute('href')
            # print("categorie ", i, ":", href, "\n")
            logger.debug("categorie " + str(i) + " " + str(href))
            get_amazon_best_sellers(href, clotype[i])
            
    # if elements:
    #     i = 4
    #     href = elements[i].find_element_by_xpath('./a').get_attribute('href')
    #     # print("categorie ", i, ":", href, "\n")
    #     logger.debug("categorie " + str(i) + " " + str(href))
    #     get_amazon_best_sellers(href)
    # driver.quit()



if __name__ == '__main__':
    logger.debug(f"the very beginning")

    start_url = 'https://www.amazon.com/Best-Sellers-Clothing-Shoes-Jewelry-Womens-Tops-Tees-Blouses/zgbs/fashion/2368343011'
    
    for num in range(3):
        get_amazon_best_sellers_categories(start_url)
        count = 1
        time.sleep(1200)

    logger.debug(f"the very end")

    time.sleep(100000)
    driver.quit()
