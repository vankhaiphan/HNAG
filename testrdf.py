import rdflib
from rdflib.plugins.sparql import prepareQuery 
g = rdflib.Graph()
g = g.parse("output.xml", format="xml")
# result = g.query("""
#     SELECT ?id ?url ?rating
#     WHERE {        
#         ?place cd:id ?id.
#         ?place cd:url ?url.
#         ?place cd:rating ?rating.
#         FILTER (?id > 1)
#     } ORDER BY ?id""")
# q = prepareQuery("""
#     SELECT ?id ?url ?rating
#     WHERE {        
#         ?place cd:id ?id.
#         ?place cd:url ?url.
#         ?place cd:rating ?rating.
#         FILTER (?id > ?number)
#     } ORDER BY ?id""")
# q = prepareQuery(
#         'SELECT ?id WHERE { ?place cd:id ?id. FILTER (?id > number)} ORDER BY ?id',
#         initNs = { "number": 5 })
number = 5
result = g.query('SELECT ?id WHERE { ?place cd:id ?id. FILTER (?id > '+ str(number) +') . FILTER (?id < '+ str(number+10) +') } ORDER BY ?id')
for row in result:
    print(row.id.toPython())

# from rdflib import URIRef, BNode, Literal, Graph
# g = Graph()
# g.bind("foaf", FOAF)

# g.add((bob, RDF.type, FOAF.Person))
# g.add((bob, FOAF.name, name))
# g.add((bob, FOAF.knows, linda))
# g.add((linda, RDF.type, FOAF.Person))
# g.add((linda, FOAF.name, Literal("Linda")))

# print(g.serialize(format="xml").decode("utf-8"))

# from rdflib import Namespace, URIRef, Graph, Literal
# from rdflib.namespace import RDF, FOAF

# data = Namespace("http://www.example.org/")


# g = Graph()
# g.bind("cd", data)
# place = URIRef("http://example.org/people/Bob")
# url = Literal('/da-nang/gogi-house-quan-nuong-han-quoc-vincom-center-da-nang')
# rating = Literal(7.6)

# g.add((place, data.url, url))
# g.add((place, data.rating, rating))

# place = URIRef("")
# url = Literal('/da-nang/gogi-house-quan-nuong-han-quoc-vincom-center-da-nang')
# rating = Literal(8)

# g.add((place, data.url, url))
# g.add((place, data.rating, rating))


# #write attempt
# g.serialize(destination='output.xml', format='xml')

# result = g.query("""
#     SELECT ?url ?rating
#     WHERE {
#         ?place cd:url ?url.
#         ?place cd:rating ?rating.
#         FILTER (?rating > 7.5)
#     } ORDER BY ?rating""")
# for row in result:
#     print(row.id.toPython())
