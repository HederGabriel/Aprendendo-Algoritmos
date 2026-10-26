# Tabelas Hash

Uma **tabela hash** é uma estrutura de dados que associa **chaves a valores**, permitindo pesquisar, inserir e remover informações rapidamente.

Em Python, é representada por um dicionário (`dict`).

```python
precos = {"maçã": 0.67, "leite": 1.49}

print(precos["maçã"])  # 0.67
```

## Funções Hash

Uma **função hash** transforma uma chave em um número que indica onde seu valor será armazenado.

Uma boa função hash deve:

- **Ser consistente:** a mesma entrada sempre retorna o mesmo resultado.
- **Distribuir bem as chaves:** evitar que muitas chaves sejam direcionadas à mesma posição.
- **Retornar uma posição válida** na tabela.

## Utilização

As tabelas hash são úteis para:

- **Pesquisas:** associar nomes a telefones, produtos a preços ou domínios a endereços IP.
- **Evitar duplicatas:** verificar se um elemento já foi registrado, como um eleitor que já votou.
- **Cache:** armazenar resultados para reutilizá-los, evitando repetir operações e tornando as consultas mais rápidas.

## Colisões

Uma **colisão** ocorre quando duas chaves diferentes são direcionadas à mesma posição da tabela.

Uma solução apresentada no livro é utilizar uma **lista encadeada** nessa posição para armazenar as chaves que colidiram.

Muitas colisões tornam essas listas maiores e prejudicam o desempenho. Por isso, é importante ter uma boa função hash e controlar o fator de carga.

## Desempenho

| Operação | Caso médio | Pior caso |
|:--|:--:|:--:|
| Pesquisa | \(O(1)\) | \(O(n)\) |
| Inserção | \(O(1)\) | \(O(n)\) |
| Remoção | \(O(1)\) | \(O(n)\) |

No caso médio, as operações têm tempo **\(O(1)\), ou constante**. No pior caso, muitas colisões podem fazer com que o tempo chegue a \(O(n)\).

## Fator de Carga

O **fator de carga** indica a proporção entre os itens armazenados e as posições disponíveis na tabela.

\[
\text{Fator de carga} =
\frac{\text{Número de itens}}{\text{Número de posições}}
\]

Quando o fator de carga aumenta, podem ocorrer mais colisões. Para reduzi-lo, a tabela pode ser **redimensionada**, aumentando o array e reinserindo os elementos.

O livro apresenta como regra prática redimensionar quando o fator de carga ultrapassa **0,7**.

## Uma Boa Função Hash

Uma boa função hash distribui as chaves uniformemente pelas posições disponíveis. Uma função ruim concentra muitas chaves em poucos espaços, aumentando as colisões.

## Recapitulando

- Tabelas hash associam chaves a valores.
- Funções hash determinam onde armazenar e encontrar os valores.
- Colisões acontecem quando chaves diferentes apontam para a mesma posição.
- No caso médio, as operações são \(O(1)\); no pior caso, podem ser \(O(n)\).
- Uma boa função hash e um fator de carga controlado ajudam a manter o desempenho.
- Os principais usos são pesquisas, prevenção de duplicatas e cache.
