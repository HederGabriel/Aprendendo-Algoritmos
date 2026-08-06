# Função recursiva - Fatorial

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

resultado = fat(4)
print()
print(f"Resultado: {resultado}")
input("Aperte Enter")