import rdflib
import csv

from rdflib import URIRef, RDF, Literal, Namespace

data = []
with open('Productos.csv', mode='r', encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        # print(row)
        data.append({
            'id': row['\ufeffid'],
            'name': row['name'],
            'price': row['price'],
            'description': row['description'],
            'image_url': row['image_url'],
            'est_time': row['est_time'],
        })

print(data)

ontoFood = Namespace("http://127.0.0.1/food/ontology/")
foodInstance = Namespace("http://127.0.0.1/food/instance/")
FOOD = ontoFood.Food

# create a Graph
g = rdflib.Graph()

foodRef = URIRef(foodInstance + 'MiRestaurant')

for food in data:
    foodRef = URIRef(foodInstance + food['id'])
    g.add((foodRef, ontoFood.offers, FOOD))
    g.add((foodRef, RDF.type, FOOD))
    g.add((foodRef, ontoFood.name, Literal(food['name'])))
    g.add((foodRef, ontoFood.price, Literal(food['price'])))
    g.add((foodRef, ontoFood.description, Literal(food['description'])))
    g.add((foodRef, ontoFood.est_time, Literal(food['est_time'])))
    g.add((foodRef, ontoFood.image_url, Literal(food['image_url'])))

g.serialize(destination='food.rdf')
