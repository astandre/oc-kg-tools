import rdflib
import requests

# create a Graph
g = rdflib.Graph()

# parse in an RDF file hosted on the Internet
result = g.parse("./cursos.rdf")

curso = rdflib.URIRef("http://127.0.0.1/ockb/course/ontology/Course")
propiedad = rdflib.URIRef("http://127.0.0.1/ockb/course/ontology/courseName")

# qres = g.query(
#     """SELECT ?nombre ?test
#        WHERE {
#           ?nombre rdf:type ?curso .
#           ?nombre ?propiedad ?test .
#        }""", initBindings={'curso': curso, 'propiedad': propiedad})
#


# qres = g.query(
#     """SELECT DISTINCT  ?propiedad
#        WHERE {
#           ?s ?propiedad ?o .
#        }""")


initialMsg = 'Que curso deseas conocer \n'
globalI = 1

# selectedObject = None
# selectedProperty = None

props = [None, None]

baseQuery = """SELECT DISTINCT  ?s
       WHERE {
          ?s ?p ?curso .
       }"""

while True:
    options = {}
    finalResp = None
    queryStr = ""

    if props[0]:
        message = ""
        queryStr = """SELECT DISTINCT  ?p
               WHERE {
                  ?curso ?p ?o .
               }"""
        qres = g.query(queryStr, initBindings={'curso': props[0]})
        if props[1]:
            queryStr = """SELECT DISTINCT  ?o
                   WHERE {
                      ?curso ?propiedad ?o .
                   }"""
            qres = g.query(queryStr, initBindings={'curso': props[0], 'propiedad': props[1]})

    else:
        message = initialMsg
        qres = g.query(baseQuery, initBindings={'curso': curso})

    print('Query ', queryStr)
    print('Resp ', len(qres))

    i = 0
    isLiteral = False
    for row in qres:
        # print(type(row[0]))
        if isinstance(row[0], rdflib.term.Literal):
            # print('Literal ', row[0])
            isLiteral = True
        #
        # if isinstance(row[0], rdflib.term.URIRef):
        #     print('Objeto ', row[0])
        options[i] = row[0]
        i += 1

    # print(options)

    for index, option in enumerate(options):
        if index < 5:
            # print(options[option], index)
            message += f'{index}) {options[option]} \n'
    print(message)
    if isLiteral and len(qres) == 1:
        props = [None, None]
    else:
        select = int(input('> '))
        print('Ha seleccionado ', options[select])
        if globalI % 2 != 0:
            props[0] = options[select]
            props[1] = None
        if globalI % 2 == 0:
            props[1] = options[select]

        globalI += 1
