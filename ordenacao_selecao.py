def buscamenor(arr):
    menor = arr[0]
    indice_menor = 0

    for i in range(len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indice_menor = i
    return indice_menor

def ordencaoSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscamenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordencaoSelecao([5,3,6,2,10]))
