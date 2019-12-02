from rdflib import Graph

g1 = Graph()
g1.parse("cursos.rdf")

g2 = Graph()
g2.parse("intents.rdf")

graph = g1 + g2

graph.serialize(destination='final.rdf')
