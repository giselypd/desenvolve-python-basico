import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_negativos = 0
inicio = 0
fim = 0

for i in range(len(lista)):
    negativos = 0
    for j in range(i, len(lista)):
        if lista[j] < 0:
            negativos += 1
        if negativos > max_negativos:
            max_negativos = negativos
            inicio = i
            fim = j

del lista[inicio:fim + 1]
print("Editada:", lista)
