'''
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.
'''
from cola import Cola

Personajes_MCU = [
    {'Nombre_Personaje': 'Tony Stark','Nombre_Superheroe': 'Iron Man','Género': 'M'},
    {'Nombre_Personaje': 'Steve Rogers','Nombre_Superheroe': 'Capitán América','Género': 'M'},
    {'Nombre_Personaje': 'Natasha Romanoff','Nombre_Superheroe': 'Black Widow','Género': 'F'},
    {'Nombre_Personaje': 'Brie Larson','Nombre_Superheroe': 'Capitana Marvel','Género': 'F'},
    {'Nombre_Personaje': 'Scott Lang','Nombre_Superheroe': 'Ant-Man','Género': 'M'},
    {'Nombre_Personaje': 'Carol Danvers','Nombre_Superheroe': 'S','Género': 'F'}]

cola = Cola()

for x in Personajes_MCU:
    cola.arrive(x)

while cola.size() > 0:
    Personaje = cola.atention()
    
    if Personaje['Nombre_Superheroe'] == 'Capitana Marvel':
        print ('El nombre de la Capitana Marvel es: ', Personaje['Nombre_Personaje'])
    
    if Personaje['Género'] == 'F':
        print ('El nombre del superheroe es: ', Personaje['Nombre_Superheroe'])
    elif Personaje['Género'] == 'M':
        print ('El nombre del personaje es: ', Personaje['Nombre_Personaje'])

    if Personaje['Nombre_Personaje'] == 'Scott Lang':
        print ('El nombre del superheroe es: ', Personaje['Nombre_Superheroe'])
    
    if (Personaje['Nombre_Personaje'][0] == 'S') or (Personaje['Nombre_Superheroe'][0] == 'S'):
        print ('Nombre del personaje: ', Personaje['Nombre_Personaje'], ', ', 'Nombre de superheroe: ', Personaje['Nombre_Superheroe'],', ', 'Género: ', Personaje['Género'])

    if Personaje['Nombre_Personaje'] == 'Carol Danvers':
        print ('Carol Danvers se encuentra en la cola, y su nombre de superheroe es: ', Personaje['Nombre_Superheroe'])