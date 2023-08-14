from Clase_lista_lista import Lista
from random import randint


# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10), cb_ganadas= randint(1, 20), cb_perdidas= randint(1, 20))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10), cb_ganadas= randint(1, 20), cb_perdidas= randint(1, 20))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10),  cb_ganadas= randint(1, 20), cb_perdidas= randint(1, 20))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))
p6 = Pokemon('charizard', 'fuego', randint(1, 20), 'planta')
p7 = Pokemon('Blastoise', 'agua', randint(1, 20), 'volador')

pokemons = [p1, p2, p3, p4, p5, p6, p7]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()

#! A
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#! B
lista_entrenadores.barrido_cantidad_torneos_ganados(6)

print()
#! C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

pokemon_mayor = sublista.get_element_by_index(0)
for pos in range(1, sublista.size()):
    pokemon = sublista.get_element_by_index(pos)
    if pokemon.nivel > pokemon_mayor.nivel:
        pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')

#! D
print()
B = input("Ingrese el entrenador a buscar: ")
search_0 = lista_entrenadores.search(B, 'nombre')
if search_0 != None:
    value = lista_entrenadores.get_element_by_index(search_0)
    entrenador, sublista = value[0], value[1]
    print(entrenador)
    sublista.barrido()
else:
    print('El entrenador {B} no se encuentra en la lista.')

print()
#! E
for i in range(lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(i)[0]
    combates_totales = value.cb_ganadas + value.cb_perdidas
    porcentaje_victorias = (value.cb_ganadas * 100) // combates_totales
    if porcentaje_victorias > 79:
        print (f'El entrenador {value.nombre} obtuvo un porcentaje de victorias mayor al 79%')
    else:
        print (f'El entrenador {value.nombre} obtuvo un porcentaje de victorias menor al 79%')
print()
#! F
for i in range(lista_entrenadores.size()):
    value=lista_entrenadores.get_element_by_index(i)
    entrenador,equipo=value[0],value[1]
    for j in range (equipo.size()):
        if (equipo.get_element_by_index(j).tipo=='fuego' and equipo.get_element_by_index(j).subtipo=='planta') or (equipo.get_element_by_index(j).tipo=='agua' and equipo.get_element_by_index(j).subtipo=='volador'):
            print(f'{entrenador.nombre} tiene pomenones de tipo fuego/planta o agua/volador')
print()
#! G
B1 = input('Ingrese la entrenadora a encontrar: ')
search_1 = lista_entrenadores.search(B1, 'nombre')
if search_1 != None:
    value = lista_entrenadores.get_element_by_index(search_1)
    entrenador = value[0]
    pokemons = value[1]
    cantidad_pokemons = 0
    cantidad_niveles = 0
    for i in range(pokemons.size()):
        nivel = pokemons.get_element_by_index(i).nivel
        cantidad_pokemons += 1
        cantidad_niveles = cantidad_niveles + nivel
    print (f'El promedio de niveles del entrenador {entrenador.nombre} es de {cantidad_niveles // cantidad_pokemons}')
else:
    print(f'El entrenador {B1} no se encuentra en la lista.')
print()
#! H
cont_pokemon = 0
pokemon = input('Ingrese el pokemon: ')
for i in range(lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = value[0], value[1]
    for x in range(sublista.size()):
        value = sublista.get_element_by_index(x)
        if value.nombre == pokemon:
            cont_pokemon += 1
            break
print(f'La cantidad de entrenadores que tienen al {pokemon} es de {cont_pokemon}.')
print()

#! I
for i in range(lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = value[0], value[1]
    check = 0
    for x in range(sublista.size()):
        first = sublista.get_element_by_index(x)
        second = sublista.get_element_by_index(x+1)
        if first == second:
            check += 1
            break
    if check == 1:
        print(f'El entrenador {entrenador.nombre} tiene pokemons repetidos.')
        print('--------')
    else:
        print(f'El entrenador {entrenador.nombre} no tiene pokemons repetidos.')
        print('--------')
print()
#! J
L1 = ['Tyrantrum', 'Terrakion', 'Wingull']
B2 = input('Ingrese el nombre del entrenador: ')
search_2 = lista_entrenadores.search(B2, 'nombre')

if search_2 != None:
    value = lista_entrenadores.get_element_by_index(search_2)
    entrenador, sublista = value[0], value[1]
    for i in range(sublista.size()):
        pokemon = sublista.get_element_by_index(i)
        if pokemon.nombre in L1:
            print(f'El entrenador {B2} tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
    print(f'El entrenador {B2} no tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
else:
    print(f'El entrenador {B2} no se encuentra en la lista.')
print()

#! K
B3 = input('Ingrese el nombre del entrenador: ')
search_3 = lista_entrenadores.search(B3, 'nombre')

if search_3 != None:
    value = lista_entrenadores.get_element_by_index(search_3)
    sublista = value[1]
    pokemon = input('Ingrese el pokemon que quiere consultar: ')
    search_4 = sublista.search(pokemon, 'nombre')
    if search_4 != None:
        print(f'El entrenador {B3} tiene en su equipo a {pokemon}')
    else:
        print(f'{B3} no tiene a {pokemon}')
else:
    print(f'El entrenador {B3} no se encuentra en la lista.')