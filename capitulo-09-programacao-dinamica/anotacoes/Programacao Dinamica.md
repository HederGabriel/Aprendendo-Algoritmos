# Programação Dinâmica

Técnica de resolução de problemas que divide um problema complexo em **subproblemas menores**, resolve cada um e combina os resultados para chegar à solução geral.

> A ideia é resolver problemas menores primeiro e usar suas respostas para resolver problemas maiores.

## **Problema da mochila**

O objetivo é selecionar itens para maximizar o valor total sem ultrapassar a capacidade da mochila.

A solução simples testa todas as combinações possíveis. Seu tempo de execução é **O(2^n)**, pois cada novo item dobra o número de combinações.

Na programação dinâmica, é criada uma tabela:
- **Linhas:** itens disponíveis.
- **Colunas:** capacidades da mochila.
- **Células:** maior valor possível para aquela combinação de itens e capacidade.

Em cada célula, comparamos duas possibilidades:
1. Não levar o item atual e manter o melhor valor anterior.
2. Levar o item atual e somar seu valor ao melhor resultado para o espaço restante.

```text
dp[i][c] = max(
    dp[i-1][c],
    valor[i] + dp[i-1][c-peso[i]]
)
```

Se o item não couber, mantém-se o valor da linha anterior. No exemplo do livro, a melhor combinação para 4 kg é um violão e um notebook, totalizando R$ 3.500.

## **Maior substring comum**

Encontra a maior sequência de caracteres **consecutivos** que aparece em duas strings.

- Se os caracteres forem iguais: valor da célula diagonal anterior + 1.
- Se forem diferentes: valor da célula = 0.
- A resposta é o maior valor encontrado na tabela, não necessariamente a última célula.

```text
if palavra_a[i] == palavra_b[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = 0
```

## **Maior subsequência comum**

Encontra a maior sequência de caracteres que duas strings têm em comum, **mantendo a ordem, mas sem exigir que sejam consecutivos**.

- Se os caracteres forem iguais: valor da célula diagonal anterior + 1.
- Se forem diferentes: maior valor entre a célula de cima e a célula da esquerda.

```text
if palavra_a[i] == palavra_b[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

## **Quando utilizar**

- Quando for necessário **otimizar algo sujeito a um limite**, como maximizar o valor dos itens respeitando o peso da mochila.
- Quando o problema puder ser dividido em **subproblemas discretos e independentes**.

Para montar a tabela, identifique o que cada célula representa, quais são os eixos e como o resultado de um subproblema ajuda a resolver outro. **Não existe uma fórmula única** para todos os problemas de programação dinâmica.

## **Limitações e observações**

- No problema da mochila apresentado, cada item é levado por inteiro ou não é levado. Para itens fracionados, o livro apresenta o algoritmo guloso como alternativa.
- Subproblemas que dependem uns dos outros não se encaixam nessa abordagem apresentada no capítulo.
- A tabela precisa considerar as capacidades relevantes. Se houver um item de 0,5 kg, por exemplo, uma tabela calculada apenas com intervalos de 1 kg precisará ser refinada.
- A melhor solução não precisa utilizar toda a capacidade disponível.

## **Aplicações**

- Comparação de sequências de DNA.
- Comparação de diferenças entre arquivos, como no `git diff`.
- Distância Levenshtein, utilizada em corretores ortográficos.
- Organização de quebras de linha em editores de texto.

## **Recapitulando**

- A programação dinâmica resolve problemas maiores a partir de subproblemas menores.
- As soluções são organizadas em uma tabela.
- Cada célula representa um subproblema.
- Os valores armazenados representam aquilo que se deseja otimizar.
- A fórmula depende do problema; não existe uma fórmula universal.