def pesquisa_binaria(lista, item):
    inicio = 0 # Ínicío do intervalo de busca
    fim = len(lista)-1 # Fim do intervalo de busca
    while inicio <= fim: # enquanto o inicio não for maior que o fim
        meio = (inicio + fim) // 2 # Descobre a posição do meio
        chute = lista[meio] # chute = ao item da lista que tem a posição = meio
        if chute == item:
            return meio # retorna meio que é a posição do item que tá sendo buscado
        elif chute > item: # chute alto
            fim = meio - 1  # diminui 1 posição do fim
        else:
            inicio = meio + 1 # aumenta 1 posição do inicio
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))