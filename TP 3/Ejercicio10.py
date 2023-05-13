'''
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra ‘Python’, si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son.
'''

from pila import Pila
from cola import Cola

Notificaciones = [
    {'Hora': 11.43, 'Aplicación': 'Facebook','Mensaje':'a'},
    {'Hora': 12.43, 'Aplicación': 'Twitter','Mensaje':'a' },
    {'Hora': 13.43, 'Aplicación': 'Twitter','Mensaje': 'Phyton'},
    {'Hora': 14.43, 'Aplicación': 'Instagram','Mensaje': 'a'},
    {'Hora': 15.57, 'Aplicación': 'LinkedIn','Mensaje': 'a'},
    {'Hora': 16.00, 'Aplicación': 'Facebook','Mensaje':'a' }
    ]

pila = Pila()
cola = Cola()
cola_auxiliar = Cola()
cola_twitter = Cola()

for x in Notificaciones:
    cola.arrive(x)

while cola.size() > 0:
    Notificación = cola.atention()
    if (Notificación['Hora'] >= 11.43) and (Notificación['Hora'] <= 15.57):
        pila.push(Notificación)
    if Notificación['Aplicación'] != 'Facebook':
        cola_auxiliar.arrive(Notificación)
    if (Notificación['Aplicación'] == 'Twitter') and  ('Python' in Notificación['Mensaje']):
        cola_twitter.arrive(Notificación)
        #print ('Hora: ', Notificación['Hora'], 'Aplicación: ', Notificación['Aplicación'], 'Mensaje: ', Notificación['Mensaje'])
        print (Notificación)

print ('La cantidad de notificaciones que se almacenaron fue de: ', (pila.size()))