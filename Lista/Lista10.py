'''
Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista,
duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
permita realizar las siguientes actividades:
a. obtener la información de la canción más larga;
b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
c. obtener todas las canciones de la banda Arctic Monkeys;
d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
'''

from Clase_Lista import Lista

class Spotify:
    def __init__(self, nombre, autor, duracion, reproducciones):
        self.nombre = nombre
        self.autor = autor
        self.duracion = duracion
        self.reproducciones = reproducciones
    
    def __str__(self):
        return f'{self.nombre} - {self.autor} - {self.duracion} - {self.reproducciones}'

C1 = Spotify('Jazz','a',8.30,5)
C2 = Spotify('Rumba','b',5.30,40)
C3 = Spotify('Disco','Artic Monkeys',3.30,50)
C4 = Spotify('Salsa','d',6.30,10)
C5 = Spotify('Merengue','e',4.30,20)

lista = Lista()

lista.insert(C1, 'reproducciones')
lista.insert(C2, 'reproducciones')
lista.insert(C3, 'reproducciones')
lista.insert(C4, 'reproducciones')
lista.insert(C5, 'reproducciones')

lista.barrido()

#a
print ()
largo = 0
posicion = 0
for i in range(0,lista.size()):
    if (lista.get_element_by_index(i).duracion >= largo):
        largo = lista.get_element_by_index(i).duracion
        posicion = i
print ('La canción más larga es: ', lista.get_element_by_index(posicion))
print ()
#b
lista.order_by('reproducciones', True)
lista.barrido()
print ()
#c
for i in range(0, lista.size()):
    if lista.get_element_by_index(i).autor == 'Artic Monkeys':
        print ('La canción de Artic Monkeys es: ', lista.get_element_by_index(i).nombre)
print()
#d
for i in range (lista.size()):
    if ' ' not in lista.get_element_by_index(i).autor:
        print(lista.get_element_by_index(i).autor)