# Busqudas Binaria
# funcina con listas ordenadas

import random
def busqueda_binaria(lista, objetivo, inicio, final):
    match =  False
    if inicio > final:
        return False

    medio = (inicio + final) // 2
    print(lista[medio])
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, final)
    else:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    


    return match

if __name__ == '__main__':
    list_size = int(input('Cual es el tamño de la lista: '))    
    objetivo = int(input('Cual es el numero que estas buscando: '))
    lista = sorted([random.randint(0, 100) for i in range(list_size)])
    encontrado = busqueda_binaria(lista,objetivo, 0, len(lista))
    print(lista)
    print(f'el numero {objetivo} {"esta" if encontrado else "No esta"} en la lista' )






