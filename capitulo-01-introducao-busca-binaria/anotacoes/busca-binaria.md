# Capítulo 1

> Geralmente, você escolhe o algoritmo mais eficiente — caso esteja tentando otimizar tempo e espaço. <br>
> — *Aditya Y. Bhargava*

---

## Busca Binária

A busca binária diminui **muito** a quantidade de etapas em uma requisição de busca.

* **Exemplo:** Um dicionário com **240.000 palavras**.
    * **Busca simples (pior hipótese):** 240.000 etapas.
    * **Busca binária (pior hipótese):** apenas 18 etapas.

---

### Etapas Máximas no Pior dos Casos

$$O\lfloor \log_2 n \rfloor + 1$$

---

### Tempo de Execução

| Métrica                 | Pesquisa Simples       | Pesquisa Binária |
|:------------------------|:-----------------------|:-----------------|
| **100 itens**           | 100 palpites           | 7 palpites       |
| **4.000.000.000 itens** | 4.000.000.000 palpites | 32 palpites      |
| **Complexidade**        | $n$                    | $(\log n) + 1$   |
| **Tempo de Execução**   | Linear                 | Logarítmico      |
