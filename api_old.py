from seleniumwire import webdriver  # Import from seleniumwire
import json
import datetime
# Create a new instance of the Firefox driver
chrome_options = webdriver.ChromeOptions()
chrome_options.accept_untrusted_certs = True
chrome_options.assume_untrusted_cert_issuer = True
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("test-type")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
        chrome_options=chrome_options
)

# # Go to the Google home page
# url = "http://www.gv.com.sg/#/"
# driver.get(url)

# driver.close()
# # Access requests via the `requests` attribute
# count = 0
# for request in driver.requests:
#     if request.response:
#         if "homenowshowing" in request.path:
#             print(
#                 request.path,
#                 request.response.status_code,
#                 request.response.body
#             )
#             filename = 'test'+str(count)+'.json'
#             f = open(filename,"w") #FHSU
#             movieResults = json.dumps(request.response.body)
#             f.write(movieResults)
#             f.close()
#             count += 1

def retrieveMovieList():
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # # Go to the Google home page
        driver.get("https://www.gv.com.sg/#/")

        # Access requests via the `requests` attribute
        for request in driver.requests:
                if request.response:
                        if "homenowshowing" in request.path:
                                filename = 'movieList.json'
                                f = open(filename,"w")
                                movieResults = json.dumps(request.response.body,indent=4)
                                f.write(movieResults)
                                f.close()
        driver.close()



# for (k, v) in data.items():
#    print("Key: " + k)
#    print("Value: " + str(v))


movieTitleArray = []
movieIdArray = []
linkArray = []

def getMovieList():
        f = open('movieList.json')
        data = json.load(f)
        for item in data['data']:
                movieTitleArray.append(item['filmTitle'])
                movieIdArray.append(item['filmCd'])
                linkArray.append("https://www.gv.com.sg/GVMovieDetails#/movie/"+str(item['filmCd']))
                print("Key: " + str(item['filmCd']) + str(item['filmTitle']))
        f.close()

def retrieveMovieTiming(movieTitleArray, movieIdArray, linkArray):
        driver = webdriver.Chrome(chrome_options=chrome_options)
        for i in range(len(movieIdArray)):
                print(movieTitleArray[i]+ "Accessing link: " + linkArray[i]) 
                driver.get(linkArray[i])
                for request in driver.requests:
                        if request.response:
                                if "sessionforfilm" in request.path:
                                # print(
                                #     request.path,
                                #     request.response.status_code,
                                #     request.response.body
                                # )
                                        filename = 'MovieTimings/movietiming'+movieIdArray[i]+'.json'
                                        f = open(filename,"w")
                                        movieResults = json.dumps(request.response.body, indent=4)
                                        f.write(movieResults)
                                        f.close()
                driver.back()
                
        driver.quit()

def gettMovieTimingLinks():
        # T = blocked, D = occupied, L = Available
        # https://www.gv.com.sg/GVSeatSelection#/cinemaId/{}/filmCode/{}/showDate/{}showTime/{}/hallNumber/{}
        mainArray = []
        
        f = open('MovieTimings/movietiming3568.json')
        count = 0
        data = json.load(f)
        for item in data['data']['locations']:
                print("id: " + str(item['id']) +" "+str(item['name']))
                cinemaId = str(item['id'])
                filmCode = str(data['data']['filmCd'])
                for item2 in item['dates']:
                        #print("Date available: " + str(item2['date']) + " -> "+ str(datetime.datetime.fromtimestamp(item2['date']/1000.0)))
                        for times in item2['times']:
                                movieDetail = []
                                midnightDate = convertDate(times['midnightDate'])
                                showTime = str(times['time24'])
                                hallNumber = str(times['hallNumber'])
                                movieDetail.append(cinemaId)
                                movieDetail.append(midnightDate)
                                movieDetail.append(showTime)
                                movieDetail.append("https://www.gv.com.sg/GVSeatSelection#/cinemaId/{0}/filmCode/{1}/showDate/{2}/showTime/{3}/hallNumber/{4}".format(
                                cinemaId,filmCode,midnightDate,showTime,hallNumber))
                                mainArray.append(movieDetail)
                                # print("https://www.gv.com.sg/GVSeatSelection#/cinemaId/%s/filmCode/%s/showDate/%s/showTime/%s/hallNumber/%s" %
                                # (cinemaId,filmCode,midnightDate,showTime,hallNumber))
                                count+=1
                               

        f.close()
        print(count)
        return mainArray

def retrieveSeats(arrayOfMovieDetail):
        driver = webdriver.Chrome()
        count = 0
        for value in arrayOfMovieDetail:
                driver.get(value[3])
                for request in driver.requests:
                        if request.response:
                                if "seatplan" in request.path:
                                # print(
                                #     request.path,
                                #     request.response.status_code,
                                #     request.response.body
                                # )
                                        filename = "MovieTimings/3568/{0}_{1}_{2}_{3}.json".format(count,value[0],value[1],value[2])
                                        f = open(filename,"w")
                                        seatResults = json.dumps(request.response.body, indent=4)
                                        f.write(seatResults)
                                        f.close()
                count+=1
                driver.back()

def convertDate(miliseconds):
        return str(datetime.datetime.fromtimestamp(miliseconds//1000.0).date().strftime('%d-%m-%Y'))

retrieveMovieList()
getMovieList()
retrieveMovieTiming(movieTitleArray, movieIdArray,linkArray)
#print(datetime.datetime.fromtimestamp(1546099200000//1000.0).date().strftime('%d-%m-%Y'))
#movieTimingLinksArray = gettMovieTimingLinks()
# retrieveSeats(movieTimingLinksArray)
print(len(linkArray))
