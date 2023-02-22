def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))
    lista_sem_repeticao.sort()
    return lista_sem_repeticao

lista = [2, 4, 2, 2, 3, 3, 1]
lista_sem_repeticao = remove_repetidos(lista)
print(lista_sem_repeticao)

