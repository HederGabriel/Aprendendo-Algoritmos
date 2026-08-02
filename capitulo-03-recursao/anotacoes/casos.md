# Caso-Base e Caso Recursivo

É fácil escrever uma função recursiva de forma incorreta e acabar caindo em um **loop infinito**.

---

## ❌ Maneira Errada

Imagine que você queira criar uma função para exibir uma contagem regressiva:

> **Saída desejada:** `3...2...1`

Se você escrever a função assim:

```python
def regressiva(i):
    print(i)
    regressiva(i - 1)
```
O resultado será um estouro de **pilha** (**stack overflow**) por conta do loop infinito:

```
Saída: 3...2...1...0...-1...-2...
[Loop Infinito]
```

---

## ✅ Maneira Correta
Toda função recursiva bem estruturada deve ser dividida em duas partes essenciais:

1. Caso-Base: A condição de parada que interrompe as chamadas.
2. Caso Recursivo: A etapa em que a função chama a si mesma com um novo valor.

> 💡 Dica: Pense nisso como uma estrutura if / else básica: o if decide se é hora de parar (caso-base) e o else dá continuidade à recursão (caso recursivo).

Exemplo corrigido:
```python
def regressiva(i):
    print(i)
    # Caso-Base: Interrompe a execução
    if i <= 1:
        return
    # Caso Recursivo: Chama a si mesma reduzindo o valor
    else:
        regressiva(i - 1)
```
```
Saída: 3...2...1
```
