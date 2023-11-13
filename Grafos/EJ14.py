# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
# tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from grafo import Grafo

grafo=Grafo(dirigido=False)
from random import randint


#!B

#Vertices
grafo.insert_vertice('cocina')
grafo.insert_vertice('comedor')
grafo.insert_vertice('cochera')
grafo.insert_vertice('quincho')
grafo.insert_vertice('baño 1')
grafo.insert_vertice('baño 2')
grafo.insert_vertice('habitacion 1')
grafo.insert_vertice('habitacion 2')
grafo.insert_vertice('sala de estar')
grafo.insert_vertice('terraza')
grafo.insert_vertice('patio')

#Aristas
grafo.insert_arist('cocina','comedor',randint(1,10))
grafo.insert_arist('cocina','baño 1',randint(1,10))
grafo.insert_arist('cocina','sala de estar',randint(1,10))
grafo.insert_arist('quincho','patio',randint(1,10))
grafo.insert_arist('cochera','sala de estar',randint(1,10))
grafo.insert_arist('comedor','patio',randint(1,10))
grafo.insert_arist('comedor','terraza',randint(1,10))
grafo.insert_arist('comedor','baño 2',randint(1,10))
grafo.insert_arist('comedor','quincho',randint(1,10))
grafo.insert_arist('baño 1','baño 2',randint(1,10))
grafo.insert_arist('baño 1','patio',randint(1,10))
grafo.insert_arist('baño 1','habitacion 1',randint(1,10))
grafo.insert_arist('baño 1','habitacion 2',randint(1,10))
grafo.insert_arist('cochera','baño 2',randint(1,10))
grafo.insert_arist('cochera','habitacion 1',randint(1,10))
grafo.insert_arist('habitacion 1','quincho',randint(1,10))
grafo.insert_arist('habitacion 2','patio',randint(1,10))
grafo.insert_arist('habitacion 2','terraza',randint(1,10))
grafo.insert_arist('sala de estar','terraza',randint(1,10))


#!C
bosque = grafo.kruskal()

acum=0
for arbol in bosque:
    for nodo in arbol.split(';'):
        print(nodo)
        acum+=int(nodo[-1])

print(f'se necesitara un total de {acum} metros de cables')

#!D
camino = grafo.dijkstra("habitacion 1","sala de estar")

acum=0
fin = "sala de estar"
while camino.size()>0:
    value = camino.pop()
    if value[0] == fin:
        print(value)
        fin = value[2]
        acum+=value[1]

print(f"Se necesitan {acum} metros para conectar la habitacion 1 y la sala de estar")