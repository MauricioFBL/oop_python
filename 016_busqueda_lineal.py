# Busqudas Lineal
import random
def busqueda_lineal(lista, objetivo):
    match =  False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    list_size = int(input('Cual es el tamño de la lista: '))    
    objetivo = int(input('Cual es el numero que estas buscando: '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'el elmeento {objetivo} {"esta" if encontrado else "No esta"} en la lista' )






