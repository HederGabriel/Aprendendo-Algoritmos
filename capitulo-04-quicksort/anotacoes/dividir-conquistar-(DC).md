# Técnica de Dividir para Conquistar (DC)

## 1. O que é?
- **Dividir para Conquistar (DC)** não é apenas um algoritmo específico, mas sim uma **estratégia/maneira de pensar** para resolver problemas complexos ou inéditos.
- É uma abordagem essencialmente **recursiva**.

## 2. Os Dois Passos de Todo Algoritmo DC
1. **Identificar o Caso-Base:** Encontrar a versão mais simples e fácil possível do problema. 
   - *Dica:* Em funções recursivas envolvendo listas ou arrays, o caso-base quase sempre será um **array vazio** ou com **apenas 1 elemento**.
2. **Dividir/Reduzir o Problema:** Reduzir o tamanho do problema a cada passo recursivo até que ele se torne o caso-base.

---

## 3. Exemplos Práticos do Livro

### Exemplo 1: Divisão de Terreno (Algoritmo de Euclides)
- **Problema:** Dividir uma fazenda de $1680 \times 640\text{ m}$ em porções **quadradas iguais** do **maior tamanho possível**.
- **Passo Recursivo:** 
  - Encontrar o maior quadrado possível ($640 \times 640\text{ m}$). 
  - Sobra um segmento de $640 \times 400\text{ m}$.
  - Aplica-se a mesma lógica recursivamente aos segmentos restantes:
    - $640 \times 400\text{ m} \rightarrow$ sobra $400 \times 240\text{ m}$
    - $400 \times 240\text{ m} \rightarrow$ sobra $240 \times 160\text{ m}$
    - $240 \times 160\text{ m} \rightarrow$ sobra $160 \times 80\text{ m}$
- **Caso-Base:** Ao chegar em $160 \times 80\text{ m}$, descobre-se que $80$ divide $160$ perfeitamente sem sobras. Logo, o maior quadrado para toda a fazenda é **$80 \times 80\text{ m}$**.

---

### Exemplo 2: Soma Recursiva de um Array
- **Problema:** Somar todos os elementos de um array `[2, 4, 6]`.
- **Caso-Base:** Array vazio (`soma([]) = 0`) ou com 1 elemento (`soma([6]) = 6`).
- **Passo Recursivo:** Diminuir o array a cada chamada:
  $$\text{soma}([2, 4, 6]) = 2 + \text{soma}([4, 6])$$
  $$\text{soma}([4, 6]) = 4 + \text{soma}([6])$$
  $$\text{soma}([6]) = 6 \quad \text{(Caso-base)}$$
- **Desempilhando a Recursão:** O sistema recupera a memória das chamadas salvas na pilha e calcula: $4 + 6 = 10 \rightarrow 2 + 10 = 12$.