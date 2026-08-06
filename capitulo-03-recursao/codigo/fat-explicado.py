# Função recursiva - Fatorial 
# Saída desse código serve para demostrar o fluxo de retorno da call stack / ignore o código

def fat(x):
    if x == 1:
        print(f"fat({x}) -- 1")
        return 1
    else:
        # 1. Executa a recursão primeiro e guarda o resultado retornado do nível abaixo
        sub_resultado = fat(x - 1)
        
        # 2. Calcula o valor atual usando o retorno recebido
        resultado_atual = x * sub_resultado
        
        # 3. Imprime o fluxo de retorno correto
        print(f"fat({x}) -- {x} x {sub_resultado} = {resultado_atual}")
        
        return resultado_atual

resultado = fat(4)
print()
print(f"Resultado: {resultado}")
input("Aperte Enter")