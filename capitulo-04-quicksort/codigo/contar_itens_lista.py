def contar_itens_lista(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_itens_lista(lista[1:]) # 1: --> Ignora o primeiro indice (isso meio que "apaga" esse valor da próxima chamada tbm)
    
lista = ["Maça", "Banana"]

result = contar_itens_lista(lista)

print(result)