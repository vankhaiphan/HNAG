import requests
from bs4 import BeautifulSoup
import json
import csv
from ftfy import fix_encoding
import xml.etree.ElementTree as ET
from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, FOAF

def standardizedAddress(text):
    # return text.replace('\n', '').replace('\r', '').strip()
    return text

customNamespace = Namespace("http://www.hnag.com/")
graph = Graph()
graph.bind("res", customNamespace)

for j in range(1,2):
    url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    number = 12
    
    addresses = soup.findAll("div", class_='address')[:number]
    for i in range(0, number):

        # sAddress = str(addresses[i].find('span').text).replace('\n', '').replace('\r', '')
        # sAddress = sAddress.split(", ")[0].strip()
        # # sAddress = sAddress.split(", ")[1]

        addressDetails = addresses[i].findAll('span')
        # for i in addressDetails:
        #     print(i.text)
        # print("----")
        if (len(addressDetails) > 3):
            street = standardizedAddress(addressDetails[1].text)
            district = standardizedAddress(addressDetails[2].text)
            city = standardizedAddress(addressDetails[3].text)
            print(street+".")
            print(district+".")
            print(city+".")
            print("---")
#         address = Literal(sAddress)
#         id = Literal((j-1)*12+i)
        
#         graph.add((place, customNamespace.address, Literal(address)))
#         graph.add((place, customNamespace.id, Literal((j-1)*12+i)))    
# graph.serialize(destination='restaurants.ttl', format='ttl')

