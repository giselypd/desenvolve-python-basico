import random

lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

print("Lista 1:", sorted(lista1))
print("Lista 2:", sorted(lista2))

inters = []
for elemento in lista1:
    if elemento in lista2 and elemento not in inters:
        inters.append(elemento)

inters.sort()
print("Interseccao:", inters)

print("Contagem")
for i in inters:
    print(f"{i}: (lista1={lista1.count(i)}, lista2={lista2.count(i)})")
