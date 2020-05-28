import requests
from bs4 import BeautifulSoup
import json
import csv
from ftfy import fix_encoding
import xml.etree.ElementTree as ET
# Adding to JSON 
# def add_json(data, filename='data.json'): 
#     with open(filename,'w') as f: 
#         json.dump(data, f, indent=4)     

lname = []
lrating = []
limage = []
with open("data.xml","w",encoding="utf-8") as f:
    f.write("<?xml version='1.0'?>\n<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' \n xmlns:cd='http://www.recshop.fake/cd#'>\n")
    for j in range(1,10):
        url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        number = 12
        
        journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
        rates = soup.findAll("div", class_='point highlight-text')[:number]
        images = soup.findAll("div", class_='ri-avatar result-image')[:number]
        for i in range(0, len(journey)):
            sURL = images[i].find('a')['href']
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
                "url": sURL,
                "name":  sName,
                "rate": sRating,
                "image": sImage
            }
            # print(lJson)
            
            data = ET.Element('rdf:Description')
            item1 = ET.SubElement(data, 'cd:url')
            item2 = ET.SubElement(data, 'cd:name')
            item3 = ET.SubElement(data, 'cd:rating')
            item4 = ET.SubElement(data, 'cd:image')
            item5 = ET.SubElement(data, 'cd:id')            
            item1.text = sURL
            item2.text = sName
            item3.text = str(sRating)
            item4.text = sImage
            # item5.text = str((j-1)*12+i) + "^^xsd:double"
            item5.text = str((j-1)*12+i).zfill(3)
            data.tail = "\n"
            item1.tail = "\n"
            item2.tail = "\n"
            item3.tail = "\n"
            item4.tail = "\n"
            item5.tail = "\n"
            myData = ET.tostring(data, encoding="unicode", method='xml')
            f.write(myData)
            # with open("data2.csv","a",encoding='utf-8') as f:            
                # fnames = ["url","name", "rate", "image"]
                # writer = csv.DictWriter(f, fieldnames=fnames)    
                # writer.writerow(lJson)
                

            # with open("data.json") as json_file:
            #     data = json.load(json_file)
            #     temp = data["data"]
            #     temp.append(lJson)
            # add_json(data)
    f.write("</rdf:RDF>")
# print(lname)