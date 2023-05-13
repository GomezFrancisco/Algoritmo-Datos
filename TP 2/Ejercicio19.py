'''
Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
'''
from pila import Pila

peliculas=[
    {'Nombre': 'Uno', 'Estudio': 'Uno', 'Anio': '2014'},
    {'Nombre': 'Dos', 'Estudio': 'Uno', 'Anio': '2014'},
    {'Nombre': 'Tres', 'Estudio': 'Uno', 'Anio': '2018'},
    {'Nombre': 'Cuatro', 'Estudio': 'Uno', 'Anio': '2018'},
    {'Nombre': 'Cinco', 'Estudio': 'Marvel', 'Anio': '2016'}]

pila = Pila();
for x in peliculas:
    pila.push(x)

cont = 0
while pila.size() > 0:
    pelicula = pila.pop()
    if pelicula['Anio'] == '2014':
        print (pelicula['Nombre'])
    elif pelicula['Anio'] == '2018':
        cont += 1
    elif pelicula['Estudio'] == 'Marvel' and pelicula['Anio'] == '2016':
        print (pelicula)

print ('La cantidad de películas estrenadas en el 2018 es de: ', cont)