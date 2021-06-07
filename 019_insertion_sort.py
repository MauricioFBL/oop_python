import random
# Insertion Sort
# El ordenamiento por inserción
# es uno de los algoritmos más comunes que estudian
# los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy
# ineficiente para listas de gran tamaño.
# Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
# Al principio, la sublista ordenada contiene un solo elemento, por lo que por
# definición se encuentra ordenada.
# A continuación se evalua el primer elemento dentro la sublista desordenada para
# que podamos insertarlo en el lugar correcto dentro de la lista ordenada.
# La inserción se realiza al mover todos los elementos mayores al elemento que
# se está evaluando un lugar a la derecha.
# Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
# tanto, la lista se encontrará ordenada.



def insertion_sort(lista):
    """Sorts a given list of numbers using the Insertion Sort algorithm.

    The original list will be mutated.

    Time Complexity: O(n^2)
    """

    for i in range(1, len(lista)):
        temp = lista[i]
        
        print('valor actual',temp)
        j = i - 1

        while temp < lista[j] and j >= 0:
            print(j)
            print('valor comparado',lista[j + 1])
            lista[j + 1] = lista[j]
            print('valor nuevo',lista[j + 1])
            j -= 1
            print('nueva pocicion en lista',lista)
        lista[j + 1] = temp
        print(lista)



    return lista


def main():
    list_size = int(input('¿De qué tamaño será la lista?: '))

    lista = [random.randint(0, 100) for i in range(list_size)]

    print('Unsorted list', lista)
    insertion_sort(lista)
    print('Sorted list', lista)

if __name__ == '__main__':
    main()