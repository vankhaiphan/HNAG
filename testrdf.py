import rdflib
from rdflib.plugins.sparql import prepareQuery
start = 10
end = 15
g = rdflib.Graph()
g = g.parse("data.xml", format="xml")

result = g.query("""
    PREFIX cd:<http://www.recshop.fake/cd#>
    SELECT ?name ?url ?rating ?image ?id
    WHERE {
        ?place cd:name ?name.
        ?place cd:url ?url.
        ?place cd:rating ?rating.
        ?place cd:image ?image.
        ?place cd:id ?id.
    } 
    ORDER BY ?id
    LIMIT ?limit""", initBindings={'limit':'9'})
for row in result:
    print(row.id.toPython())

# print(str(format(11,">3,d")))
# print(str(11).zfill(3))
