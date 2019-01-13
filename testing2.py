from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#launch url
url = "https://www.gv.com.sg/#/"

# create a new Firefox session
driver = webdriver.Chrome()

# driver.implicitly_wait(2)

driver.get(url)
driver.execute_script("""
(function(XHR) {
  "use strict";
  console.log("asdasda");
  var element = document.createElement('div');
  element.id = "interceptedResponse";
  element.appendChild(document.createTextNode(""));
  document.body.appendChild(element);

  var open = XHR.prototype.open;
  var send = XHR.prototype.send;

  XHR.prototype.open = function(method, url, async, user, pass) {
    this._url = url; // want to track the url requested
    console.log(url);
    open.call(this, method, url, async, user, pass);
    
  };

  XHR.prototype.send = function(data) {
    var self = this;
    var oldOnReadyStateChange;
    var url = this._url;
    console.log(url);
    function onReadyStateChange() {
      if(self.status === 200 && self.readyState == 4 /* complete */) {
        document.getElementById("interceptedResponse").innerHTML +=
          '{"data":' + self.responseText + '}*****';
      }
      if(oldOnReadyStateChange) {
        oldOnReadyStateChange();
      }
    }

    if(this.addEventListener) {
      this.addEventListener("readystatechange", onReadyStateChange,
        false);
    } else {
      oldOnReadyStateChange = this.onreadystatechange;
      this.onreadystatechange = onReadyStateChange;
    }
    send.call(this, data);
  }
})(XMLHttpRequest);
""")
wait = WebDriverWait(driver, 3)


#After opening the url above, Selenium clicks the specific agency link
# python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
# python_button.click() #click fhsu link

#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
#print(soup_level1.prettify())
datalist = [] #empty list
x = 0 #counter
asd = soup_level1.find_all("div",{"class":"tab-content"})
# for link in soup_level1.find_all("div",{"id":"movieTabs"}):
#     #print(link)

#works do not delete
# link = driver.find_element_by_link_text('Advance Sales')
# link.click()


#secondOption = driver.find_element_by_xpath("//div[@id='movieTabs']/div[@class='muti-tabs container-fluid']/div[@class='tab-content']/div[@class='tab-pane ng-scope active']/div[2]/div[@class='thumbnail']/div[@class='poster']/a")
# works
# for x in range(2,6):
#     search = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']/div[@class='tab-pane ng-scope active']/div["+str(x)+"]/div[@class='thumbnail']/div[@class='poster']/a")))
#     #secondOption = driver.find_element_by_xpath("//div[@class='tab-content']/div[@class='tab-pane ng-scope active']/div["+str(x)+"]/div[@class='thumbnail']/div[@class='poster']/a")
#     #secondOption.click()
#     search.click()
#     driver.execute_script("window.history.go(-1)")
#     print("enter")



# #Beautiful Soup finds all Job Title links on the agency page and the loop begins
# for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
#     #Selenium visits each Job Title page
#     python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
#     python_button.click() #click link
    
#     #Selenium hands of the source of the specific job page to Beautiful Soup
#     soup_level2=BeautifulSoup(driver.page_source, 'lxml')

#     #Beautiful Soup grabs the HTML table on the page
#     table = soup_level2.find_all('table')[0]
    
#     #Giving the HTML table to pandas to put in a dataframe object
#     df = pd.read_html(str(table),header=0)
    
#     #Store the dataframe in a list
#     datalist.append(df[0])
    
#     #Ask Selenium to click the back button
#     driver.execute_script("window.history.go(-1)") 
    
#     #increment the counter variable before starting the loop over
#     x += 1
    
#     #end loop block
    
# #loop has completed

# #end the Selenium browser session
# driver.quit()

# #combine all pandas dataframes in the list into one big dataframe
# result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

# #convert the pandas dataframe to JSON
# json_records = result.to_json(orient='records')

# #pretty print to CLI with tabulate
# #converts to an ascii table
# print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"],tablefmt='psql'))

# #get current working directory
# path = os.getcwd()

# #open, write, and close the file
# f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
# f.write(json_records)
# f.close()

# driver.quit()