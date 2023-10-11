# 6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento,
# color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

from arbol_binario_actualizado import BinaryTree, get_value_from_file

file_jedi = open('Arboles\jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

#!A
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
#!B
print ('InOrder de Nombres: ')
name_tree.inorden()
print()
print('InOrder de Ranking: ')
ranking_tree.inorden()
print()
#!C
print('ByLevel de Ranking: ')
ranking_tree.by_level()
print()
print('ByLevel de Especies: ')
specie_tree.by_level()
print()
#!D
pos = name_tree.search('yoda')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')
print()

pose = name_tree.search('luke skywalker')
if pose:
    print(get_value_from_file('jedis.txt', pose.other_values))
else:
    print('no esta en la lista')
print()
#!E
ranking_tree.inorden_file_rank('jedis.txt', 'jedi master')
print()
#!F
name_tree.inorden_file_lightsaber('jedis.txt', 'green')
print()
#!G
name_tree.inorden_file_master('jedis.txt')
print()
#!H
print('Especies Togruta: ')
specie_tree.inorden_file_especie('jedis.txt', 'togruta')
print()
print('Especies Cerean: ')
specie_tree.inorden_file_especie('jedis.txt', 'cerean')
print()
#!I
print('Los jedis que empiezan con la letra A son: ')
name_tree.inorden_start_with_jedi('A')
print()
print('Los jedis que tienen un - en su nombre son: ')
name_tree.inorden_file_jedis('jedis.txt')
