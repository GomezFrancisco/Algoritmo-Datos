from lista import Lista
from ListaAux import ListaAuxiliar
from cola import Cola

class Superheroe: 
    def __init__(self, nombreSuper, nombrePersonaje, grupo, anio):
        self.nombreSuper = nombreSuper
        self.nombrePersonaje = nombrePersonaje
        self.grupo = grupo
        self.anio = anio

    def __str__(self) -> str:
        return f'"Superheroe: " - {self.nombreSuper} - "Personaje: " - {self.nombrePersonaje} - "Grupo: " - {self.grupo} - "Año: "- {self.anio}'
    
S1 = Superheroe("Starlord", "Peter Quill", "Guardianes de las Galaxias", 1976)
S2 = Superheroe("Capitana Marvel", "Rose", "Guardianes de las Galaxias", 1958)
S3 = Superheroe("Roca", "Rock", "Los cuatro Fantásticos", 1957)
S4 = Superheroe("Hulk", "Peter Quill", "Guardianes de las Galaxias", 1959)
S5 = Superheroe("Superman", "Peter Quill", "Guardianes de las Galaxias", 1961)
S6 = Superheroe("Linterna Verde", "Peter Quill", "Guardianes de las Galaxias", 1962)
S7 = Superheroe("Vlanck Widow", "Peter Quill", "Guardianes de las Galaxias", 1955)
S8 = Superheroe("Hombre araña", "Peter Quill", "Guardianes de las Galaxias", 1964)
S9 = Superheroe("Pedro", "Peter Quill", "Guardianes de las Galaxias", 1975)
S10 = Superheroe("a", "a", "a", 1)
S11 = Superheroe("b", "b", "b", 2)
S12 = Superheroe("c", "c", "c", 3)
S13 = Superheroe("d", "d", "d", 4)
S14 = Superheroe("e", "e", "e", 5)
S15 = Superheroe("f", "f", "f", 6)
S17 = Superheroe("g", "g", "g", 0)

L = Lista()

L.insert(S1, 'nombreSuper')
L.insert(S2, 'nombreSuper')
L.insert(S3, 'nombreSuper')
L.insert(S4, 'nombreSuper')
L.insert(S5, 'nombreSuper')
L.insert(S6, 'nombreSuper')
L.insert(S7, 'nombreSuper')
L.insert(S8, 'nombreSuper')
L.insert(S9, 'nombreSuper')
L.insert(S10, 'nombreSuper')
L.insert(S11, 'nombreSuper')
L.insert(S12, 'nombreSuper')
L.insert(S13, 'nombreSuper')
L.insert(S14, 'nombreSuper')
L.insert(S15, 'nombreSuper')
L.insert(S17, 'superNombre')

# ------------------------------------------

#a
capitana = L.search("Capitana Marvel", "nombreSuper")
if capitana != None:
    print ("El nombre de la capitana es: ", L.get_element_by_index(capitana).nombrePersonaje)
else:
    print("La capitana Marvel no se encuentra en la lista.")
print()

#b
cola = Cola()
for i in range(L.size()):
    if L.get_element_by_index(i).grupo == "Guardianes de las Galaxias":
        cola.arrive(L.get_element_by_index(i))
    else:
        pass

contador = 0
while cola.size() > 0:
    cola.atention()
    contador += 1

print ('El número de superheroes pertenecientes a los Guardianes de las Galaxias son: ', contador)
print()

#C
C = ["Guardianes de las Galaxias", "Los cuatro Fantásticos"]
LAux = Lista()
for i in range(L.size()):
    if L.get_element_by_index(i).grupo in C:
        LAux.insert(L.get_element_by_index(i), "nombreSuper")

LAux.order_by("nombreSuper", True)
LAux.barrido()
print()

#D
for i in range(L.size()):
    if L.get_element_by_index(i).anio > 1960:
        print (L.get_element_by_index(i))
    else:
        pass
print()

#E
Widow = L.search("Vlanck Widow", "nombreSuper")
if Widow != None:
    L.delete("Vlanck Widow", "nombreSuper")
    S16 = Superheroe("Black Widow", "", "", 0)
    L.insert(S16, "nombreSuper")
else:
    pass
L.barrido()
print()

# #F
# for i in ListaAuxiliar:
#     L.insert(Superheroe(i["nombreSuper"],i["nombrePersonaje"],i["grupo"],i["anio"]), 'nombreSuper')
# L.barrido()

#G
Letras = ["C", "P", "S"]
for i in range(L.size()):
    if L.get_element_by_index(i).nombreSuper[0] in Letras:
        print (L.get_element_by_index(i))