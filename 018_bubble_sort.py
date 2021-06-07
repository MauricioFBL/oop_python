# Ordenamiento de Burbuja
# recorre la lsita y compara valores para ir ordenando los valores de manera decuada
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1 -1):
            if lista[j] > lista[ j + 1]:
                lista[j] , lista[j + 1] = lista[j + 1], lista[j]
    return lista





if __name__ == '__main__':
    list_size = int(input('Cual es el tamño de la lista: '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    # encontrado = busqueda_binaria(lista,objetivo, 0, len(lista))
    print(lista)
    print('ordenada')
    print(bubble_sort(lista))

