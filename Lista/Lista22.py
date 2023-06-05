'''
Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
'''
from Clase_Lista import Lista

class Jedi:
    def __init__(self, nombre, maestro, sable, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.sable = sable
        self.especie = especie
    
    def __str__(self):
        return f'{self.nombre} - {self.maestro} - {self.sable} - {self.especie}'
    
J1 = Jedi('Ahsoka Tano', 'a', 'amarillo', 'a')
J2 = Jedi('Kit Fisto', 'b', 'violeta', 'b')
J3 = Jedi('c', 'Yoda', 'rojo y verde', 'c')
J4 = Jedi('d', 'Luke Skywalker', 'd', 'd')
J5 = Jedi('e', 'e', 'e', 'humana')
J6 = Jedi('f', 'f', 'f', 'twi lek')
J7 = Jedi('A', 'Qui-Gon Jin', 'verde', 'a')
J8 = Jedi('b', 'Mace Windu', 'b', 'b')

#a
lista_nombre = Lista()
lista_especie = Lista()

lista_nombre.insert(J1, 'nombre')
lista_nombre.insert(J2, 'nombre')
lista_nombre.insert(J3, 'nombre')
lista_nombre.insert(J4, 'nombre')
lista_nombre.insert(J5, 'nombre')
lista_nombre.insert(J6, 'nombre')
lista_nombre.insert(J7, 'nombre')
lista_nombre.insert(J8, 'nombre')

lista_nombre.barrido()
print()

lista_nombre.order_by('especie', False)
lista_nombre.barrido()

#b
print()
tano = lista_nombre.search('Ahsoka Tano', 'nombre')
if tano != None:
    print ('La información de Ahsoka Tano es: ', lista_nombre.get_element_by_index(tano))

kit = lista_nombre.search('Kit Fisto', 'nombre')
if kit != None:
    print ('La información de Kit Fisto es: ', lista_nombre.get_element_by_index(kit))
print()

#c
jedis = ['Yoda', 'Luke Skywalker']
for i in range (lista_nombre.size()):
    if lista_nombre.get_element_by_index(i).maestro in jedis:
        print ('Los aprendices de Yoda y Luke son: ', lista_nombre.get_element_by_index(i).nombre)
    elif lista_nombre.get_element_by_index(i).maestro == 'Qui-Gon Jin':
        print ('Los aprendices de Qui-Gon son: ', lista_nombre.get_element_by_index(i).nombre)
    elif lista_nombre.get_element_by_index(i).maestro == 'Mace Windu':
        print ('Los aprendices de Mace son: ', lista_nombre.get_element_by_index(i).nombre)
    else:
        pass
print ()

#d
for i in range(lista_nombre.size()):
    if lista_nombre.get_element_by_index(i).especie == 'humana':
        print (lista_nombre.get_element_by_index(i).nombre, ' es humano.')
    elif lista_nombre.get_element_by_index(i).especie == 'twi lek':
        print (lista_nombre.get_element_by_index(i).nombre, ' es Twi lek.')
    else:
        pass
print ()

#e
print ()
for i in range(lista_nombre.size()):
    if lista_nombre.get_element_by_index(i).nombre[0] == 'A':
        print ('Los yedis que son empiezan con A son: ', lista_nombre.get_element_by_index(i).nombre)
print ()
#f
for i in range(lista_nombre.size()):
    if ' ' in lista_nombre.get_element_by_index(i).sable:
        print (lista_nombre.get_element_by_index(i).nombre, ' tiene un sable de dos colores.')
    elif lista_nombre.get_element_by_index(i).sable == 'amarillo':
        print (lista_nombre.get_element_by_index(i).nombre, ' tiene un sable amarillo.')
    elif lista_nombre.get_element_by_index(i).sable == 'violeta':
        print (lista_nombre.get_element_by_index(i).nombre, ' tiene un sable violeta.')
    else:
        pass
