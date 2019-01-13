from browsermobproxy import Server
import json

server = Server('/Users/harrisonwjy/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy')

server.start()
proxy = server.create_proxy()

from selenium import webdriver
co = webdriver.ChromeOptions()
co.add_argument('--proxy-server={host}:{port}'.format(host='localhost', port=proxy.port))

driver = webdriver.Chrome(chrome_options=co)

proxy.new_har('req',options={'captureHeaders': True,'captureContent':True})

driver.get('https://www.gv.com.sg/GVHome#/')
#print(proxy.har)  # returns a HAR

filename = 'proxyHar.json'
f = open(filename,"w")
movieResults = json.dumps(proxy.har,indent=4)
f.write(movieResults)
f.close()

# for ent in proxy.har['log']['entries']:
#     _url = ent['request']['url']
#     _response = ent['response']
#     _content = _response['content']['text']