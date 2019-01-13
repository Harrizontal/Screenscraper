import requests
from bs4 import BeautifulSoup


# response = requests.get("https://www.walmart.com/search/?query=water&cat_id=0")
# doc = BeautifulSoup(response.text, 'html.parser')
#
# # Grab all of the titles
# title_tags = doc.find_all(class_='prod-ProductTitle')
#
# # Let's print the first 5
# for title in title_tags[:5]:
#     print(title.text.strip())
#
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
#
#

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8,ja;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': 217,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONIDP1=0000d6ybYEb3ITIHU8RaoIlLKrJ:19nr4sl2a; PD_STATEFUL_4b59ea50-9738-11e5-bed7-74fe48068c63=%2Fwebapp; BIGipServerhdb_rp_http_pool=!OIjkhw1PetIWBCI8p2SC/TVKwmPbZuVl/oSqIg5nIThkoCkY6HkPXhrZVkfwKiPPZJXtuAVmzcl4ma8=; PD_STATEFUL_c1cfe488-94b2-11e5-8b7f-74fe48068c63=%2Fweb; PD_STATEFUL_c1b1031a-94b2-11e5-8b7f-74fe48068c63=%2Fweb; TS01170d4d=01e2ec192a4bfe96dcf24f15b43111bdc74b530773ab4b912cd73ed5d2cc1db19e87e47d9559d1e93f00c4bfe58f3563ed0f745cb804025873d217d25327ef8e560e9c8995e9f8b9451ba5f93a54e414d7504b98f089b5d03aa9f03383ce76440b0937db0a',
    'Host':'services2.hdb.gov.sg',
    'Origin': 'https://services2.hdb.gov.sg',
    'Referer': 'https://services2.hdb.gov.sg/webapp/BB33RTIS/BB33PReslTrans.jsp',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

headers2 ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

data = {
'USER_PROFILE': 1,
'FLAT_TYPE': 05,
'NME_NEWTOWN':'',
'NME_STREET': 'Cantonment Rd',
'NUM_BLK_FROM': '1G',
'NUM_BLK_TO':'',
'dteRange':12,
'DTE_APPROVAL_FROM': 'Aug 2016',
'DTE_APPROVAL_TO': 'Aug 2018',
'AMT_RESALE_PRICE_FROM': '',
'AMT_RESALE_PRICE_TO': '',
'Process': 'continue',
'null': 'null'

}

url = 'https://www.gv.com.sg/GVMovieDetails#/movie/6289/cinema/80'
url2 = 'https://services2.hdb.gov.sg/webapp/BB33RTIS/BB33SSearchWidget'
response = requests.get(url, headers=headers2)
doc = BeautifulSoup(response.text, 'html.parser')

print response.status_code

# Grab all of the rows
row_tags = doc.find_all('li')

# Let's print the first 5
for row in row_tags[:90]:
    print(row.text.strip())
#
# for link in doc.find_all('a'):
#     print(link.get('href'))
#
# print(doc.get_text())



# url = raw_input("harrizontal.com")
#
# r  = requests.get("http://" +url)
#
# data = r.text
#
# soup = BeautifulSoup(data)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
