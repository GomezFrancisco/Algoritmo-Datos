V =['wea','wea','wea','wea','wea','a','a','a','a','a','a','a']

palabra=input('Ingrese palabra a buscar: ')

def contador_palabra(vector,palabra):
    if len(vector)==0:
        return 0
    elif vector[-1]==palabra:
        return 1 + contador_palabra(vector[:-1],palabra)
    else:
        return contador_palabra(vector[:-1],palabra)

Contador= contador_palabra(V,palabra)
print ("La palabra seleccionada se ejecutó: ", Contador)