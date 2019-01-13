import time
from selenium import webdriver

import requests
from bs4 import BeautifulSoup

# driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

#launch url
#url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
url = "https://www.gv.com.sg/#/"
#tab-content
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

#python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
#python_button.click() #click fhsu link

findAllList = driver.find_elements_by_class_name('tab-content')
#print findAllList.count()
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 0 #counter
# for link in soup_level1.find_all('div'):
#     print 'asd'
    
driver.quit()