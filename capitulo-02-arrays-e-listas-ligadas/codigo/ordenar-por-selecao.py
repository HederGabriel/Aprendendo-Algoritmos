def buscaMenor(arr):
    menor_valor = arr[0]          # menor recebe o valor do primeiro índice do array
    menor_indice = 0              # Começa zerado

    for i in range(1, len(arr)):  # Começa no índice 1

        if arr[i] < menor_valor:
            menor_valor = arr[i] 
            menor_indice = i

    return menor_indice

def ordenar(arr):
    novo_arr = []

    for i in range(len(arr)):

        menor_valor = buscaMenor(arr)
        novo_arr.append(arr.pop(menor_valor))           #pop() --> remove e retorna um elemento

    return novo_arr

arr = [5, 3, 6, 2, 10]
arr_ordenado = ordenar(arr)
print(arr_ordenado)