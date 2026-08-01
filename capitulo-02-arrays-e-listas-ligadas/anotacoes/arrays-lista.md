# Arrays e Listas Encadeadas

Estruturas de dados fundamentais para armazenar coleções de itens, cada uma com um jeito diferente de organizar a
memória — e, por consequência, vantagens e desvantagens opostas.

## Sumário

- [Array](#array)
- [Lista Encadeada](#lista-encadeada)
- [Comparação](#comparação)

---

## Array

Usar um array significa que todos os itens estão armazenados **contiguamente** (um ao lado do outro) na memória.

![Representação de um array na memória](img/Array.png)

> **Nota:** Quando não há espaço contíguo suficiente para um novo item, o sistema aloca um bloco de memória maior, copia
> todos os elementos antigos para esse novo local e descarta a memória anterior.

### Vantagens e Desvantagens

| ✅ | Leitura instantânea, independente do índice (posição do item) |
|---|---------------------------------------------------------------=|
| ❌ | Inserção pode demorar cada vez mais conforme o array cresce |

---

## Lista Encadeada

Em uma lista encadeada, os itens podem estar em **qualquer lugar** da memória.

![Representação de uma lista encadeada na memória](img/Lista-Encadeada.png)

> **Nota:** Cada item armazena o endereço do próximo item da lista — um monte de endereços aleatórios de memória
> interligados.

### Vantagens e Desvantagens

| ❌ | Leitura fica cada vez mais lenta conforme a lista encadeada cresce |
|---|--------------------------------------------------------------------|
| ✅ | Inserção instantânea, independente do tamanho da lista             |

---

## Comparação

|            | Arrays | Listas Encadeadas |
|:-----------|:------:|:-----------------:|
| **Write**  |  O(1)  |       O(n)        |
| **Read**   |  O(n)  |       O(1)        |
| **Delete** |  O(n)  |       O(1)        |

> - **O(n)** = tempo de execução **linear**
> - **O(1)** = tempo de execução **constante**