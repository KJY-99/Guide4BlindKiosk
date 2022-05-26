import json
import urllib
from urllib.parse  import urlparse
import httplib2 as http #External library

if __name__=="__main__":
 #Authentication parameters
 headers = { 'AccountKey' : 'VD/JsOzJTc6dEt90BHj5dA==', 
 'accept' : 'application/json'} #Don't steal our API key pls

 #API parameters
 uri = 'http://datamall2.mytransport.sg/' #Resource URL
 path = '/ltaodataservice/BusArrivalv2?BusStopCode=12101' #12101 =Ngee Ann Poly Stop
 #Build query string & specify type of API call
 target = urlparse(uri + path)
 print(target.geturl())
 method = 'GET'
 body = ''

 #Get handle to http
 h = http.Http()
 #Obtain results
 response, content = h.request(
 target.geturl(),
 method,
 body,
 headers)
 #Parse JSON to print
 jsonObj = json.loads(content)
 
 #OwnCode (GuanTeng)
 #print(jsonObj["Services"][1]["ServiceNo"]) #testing purpose

#List available bus
 print("List of available bus for NgeeAnnPoly BusStop")
 for x in jsonObj["Services"]:
     print(x["ServiceNo"])
 
 while True:
     print("\nType Exit to exit")
     #temp replacement since voice to text is not working)
     number = input("Enter bus number : " )
     found = False
     if(number == "Exit"):
         break
     #prints next 3 bus number
 
     for x in jsonObj["Services"]:
         if(x["ServiceNo"] == number):
             found = True
             print("\nEstimated Time for Bus {}".format(number))
             for i in range(3):
                 try:
                     i += 1
                     busNo = "NextBus"
                     if( i != 1):
                         busNo += str(i)
                     time = x[busNo]["EstimatedArrival"].split("T") #Without split 2019-02-03T22:57:51+08:00
                     time = time[1].split("+") #Without split 22:57:51+08:00
                     print("BusNo {} : ".format(i) + time[0]) #[22:57:51,08:00]
                 except:
                    print("No more bus available")
     
     if(found == False):
         print("Bus number not found")

