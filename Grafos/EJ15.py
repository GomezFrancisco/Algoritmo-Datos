# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
# y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.
from grafo import Grafo
#!A
grafo=Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'
    
grafo.insert_vertice(Maravilla("Gran Muralla", ['China'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Machu Picchu", ['Peru'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Arco del Triunfo", ['Francia'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Cataratas", ['Argentina', 'Brasil'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Isla Jeju", ['Corea del Sur'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Salar de Uyuni", ['Bolivia'], 'Natural'), criterio= 'nombre')

grafo.insert_arist('Gran Muralla', 'Machu Picchu', 8, criterio_vertice='nombre')
grafo.insert_arist('Machu Picchu', 'Arco del Triunfo', 8, criterio_vertice='nombre')
grafo.insert_arist('Cataratas', 'Isla Jeju', 8, criterio_vertice='nombre')
grafo.insert_arist('Isla Jeju', 'Salar de Uyuni', 8, criterio_vertice='nombre')

print('BARRIDO GENERAL')
grafo.barrido()
print()
#!B
print('CAMINO MÁS CORTO')
ori = 'Gran Muralla'
des = 'Arco del Triunfo'
origen = grafo.search_vertice(ori, criterio='nombre')
destino = grafo.search_vertice(des, criterio='nombre')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des, criterio='nombre')):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]
print()

#!C
print('ARBOL DE EXPANSIÓN MÍNIMA -- ARQUITECTURAS')
print()
grafo_A = Grafo(dirigido=False)

grafo_A.insert_vertice(Maravilla("Gran Muralla", ['China'], 'Arquitectonica'), criterio='nombre')
grafo_A.insert_vertice(Maravilla("Machu Picchu", ['Peru'], 'Arquitectonica'), criterio='nombre')
grafo_A.insert_vertice(Maravilla("Arco del Triunfo", ['Francia'], 'Arquitectonica'), criterio='nombre')

grafo_A.insert_arist('Gran Muralla', 'Machu Picchu', 8, criterio_vertice='nombre')
grafo_A.insert_arist('Machu Picchu', 'Arco del Triunfo', 8, criterio_vertice='nombre')

bosque_A = grafo_A.kruskal()
for arbol in bosque_A:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)
print()
print('ARBOL DE EXPANSIÓN MÍNIMA -- NATURALES')
print()
grafo_N = Grafo(dirigido=False)

grafo_N.insert_vertice(Maravilla("Cataratas", ['Argentina', 'Brasil'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Isla Jeju", ['Corea del Sur'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Salar de Uyuni", ['Bolivia'], 'Natural'), criterio= 'nombre')
grafo_N.insert_arist('Cataratas', 'Isla Jeju', 8, criterio_vertice='nombre')
grafo_N.insert_arist('Isla Jeju', 'Salar de Uyuni', 8, criterio_vertice='nombre')

bosque_N = grafo_N.kruskal()
for arbol in bosque_N:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)
print()
#!D
pais_1 = input('ingrese el pais a consultar: ')
print(grafo.barrido_maravillas(pais_1))
#!E
print()

print('Barrido de tipos de maravillas')
pais = input('ingrese el pais a consultar: ')
print (grafo.barrido_tipos(pais))