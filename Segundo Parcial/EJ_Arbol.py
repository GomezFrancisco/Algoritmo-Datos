# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

from arbol_binario_actualizado import BinaryTree

pokemons = [
    {'nombre': "test", 'numero': 1, 'tipo': 'neutral'},
    {'nombre': "Jolteon", 'numero': 2, 'tipo': 'eléctrico'},
    {'nombre': "Lycanroc", 'numero': 2, 'tipo': 'neutral'},
    {'nombre': "Tyrantrum", 'numero': 3, 'tipo': 'acero'},
]

arbol_nombres = BinaryTree()
arbol_numeros = BinaryTree()
arbol_tipos = BinaryTree()

for pokemon in pokemons:
    arbol_nombres.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],"tipo": pokemon['tipo']})
    arbol_numeros.insert_node(pokemon['numero'], {'nombre': pokemon['nombre'],"tipo": pokemon['tipo']})
    arbol_tipos.insert_node(pokemon['tipo'], {'nombre': pokemon['nombre'],"numero": pokemon['numero']})

print('B')
#Ingrese el número a buscar:
num = int(input('Ingrese el número del pokemon a encontrar:'))
arbol_numeros.inorden_numero(num)
print()
name = input('Ingrese el nombre del pokemon a encontrar')
arbol_nombres.search_by_coincidence(name)
print()
print('C')
type = input('Ingrese el tipo del pokemon a encontrar: ') #Se puede ingresar cualquier tipo de pokemon
arbol_numeros.inorden_tipo(type)
print()

#Listado ascendente
print('D')
print('Listado ascendente por nombres')
arbol_nombres.postorden_other_values()
print()
print('Listado ascendente por números')
arbol_numeros.postorden_other_values()
print()
print('Listado por nivel de nombres')
arbol_nombres.by_level_otherValues()
print()
#? E
print('E')
bus_1 = arbol_nombres.search('Jolteon')
if bus_1:
    print (bus_1.value, bus_1.other_values)
else:
    print('No se encuentra en la lista')
print()
bus_2 = arbol_nombres.search('Lycanroc')
if bus_1:
    print (bus_2.value, bus_2.other_values)
else:
    print('No se encuentra en la lista')
print()
bus_3 = arbol_nombres.search('Tyrantrum')
if bus_3:
    print (bus_3.value, bus_3.other_values)
else:
    print('No se encuentra en la lista')
print()
#?F
print('F')
print('El número de pokemon de tipo neutral es: ', arbol_nombres.contar_tipo('neutral'))