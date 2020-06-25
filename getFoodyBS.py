import requests
from bs4 import BeautifulSoup
import json
import csv
from ftfy import fix_encoding
import xml.etree.ElementTree as ET
from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, FOAF
# Adding to JSON 
# def add_json(data, filename='data.json'): 
#     with open(filename,'w') as f: 
#         json.dump(data, f, indent=4)     

customNamespace = Namespace("http://www.hnag.com/")
graph = Graph()
graph.bind("res", customNamespace)

for j in range(1,2):
    url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    number = 12

    journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
    rates = soup.findAll("div", class_='point highlight-text')[:number]
    images = soup.findAll("div", class_='ri-avatar result-image')[:number]
    addresses = soup.findAll("div", class_='address')[:number]
    for i in range(0, len(journey)):
        sURL = images[i].find('a')['href']
        sName = journey[i].find("h2").text
        sName.strip("\n\r\n")
        sName = sName[43:len(sName) - 39]
        sName = fix_encoding(sName)  
        sRating = rates[i].text
        sRating.strip("\n\r\n")
        sRating = sRating[38:len(sRating) - 32]
        sRating = float(sRating)
        sImage = images[i].find('img')['src']
        sAddress = str(addresses[i].find('span').text).replace('\n', '').replace('\r', '')
        sAddress = sAddress.split(", ")[0].strip()
        # sAddress = sAddress.split(", ")[1]

        place = URIRef(str((j-1)*12+i))
        url = Literal(sURL)
        name = Literal(sName)
        rating = Literal(sRating)
        image = Literal(sImage)
        address = Literal(sAddress)
        id = Literal((j-1)*12+i)

        graph.add((place, customNamespace.url, Literal(sURL)))
        graph.add((place, customNamespace.rating, Literal(sRating)))
        graph.add((place, customNamespace.image, Literal(sImage)))
        graph.add((place, customNamespace.name, Literal(name)))
        graph.add((place, customNamespace.address, Literal(address)))
        graph.add((place, customNamespace.id, Literal((j-1)*12+i)))    
graph.serialize(destination='restaurants.xml', format='xml')