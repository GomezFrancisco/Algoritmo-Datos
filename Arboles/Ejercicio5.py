from arbol_binario import BinaryTree

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

#!A
lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

print()

#!b
print (f'Printeo alfabetico de los villanos {arbol.inorden_super_or_villano(False)}')
print()
#!C
arbol.inorden_start_with('C')
print()
#!D
print('La cantidad de superheroes es: ', arbol.contar_heroes())
print()
#!E
arbol.search_by_coincidence('do')

value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
print()
print(arbol.inorden())
print()
#!F
print(f'Barrido por nivel {arbol.by_level()}')
print()
#!G
heroes = BinaryTree()
villanos = BinaryTree()
arbol.bifurcar(heroes, villanos)

print (f'Barrido alfabetico de los heroes: ')
heroes.inorden()
print()
print (f'Barrido alfabetico de los villanos: ' )
villanos.inorden()
