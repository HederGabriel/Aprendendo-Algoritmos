def achar_maior_valor(array):
    if len(array) == 1:
        return array[0]
    else:
        primeiro = array[0]
        maior_resto = achar_maior_valor(array[1:])

        if primeiro > maior_resto:
            return primeiro
        else:
            return maior_resto

arr = [50, 12, 30, 70]

print(f"O maior valor do array: {arr} é {achar_maior_valor(arr)}")