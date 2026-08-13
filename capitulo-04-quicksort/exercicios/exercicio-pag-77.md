# 4.1 Escreva o código para a função soma, vista anteriormente

### R: 
```python
def soma(arr):
    if arr == []:
        return 0
    else:
        primeiro_item = arr.pop(0)
        resultado = primeiro_item + soma(arr)
        return resultado

array = [2,4,6]
print(f"Resultado da soma do array: {array} é {soma(array)}")
```

Arquivo [aqui](../codigo/soma.py)

# 4.2 Escreva uma função recursiva que conte o número de itens em uma lista.

### R: 
```python
def contar_itens_lista(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_itens_lista(lista[1:]) # 1: --> Ignora o primeiro indice (isso meio que "apaga" esse valor da próxima chamada tbm)
    
lista = ["Maça", "Banana"]

result = contar_itens_lista(lista)

print(result)
```

Arquivo [aqui](../codigo/contar_itens_lista.py)

# 4.3 Encontre o valor mais alto de uma lista.

### R: 
```python
def achar_maior_valor(array):
    if len(array) == 1:
        return array[0]
    else:
        primeiro = array[0]
        maior_resto = achar_maior_valor(array[1:])

        if primeiro > maior_resto:
            return primeiro
        else:
            return maior_resto

arr = [50, 12, 30, 70]

print(f"O maior valor do array: {arr} é {achar_maior_valor(arr)}")
```

Arquivo [aqui](../codigo/valor_mais_alto.py)

# 4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo do tipo dividir para conquistar. Você consegue determinar o caso-base e o caso recursivo para a pequisa binária?

### R: **Caso-base** (2 possibilidades):
1. Se for igual ao que procura → achou.
2. Se a lista acabar → o valor não existe na lista.

### R: **Caso recursivo** (2 possibilidades):
1. Se `chute < meio` → busca recursivamente na metade esquerda.
2. Se `chute > meio` → busca recursivamente na metade direita.