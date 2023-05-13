'''
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''

from pila import Pila

Personajes = [
    {'Nombre': 'Rocket Raccoon', 'Participaciones': 1},
    {'Nombre': 'Uno', 'Participaciones': 5},
    {'Nombre': 'Dos', 'Participaciones': 6},
    {'Nombre': 'Black Widow', 'Participaciones': 3},
    {'Nombre': 'Groot', 'Participaciones': 1}]

pila = Pila()

for i in Personajes:
    pila.push(i)

cont = 0
while pila.size() > 0:
    Personaje = pila.pop();
    if Personaje['Nombre'] == 'Rocket Raccoon' or Personaje['Nombre'] == 'Groot':
        print (Personaje['Nombre'], ' se encuentra en la posición: ', (pila.size()+ 1))
    elif Personaje['Participaciones'] > 5:
        cont += 1
    elif Personaje['Nombre'] == 'Black Widow':
        print ('Black Widow participó en: ', Personaje['Participaciones'])
    elif Personaje['Nombre'][0] in ['C', 'D', 'G']:
        print ('Nombre: ', Personaje['Nombre'], 'Participaciones: ', Personaje['Participaciones'])
    
print ('El número de personajes que estuvieron en más de 5 películas es de: ', cont)