import rdflib
from rdflib.namespace import FOAF
from rdflib.plugins.sparql import prepareQuery
# start = 10
# end = 15
g = rdflib.Graph()
g = g.parse("data.xml", format="xml")


# end = "020"

# q = prepareQuery('SELECT DISTINCT ?name ?url ?rating ?image ?id WHERE { ?place cd:name ?name. ?place cd:url ?url. ?place cd:rating ?rating. ?place cd:image ?image. ?place cd:id ?id. FILTER (?id > ?start) FILTER (?id < ?end)}')

# result = g.query(q, initNs={"cd":DC},initBindings={'start':start, 'end':end})

# start = rdflib.URIRef('Bob')
start = "Bob"
end = "025"
print(start)
print(end)
st = 'SELECT ?name ?id WHERE { ?place foaf:name ?name. ?place FILTER (?name = ' + '"'+ start + '"' + ')}'
print(st)
q = prepareQuery(st, initNs={"foaf":FOAF})
result = g.query(q)
for row in result:
    print(row.name.toPython())

# # print(str(format(11,">3,d")))
# # print(str(11).zfill(3))

# import requests
# from bs4 import BeautifulSoup
# import json
# import csv
# from ftfy import fix_encoding
# import xml.etree.ElementTree as ET
# # Adding to JSON 
# # def add_json(data, filename='data.json'): 
# #     with open(filename,'w') as f: 
# #         json.dump(data, f, indent=4)     

# lname = []
# lrating = []
# limage = []
# with open("data1.xml","w",encoding="utf-8") as f:
#     f.write("<?xml version='1.0'?>\n<rdf:RDF xmlns:owl='http://www.w3.org/2002/07/owl#' \n xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' \n xmlns:rdfs='http://www.w3.org/2000/01/rdf-schema#'>\n")
#     for j in range(1,10):
#         url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
#         page = requests.get(url)
#         soup = BeautifulSoup(page.text, 'html.parser')
#         number = 12
        
#         journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
#         rates = soup.findAll("div", class_='point highlight-text')[:number]
#         images = soup.findAll("div", class_='ri-avatar result-image')[:number]
#         for i in range(0, len(journey)):
#             sURL = images[i].find('a')['href']
#             sName = str(journey[i].find("h2").text)
#             sName.strip("\n\r\n")
#             sName = sName[43:len(sName) - 39]
#             sName = fix_encoding(sName)        
#             lname.append(sName)
#             sRating = rates[i].text
#             sRating.strip("\n\r\n")
#             sRating = sRating[38:len(sRating) - 32]
#             sRating = float(sRating)
#             lrating.append(sRating)
#             sImage = images[i].find('img')['src']
#             limage.append(sImage)
#             lJson = {
#                 "url": sURL,
#                 "name":  sName,
#                 "rate": sRating,
#                 "image": sImage
#             }
#             # print(lJson)
            
#             data = ET.Element('rdf:Description')
#             item1 = ET.SubElement(data, 'owl:url')
#             item2 = ET.SubElement(data, 'owl:name')
#             item3 = ET.SubElement(data, 'owl:rating')
#             item4 = ET.SubElement(data, 'owl:image')
#             item5 = ET.SubElement(data, 'owl:id')            
#             item1.text = sURL
#             item2.text = sName
#             item3.text = str(sRating)
#             item4.text = sImage
#             # item5.text = str((j-1)*12+i) + "^^xsd:double"
#             item5.text = str((j-1)*12+i).zfill(3)
#             data.tail = "\n"
#             item1.tail = "\n"
#             item2.tail = "\n"
#             item3.tail = "\n"
#             item4.tail = "\n"
#             item5.tail = "\n"
#             myData = ET.tostring(data, encoding="unicode", method='xml')
#             f.write(myData)
#             # with open("data2.csv","a",encoding='utf-8') as f:            
#                 # fnames = ["url","name", "rate", "image"]
#                 # writer = csv.DictWriter(f, fieldnames=fnames)    
#                 # writer.writerow(lJson)
                

#             # with open("data.json") as json_file:
#             #     data = json.load(json_file)
#             #     temp = data["data"]
#             #     temp.append(lJson)
#             # add_json(data)
#     f.write("</rdf:RDF>")
# # print(lname)

# from rdflib import URIRef, BNode, Literal, Graph, Namespace
# from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
#                            PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
#                            VOID, XMLNS, XSD

# bob = URIRef("http://example.org/people/Bob")
# linda = BNode()  # a GUID is generated

# name = Literal('Bob')  # passing a string
# age = Literal(24)  # passing a python int
# height = Literal(76.5)  # passing a python float
# n = Namespace("http://example.org/people/")

# # n.bob  # = rdflib.term.URIRef(u'http://example.org/people/bob')
# # n.eve  # = rdflib.term.URIRef(u'http://example.org/people/eve')


# # RDF.type
# # # = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

# # FOAF.knows
# # # = rdflib.term.URIRef("http://xmlns.com/foaf/0.1/knows")

# # PROF.isProfileOf
# # # = rdflib.term.URIRef("http://www.w3.org/ns/dx/prof/isProfileOf")

# # SOSA.Sensor
# # # = rdflib.term.URIRef("http://www.w3.org/ns/sosa/Sensor")

# g = Graph()
# g.bind("foaf", FOAF)
# g.bind("rs",n)

# g.add((bob, RDF.type, FOAF.Person))
# g.add((bob, FOAF.name, name))
# g.add((bob, FOAF.knows, linda))
# g.add((bob, n.test, height))
# g.add((linda, RDF.type, FOAF.Person))
# g.add((linda, FOAF.name, Literal("Linda")))

# g.serialize(destination='data2.xml', format='xml')
# # print(g.serialize(format="turtle").decode("utf-8"))