import random

def llamado(lista):
    lista.sort()
    lista.append(random.randint(1,100))
    return lista

def llamado2(lista):
    lista = lista.copy()
    lista.append(random.randint(1,100))
    print('lista en funcion 2',lista)
    return lista

def llamado3(lista):
    lista = lista[::]
    lista.append(random.randint(1,100))
    print('lista en funcion 3', lista)
    return lista


lista = [10,6,8,2]
print(lista)
llamado(lista)
print(lista)
#___________
llamado2(lista)
print(lista)
#___________
llamado3(lista)
print(lista)