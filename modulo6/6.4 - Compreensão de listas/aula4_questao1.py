pares = [x for x in range(20, 51) if x % 2 == 0]
quadrados = [x**2 for x in range(1, 10)]
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
paridade = ['par' if x % 2 == 0 else 'impar' for x in range(0, 30, 3)]

print("Pares entre 20 e 50:", pares)
print("Quadrados:", quadrados)
print("Divisíveis por 7:", divisiveis_por_7)
print("Par ou Ímpar:", paridade)
