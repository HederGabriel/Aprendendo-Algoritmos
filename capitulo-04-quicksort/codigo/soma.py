def soma(arr):
    if arr == []:
        return 0
    else:
        primeiro_item = arr.pop(0)
        resultado = primeiro_item + soma(arr)
        return resultado

array = [2,4,6]
print(f"Resultado da soma do array: {array} é {soma(array)}")