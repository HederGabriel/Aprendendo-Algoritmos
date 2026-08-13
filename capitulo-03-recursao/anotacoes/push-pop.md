# As Duas Operações Principais

## 📥 `push` (Empilhar)
- **Conceito:** Adiciona um novo elemento no **topo** da pilha.
- **Na Recursão (Call Stack):** Cada vez que uma função chama a si mesma, um novo **quadro de pilha (stack frame)** é criado e colocado no topo da *Call Stack*. Esse quadro guarda:
  - Argumentos da função
  - Variáveis locais
  - Endereço de retorno (para onde voltar após concluir)

## 📤 `pop` (Desempilhar)
- **Conceito:** Remove o elemento do **topo** da pilha e o retorna.
- **Na Recursão (Call Stack):** Quando uma função atinge seu `return` (ou o **Caso Base**), o seu quadro de pilha é removido do topo. O controle retorna para a função imediatamente abaixo na pilha.

---

## ⚡ Resumo Rápido

| Operação | Ação no Topo | Papel na Recursão |
| :--- | :--- | :--- |
| **`push`** | Adiciona elemento | Ocorre a cada **nova chamada** recursiva |
| **`pop`** | Remove elemento | Ocorre a cada **retorno** de função (`return`) |