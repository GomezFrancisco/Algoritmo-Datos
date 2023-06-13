from pila import Pila

Misiones = [
    {"Planeta": "a", "Capturado": "Han Solo", "Recompensa": 0},
    {"Planeta": "b", "Capturado": "a", "Recompensa": 1},
    {"Planeta": "c", "Capturado": "a", "Recompensa": 2},
    {"Planeta": "d", "Capturado": "a", "Recompensa": 3},
    {"Planeta": "e", "Capturado": "a", "Recompensa": 4},
    {"Planeta": "f", "Capturado": "a", "Recompensa": 5},
    ]
pila = Pila()
for i in Misiones:
    pila.push(i)
Contador = 0
Acumulador = 0
while pila.size()>0:
    E = pila.pop()
    Acumulador = Acumulador + E["Recompensa"]
    print ('La misión del planeta: ', E["Planeta"], ", se hizo en el orden: ", (pila.size() + 1))
    if E["Capturado"] == "Han Solo":
        Contador += 1
        print ("Han solo fue capturado en el planeta: ", E["Planeta"])
    
print ("Han Solo fue capturado: ", Contador)
print ("El número de créditos acumulados es de: ", Acumulador)