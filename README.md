# Open Campus KnowledGraph Tools

Estas son las herramientas para generar la base de conocimiento de Open Campus

## Requerimientos

Los requerimientos iniciales se encuentran en el archivo requirements.txt

Python +3.7

## Instalacion
Para instalar las dependencias necesarias usar el comando:

``
pip install -r requirements.txt
``

## Uso

Primero ejectura la araña *cursos-list* con el siguiente comando, para extraer de la pagina de Open Campus, el listado de los cursos con sus URLs.

``
crawl cursos-list
``

Ahora ejectur la araña *cursos-meta* con el siguiente comando, para la meta informacion de cada uno de los cursos que se han obtenido con la araña *cursos-list*

``
crawl cursos-meta
``

Seguido ejecutar el notebook de *kg_cursos* para generar el grafo de los cursos, los resultados se pueden visualizar en el archivo.

``
cursos.rdf
``

Tambien ejecutar el notebook de *kg_intents* para generar el grafo de las intenciones.

``
intents.rdf
``

Finalmente ejecutar el script de *mix_graphs.py* para unir los cursos y las intenciones para generar el grafo de conocimiento.
``
final.rdf
``
