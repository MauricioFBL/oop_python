# Merge Sort
import random
def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        left = lista[:medio]
        print("Valor izquierda preorden",left)
        right = lista[medio:]
        print(left,("-"*5),right)
        merge_sort(left)
        print("Valor izquierda ordenado",left)
        merge_sort(right)
        # Iteradores para sublista
        i = 0
        j = 0
        # Iterador para lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                # print(k, lista[k], "valor en incorporacionde izquierda en i", i)
                i += 1
            else: 
                lista[k] = right[j]
                # print(k, lista[k], "valor en incorporacionde derechas en j", j)
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            # print(k, lista[k], "valor en incorporacionde sublista izquierda en i", i)
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            # print(k, lista[k], "valor en incorporacionde sublista derecha en i", i)
            j += 1
            k += 1
        
        print(f'izquireda {left}, derecha {right}')
        print(f'lista reincorporada {lista}')
        print("-"*5)
    return lista



if __name__ == '__main__':
    list_size = int(input('Cual es el tamño de la lista: '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)
    print('LISTA ORDENADA')
    print(merge_sort(lista))