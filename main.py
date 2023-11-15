import os
import csv
import json
import requests


#get Current Directory
crrDir = os.path.dirname(__file__)

#get login.json(ID,password)
with open(crrDir+"\\login.json") as f:
    login = json.load(f)

#get config.json(Apikey,Sysmtedivision)
with open(crrDir+"\\config.json") as f:
    config = json.load(f)

#set URL
authURL = "https://zeroden.enetsystems.co.jp/api/v1/client/auth/login"
wattUsageURL = "https://zeroden.enetsystems.co.jp/api/v1/client/mypage/watt-usage"
wattUsageLatestURL = "https://zeroden.enetsystems.co.jp/api/v1/client/mypage/watt-usage/latest?name="

#set Headers
headers = {
            'Apikey': config["Apikey"],
            'Systemdivision': config["Systemdivision"],
            'Authorization': 'Bearer {}'
          }

#main Function
def main():
    #Get Authentication from Zeroden
    auth = requests.post(authURL, headers=headers, json=login).json()
    
    #set token to headers
    headers["Authorization"] = headers["Authorization"].format(auth["token"])

    #Get watt-usage List
    usageList = requests.get(wattUsageURL, headers=headers).json()["list"]
    
    for num in range(len(usageList)):
        #Get watt-usage detail
        usageDetail = requests.get(wattUsageLatestURL+usageList[num]["name"], headers=headers).json()
        print(f'{usageList[num]["target_month_display"]}の電気代 : {str(usageDetail["tax_billing"])}円')    

#set Current Directory
def getConfig(fileName):
    with open(fileName, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        dictCSV = {row[0]:row[1] for row in csvreader}        
    return dictCSV

if __name__ == '__main__':
    main()
