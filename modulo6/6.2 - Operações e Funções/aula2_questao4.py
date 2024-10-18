def obter_lista(numero_lista):
    tamanho = int(input(f"Digite a quantidade de elementos da lista {numero_lista}: "))
    lista = []
    print(f"Digite os {tamanho} elementos da lista {numero_lista}:")
    for i in range(tamanho):
        lista.append(int(input()))
    return lista

lista1 = obter_lista(1)
lista2 = obter_lista(2)

lista_intercalada = []
for i in range(max(len(lista1), len(lista2))):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
