# Pilha

Suponhamos que você tenha uma lista de afazeres em uma pilha de bloco de notas

![Pilha de Anotações em um bloco de notas](img/bloco-nota.png)

em um bloco de notas, você adiciona uma tarefa no topo do bloco, e quando você vai ler um item, você tira ele do topo do bloco de anotações.

Logo, essa lista de afazeres só tem duas ações:
- `push` (inserir)
- `pop` (remover e ler)

![img.png](img/push-pop.png)

### Na Prática funciona assim:
![img.png](img/fluxo-pilha.png)
> está estrutura de dados é chamada de **_pilha_**.

---

# Pilha de Chamada (``call stack``)
Seu computador usa uma pilha interna denominada _**pilha de chamada**_.

## Exemplo prático simples:
````python
def sauda2(nome):
    print("Como vai " + nome + "?")
    
def tchau():
    print("ok, tchau!")
    
def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()
````


