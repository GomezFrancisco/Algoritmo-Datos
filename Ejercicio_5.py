#5. Determinar si una cadena de caracteres es un palíndromo.
from pila import Pila

#Palabra --> Asigna a pila_principal --> pop --> pila_main.push (pila_soporte.pop)
#Pila_soporte --> pila_soporte.push (pila_main.pop) 
#Pila_comparativa --> pila_soporte.push (pila_main.pop) --> lista invertida

pila_principal = Pila()
palabra = input('ingrese una palabra: ')

for i in palabra:
    pila_principal.push(i)

print (pila_principal)

pila_soporte = Pila()
pila_comparativa = Pila()

while pila_principal.size() > 0:
    pila_soporte.push (pila_principal.pop())
    pila_comparativa.push (pila_principal.pop())

while pila_soporte.size() > 0:
    pila_principal.push (pila_soporte.pop())


if pila_principal == pila_comparativa:
    print('La palabra es un palíndromo.')

print (pila_principal)
print (pila_comparativa)