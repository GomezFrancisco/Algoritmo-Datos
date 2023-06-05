'''Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.'''

from Clase_Lista import Lista

class Superheroes():
    def __init__(self, nombre, año, casa, bibliografia):
        self.nombre = nombre
        self.año = año
        self.casa = casa
        self.bibliografia = bibliografia
    
    def __str__(self):
        return f'{self.nombre} - {self.año} - {self.casa} - {self.bibliografia}'
    
personaje1 = Superheroes('Linterna Verde', 10, 'DC', 'Es verde')
personaje2 = Superheroes('Wolverine', 12, 'Marvel', 'Tiene Garras')
personaje3 = Superheroes('Dr. Strange', 14, 'DC', 'Es mago')
personaje4 = Superheroes('Capitana America', 1964, 'DC', 'Traje')
personaje5 = Superheroes('Mujer Maravilla', 16, 'DC', 'Armadura')
personaje6 = Superheroes('Flash', 18, 'DC', 'Armadura')
personaje7 = Superheroes('Star Lord', 20, 'Marvel', 'Armadura')

lista = Lista()

lista.insert(personaje1,'nombre')
lista.insert(personaje2,'nombre')
lista.insert(personaje3,'nombre')
lista.insert(personaje4,'nombre')
lista.insert(personaje5,'nombre')
lista.insert(personaje6,'nombre')
lista.insert(personaje7,'nombre')

lista.barrido()

#a
buscado = (lista.search('Linterna Verde', 'nombre'))
if buscado != None:
    lista.delete('Linterna Verde', 'nombre')
print()
(lista.barrido())
#b
wolverine = (lista.search('Wolverine', 'nombre'))
if wolverine != None:
    print ()
    print('El año de Wolverine es: ', lista.get_element_by_index(wolverine).año)
#c
dr_strange = (lista.search('Dr. Strange', 'nombre'))
if dr_strange != None:
    lista.get_element_by_index(dr_strange).casa = 'Marvel'
print ()
lista.barrido()
print ()
#d
for i in range(0,lista.size()):
   if ('Armadura' in lista.get_element_by_index(i).bibliografia) or ('Traje' in lista.get_element_by_index(i).bibliografia):
       print (lista.get_element_by_index(i).nombre)
print()
#e
for i in range(0,lista.size()):
    if (lista.get_element_by_index(i).año < 1963):
        print(lista.get_element_by_index(i).nombre,', ', lista.get_element_by_index(i).casa)
print()
#f
capitana = (lista.search('Capitana Marvel', 'nombre'))
maravilla = (lista.search('Mujer Maravilla', 'nombre'))
if capitana != None:
    print ('La capitana Marvel pertene a la casa: ', lista.get_element_by_index(capitana).casa)
if maravilla != None:
    print ('La mujer maravilla pertene a la casa: ',lista.get_element_by_index(maravilla).casa)
print ()
#g
flash = (lista.search('Flash', 'nombre'))
lord = (lista.search('Star Lord', 'nombre'))
if flash != None:
    print (lista.get_element_by_index(flash))
if lord != None:
    print (lista.get_element_by_index(lord))
print ()
#h
for i in range (0, lista.size()):
    if lista.get_element_by_index(i).nombre[0] in ['B', 'M', 'S']:
        print (lista.get_element_by_index(i))
print ()
#i
cont = 0
cont_1 = 0
for i in range (0, lista.size()):
    if lista.get_element_by_index(i).casa == 'DC':
        cont = cont + 1
    else:
        cont_1 = cont_1 + 1
print ('La cantidad de heroes de la casa DC son: ', cont)
print ('La cantidad de heroes de la casa Marvel son: ', cont_1)