'''
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
para encontrarlo;
c. Utilizar un vector para representar la mochila.
'''

#Sección a

mochila = ['pan','agua','sable de luz','vendajes','ropa']
contador = 0

def usar_la_fuerza(lista,contador):
    if len(lista) == 0:
        return -1
    elif lista[-1] == 'sable de luz':
        return contador + 1
    else:
       contador=contador+1
       return usar_la_fuerza(lista[:-1],contador)

contador = (usar_la_fuerza(mochila,contador))

if contador != -1:
    print ('Se ha encontrado el sable de luz')
    print(f' y fue necesario sacar {contador} objetos')
else:
    print ('El sable de luz no se encuentra en la mochila')