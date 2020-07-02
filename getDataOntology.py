import requests
from bs4 import BeautifulSoup
import json
from ftfy import fix_encoding
from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, FOAF
from SPARQLWrapper import SPARQLWrapper, JSON
# Adding to JSON 
# def add_json(data, filename='data.json'): 
#     with open(filename,'w') as f: 
#         json.dump(data, f, indent=4)   
  
sparql = SPARQLWrapper("http://localhost:7200/repositories/HNAG/statements")
customNamespace = Namespace("http://www.hnag.com/")

def addCityAndDistricts():
    districtNames = ['Hải Châu', 'Cẩm Lệ', 'Hoà Vang', 'Liên Chiểu', 'Ngũ Hành Sơn', 'Sơn Trà', 'Thanh Khê', 'Hoàng Sa']
    districtId = ['hai-chau', 'cam-le', 'hoa-vang', 'lien-chieu', 'ngu-hanh-son', 'son-tra', 'thanh-khe', 'hoang-sa']
    sparql.setQuery("""
        PREFIX res: <http://www.hnag.com/>
        INSERT DATA {
            <http://www.hnag.com/city/da-nang> res:name "Đà Nẵng" . 
        }
    """)
    sparql.method = 'POST'
    sparql.query()
    for i in range(0, len(districtId)):
        queryString = '''
            PREFIX res:<http://www.hnag.com/>
            INSERT DATA {
            <http://www.hnag.com/district/'''+districtId[i]+'''> res:name "'''+districtNames[i]+'''";
                                    res:inCity <http://www.hnag.com/city/da-nang> .                                    
            }
        '''
        print(queryString)
        sparql.setQuery(queryString)
        sparql.method = 'POST'        
        sparql.query()

def addPlaces():
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

            sName = journey[i].find("h2").text.strip()
            sName = fix_encoding(sName)  

            sRating = rates[i].text.strip("\n\r\n").strip()
            # sRating = float(sRating)

            sImage = images[i].find('img')['src']

            sAddress = str(addresses[i].find('span').text).replace('\n', '').replace('\r', '')
            sAddress = sAddress.split(", ")[0].strip()
            # sAddress = sAddress.split(", ")[1]
            id = str((j-1)*12+i)

            queryString = '''
                PREFIX res:<http://www.hnag.com/>
                INSERT DATA {
                    res:res'''+id+'''   res:url "'''+sURL+'''";
                                        res:rating '''+sRating+''';
                                        res:image "'''+sImage+'''";
                                        res:name "'''+sName+'''";
                                        res:address _:address'''+id+''';
                                        res:id '''+id+''' . 
                }
            '''
            # print(queryString)
            sparql.setQuery(queryString)
            sparql.method = 'POST'
            sparql.query()

            addressDetails = addresses[i].findAll('span')
            if (len(addressDetails) > 3):
                street = addressDetails[1].text
                district = addressDetails[2].text
                district = district[5:len(district)]
                city = addressDetails[3].text
                insertAddress(id, street, district, city)

def insertAddress(id, street, district, city):
    queryString = '''
        PREFIX res:<http://www.hnag.com/>
        INSERT {
            ?blankNode  res:street "'''+street+'''";
                        res:district ?district;
                        res:city ?city
        }
        WHERE {
            ?place res:address ?blankNode.
            ?place res:id '''+id+'''.
            ?district res:name "'''+district+'''".
            ?city res:name "'''+city+'''" .
        }
    '''
    print(queryString)
    sparql.setQuery(queryString)
    sparql.method = 'POST'
    sparql.query()

def standardizedAddress(text):
    return text.replace('\n', '').replace('\r', '').split(", ")[0].strip()
# test()
addCityAndDistricts()
addPlaces()