# Dado un algoritmo no dirigido con personajes de la saga de Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas.
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personaje, quienes son.
# d) cargue al menos los siguientes personajes: Luke SkyWalker, Darth Vader, Yoda, Boba Fett,
# C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

from grafo import Grafo
from random import randint

grafo = Grafo(dirigido=False)

grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Yoda')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2-D2')
grafo.insert_vertice('BB-8')

grafo.insert_arist('Luke Skywalker','Darth Vader',randint(1,10))
grafo.insert_arist('Darth Vader','Rey',randint(1,10))
grafo.insert_arist('Yoda','BB-8',randint(1,10))
grafo.insert_arist('Kylo Ren','Leia',randint(1,10))
grafo.insert_arist('Rey','Boba Fett',randint(1,10))
grafo.insert_arist('Chewbacca','R2-D2',randint(1,10))
grafo.insert_arist('Luke Skywalker','C-3PO',randint(1,10))
grafo.insert_arist('Han Solo','Darth Vader',randint(1,10))

#!B
print('B')
exp_minima= grafo.kruskal()
check = 0
for arbol in exp_minima:
    for nodo in arbol.split(';'):
        partes = nodo.split('-')
        print(partes)
        if 'Yoda' in partes:
            check=+1

if check>=1:
    print()
    print('Yoda está en el arbol de expasión mínima.')

print()

#!C
#No puede hacer
