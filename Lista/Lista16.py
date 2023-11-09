from Operaciones_Cola_Prioridad import ColaPrioridad

# 16_ Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

cola= ColaPrioridad()

#!A
empleados=[{'nombre':'Luis','prioridad':1},
        {'nombre':'Pedro','prioridad':1},
        {'nombre':'Maria','prioridad':1}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#!B
print('B')
print(cola.atention()[1])
print()

#!C
empleados=[{'nombre':'Jose','prioridad':2},
        {'nombre':'Monica','prioridad':2}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#!D
empleados=[{'nombre':'Maria Laura','prioridad':3}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#!E
print('E')
for i in range(2):
    print(cola.atention()[1])
print()

#!F
empleados=[{'nombre':'Juan','prioridad':1},
        {'nombre':'Jorge','prioridad':1},
        {'nombre':'Axel','prioridad':3}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])
print()

#!G
while cola.size()>0:
    print(cola.atention()[1])
print()