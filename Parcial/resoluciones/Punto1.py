V =['wea','wea','wea','wea','wea','a','a','a','a','a','a','a']

palabra=input('Ingrese palabra a buscar: ')

def cont_palabras(vector,palabra):
    if len(vector)==0:
        return 0
    elif vector[-1]==palabra:
        return 1 + cont_palabras(vector[:-1],palabra)
    else:
        return cont_palabras(vector[:-1],palabra)

Contador= cont_palabras(V,palabra)
print ("La palabra seleccionada se ejecutó: ", Contador)