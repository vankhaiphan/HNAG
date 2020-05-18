import requests
from bs4 import BeautifulSoup
import json
import csv
from ftfy import fix_encoding
# Adding to JSON 
# def add_json(data, filename='data.json'): 
#     with open(filename,'w') as f: 
#         json.dump(data, f, indent=4)     

lname = []
lrating = []
limage = []
for j in range(1,10):
    url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    number = 12
    journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
    rates = soup.findAll("div", class_='point highlight-text')[:number]
    images = soup.findAll("div", class_='ri-avatar result-image')[:number]

    for i in range(0, len(journey)):
        sName = str(journey[i].find("h2").text)
        sName.strip("\n\r\n")
        sName = sName[43:len(sName) - 39]
        sName = fix_encoding(sName)        
        lname.append(sName)
        sRating = rates[i].text
        sRating.strip("\n\r\n")
        sRating = sRating[38:len(sRating) - 32]
        sRating = float(sRating)
        lrating.append(sRating)
        sImage = images[i].find('img')['src']
        limage.append(sImage)
        lJson = {
            "name":  sName,
            "rate": sRating,
            "image": sImage
        }
        print(lJson)
        with open("data.csv","a",encoding='utf-8') as f:            
            fnames = ["name", "rate", "image"]
            writer = csv.DictWriter(f, fieldnames=fnames)    
            writer.writerow(lJson)
        # with open("data.json") as json_file:
        #     data = json.load(json_file)
        #     temp = data["data"]
        #     temp.append(lJson)
        # add_json(data)
# print(lname)