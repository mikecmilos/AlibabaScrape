import wget
# image download
import os
import json
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=riot+gear&viewtype=&tab=")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)

items = driver.find_elements_by_css_selector(".J-offer-wrapper")

output = []

for i in items:
    try:
        product_name = i.find_element_by_css_selector("h4").text
    except:
        product_name = None
    try:
        price = i.find_element_by_css_selector(".list-no-v2-basicinfo__element").text
    except:
        price = None
    
    try:
        img_div = i.find_element_by_css_selector(".seb-img-switcher__imgs")
        img_url = img_div.get_attribute("data-image")
        img_url = "https:" + img_url
        img_url = img_url.replace("_300x300.jpg","")
        img_url = img_url.replace("_300x300.png","")
        destination = "images/" + img_url.split("/")[-1]
        if os.path.exists(destination) != True:              #If doesnt exist it will download
            wget.download(img_url, destination)
    except:
        img_url = None



    output_item = {
        'img':img_url,
        'price': price,
        'product_name': product_name
    }


    output.append(output_item)
    # print(price, product_name, img_url)


json.dump(output, open("product.json","w"), indent = 2)

driver.close()